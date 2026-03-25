import random
import math
import matplotlib.pyplot as matplotlib
import numpy as numpy_np
import pandas as pandas_pd

def gerar_intervalos(tempo_medio):
    # X = -ln(U) / λ
    if tempo_medio <= 0:
        return 0
    
    u = random.random()
    if u == 0:
        u = 0.0001
    
    _lambda = 1.0 / tempo_medio
    
    return -math.log(u) / _lambda

def calcular_media(lista_numeros):
    if not lista_numeros:
        return 0
    
    # Otimizar com array e calcular media
    return numpy_np.mean(numpy_np.array(lista_numeros))

def calcular_estatistica(lista_numeros):
    if not lista_numeros:
        return {}
    
    array_otimizado =  numpy_np.array(lista_numeros)

    estatistica = {
        'media': numpy_np.mean(array_otimizado),
        'mediana': numpy_np.median(array_otimizado),
        'desvio_padrao': numpy_np.std(array_otimizado),
        'variancia': numpy_np.var(array_otimizado),
        'minimo': numpy_np.min(array_otimizado),
        'maximo': numpy_np.max(array_otimizado),
        'percentil_25': numpy_np.percentile(array_otimizado, 25),
        'percentil_50': numpy_np.percentile(array_otimizado, 50), #Mediana
        'percentil_75': numpy_np.percentile(array_otimizado, 75),
        'quantidade': len(array_otimizado)
    }

    return estatistica

def gerar_dataframe(resultados_simulacao):
    # Transformar em DataFrame (estilo Excel) e deixar na vertical usando T 
    # Convert scalar values to lists for DataFrame creation
    data_dict = {}
    for key, value in resultados_simulacao.items():
        if isinstance(value, (int, float)):
            data_dict[key] = [value]
        else:
            data_dict[key] = value
    
    data_frame = pandas_pd.DataFrame(data_dict).T

    # Dar nome a coluna dos valores
    data_frame.columns = ['valor']
    #Criar a linha sobre a configuracao da simulacao 
    data_frame.loc['Configuracao'] = ['Taxa Chegada: 3, Taxa Atendimento: 5, Tempo: 1000']

    return data_frame

def comparador_matematico(resultados_simulacao):
    dados_comparacao = {
        'Metrica': [
            'Tempo Medio no Sistema',
            'Tempo Medio na Fila',
            'Numero Medio no Sistema',
            'Numero Medio na Fila'
        ],
        'Simulado': [
            resultados_simulacao['tempo_medio_sistema_simulado'],
            resultados_simulacao['tempo_medio_fila_simulado'],
            resultados_simulacao['numero_medio_sistema_simulado'],
            resultados_simulacao['numero_medio_fila_simulado']
        ],
        'Teorico': [
            resultados_simulacao['tempo_medio_sistema_teorico'],
            resultados_simulacao['tempo_medio_fila_teorico'],
            resultados_simulacao['numero_medio_sistema_teorico'],
            resultados_simulacao['numero_medio_fila_teorico']
        ]
    }
    data_frame = pandas_pd.DataFrame(dados_comparacao)

    # Calcular diferenca 
    data_frame['Diferenca'] =  data_frame['Simulado'] - data_frame['Teorico']
    data_frame['Erro (%0)'] = data_frame['Simulado'] / data_frame['Teorico'] * 100

    return data_frame

def exportar(data_frame):
    try:
        data_frame.to_excel('dataframe.xlxs', index = False)
    except Exception as e:
        print('Erro ao exportar')

def gerar_fila():
    return []

def adicionar_pessoa(fila, tempo_chegada):
    fila.append(tempo_chegada)

def remover_cliente(fila):
    if fila:
        return fila.pop(0)
    return None

def verificar_fila_vazia(fila):
    return len(fila) == 0

def simular_fila_mm1(taxa_de_chegada, taxa_atendimento, tempo_simulacao):
    # Variaveis de controle
    lista_cliente_espera = gerar_fila()
    tempo_simulado = 0
    contador_clientes_atendidos = 0

    # Metricas
    lista_tempo_total_sistema = []
    lista_tempo_total_fila = []

    #Estado servidor
    servidor_ocupado = False
    tempo_liberacao_servidor = 0

    #gerar o tempo
    tempo_proximo_cliente = gerar_intervalos(1/taxa_de_chegada)

    # Loop principal da simulacao
    while tempo_simulado < tempo_simulacao:
        # Determina qual sera o proximo evento
        if servidor_ocupado:
            # Se servidor esta ocupado, proximo evento pode ser chegada OU saída
            tempo_evento = min(tempo_proximo_cliente, tempo_liberacao_servidor)
        else:
            # Se servidor esta livre, so pode acontecer chegada
            tempo_evento = tempo_proximo_cliente

        # Avanca o relogio da simulacao
        tempo_simulado = tempo_evento

        # Verifica se ainda estamos dentro do tempo de simulacao
        if tempo_simulado >= tempo_simulacao:
            break

        # Processa a chegada de um cliente
        if tempo_evento == tempo_proximo_cliente:
            # Cliente chega e entra na fila
            adicionar_pessoa(lista_cliente_espera, tempo_simulado)
            
            # Gera o tempo da proxima chegada
            tempo_proximo_cliente = tempo_simulado + gerar_intervalos(1/taxa_de_chegada)

            # Se o servidor esta livre, atende imediatamente
            if not servidor_ocupado and not verificar_fila_vazia(lista_cliente_espera):
                # Remove da fila e comeca o atendimento
                tempo_chegada_cliente = remover_cliente(lista_cliente_espera)
                if tempo_chegada_cliente is not None:
                    tempo_servico = gerar_intervalos(1/taxa_atendimento)  # Tempo de atendimento aleatorio
                    servidor_ocupado = True
                    tempo_liberacao_servidor = tempo_simulado + tempo_servico

        # Processa a liberacao do servidor (saída de cliente)
        elif tempo_evento == tempo_liberacao_servidor and servidor_ocupado:
            # Cliente terminou o atendimento
            if 'tempo_chegada_cliente' in locals() and tempo_chegada_cliente is not None:
                tempo_espera = tempo_simulado - tempo_chegada_cliente
                lista_tempo_total_fila.append(tempo_espera)
                lista_tempo_total_sistema.append(tempo_espera + tempo_servico)
                contador_clientes_atendidos += 1

            # Se tem alguem na fila, comeca a atender
            if not verificar_fila_vazia(lista_cliente_espera):
                tempo_chegada_cliente = remover_cliente(lista_cliente_espera)
                if tempo_chegada_cliente is not None:
                    tempo_espera_fila = tempo_simulado - tempo_chegada_cliente
                    tempo_servico = gerar_intervalos(1/taxa_atendimento)
                    tempo_liberacao_servidor = tempo_simulado + tempo_servico
            else:
                # Fila esta vazia, servidor fica livre
                servidor_ocupado = False

    # Apos terminar a simulacao, calcula as metricas
    return calcular_metricas_fila(taxa_de_chegada, taxa_atendimento, 
                                 lista_tempo_total_sistema, lista_tempo_total_fila, 
                                 contador_clientes_atendidos)

def calcular_metricas_fila(taxa_de_chegada, taxa_atendimento, 
                          lista_tempo_total_sistema, lista_tempo_total_fila, 
                          contador_clientes_atendidos):
    
    # Utilizacao do servidor: taxa de chegada / taxa de servico
    # Se utilizacao_servidor >= 1, o sistema nunca se estabiliza (chega mais rapido que atende)
    utilizacao_servidor = taxa_de_chegada / taxa_atendimento

    # Metricas simuladas (baseadas nos resultados da simulacao)
    tempo_medio_sistema_simulado = calcular_media(lista_tempo_total_sistema) if lista_tempo_total_sistema else 0
    tempo_medio_fila_simulado = calcular_media(lista_tempo_total_fila) if lista_tempo_total_fila else 0
    numero_medio_sistema_simulado = taxa_de_chegada * tempo_medio_sistema_simulado  # Formula de Little: L = lambda * W
    numero_medio_fila_simulado = taxa_de_chegada * tempo_medio_fila_simulado  # Formula de Little: Lq = lambda * Wq

    # Metricas teoricas (formulas exatas para M/M/1)
    if utilizacao_servidor < 1:
        # Formula da teoria das filas M/M/1
        tempo_medio_sistema_teorico = 1 / (taxa_atendimento - taxa_de_chegada)  # Tempo medio no sistema
        tempo_medio_fila_teorico = taxa_de_chegada / (taxa_atendimento * (taxa_atendimento - taxa_de_chegada))  # Tempo medio na fila
        numero_medio_sistema_teorico = taxa_de_chegada / (taxa_atendimento - taxa_de_chegada)  # Numero medio no sistema
        numero_medio_fila_teorico = (taxa_de_chegada ** 2) / (taxa_atendimento * (taxa_atendimento - taxa_de_chegada))  # Numero medio na fila
    else:
        # Sistema instavel - as filas crescem infinitamente
        tempo_medio_sistema_teorico = tempo_medio_fila_teorico = numero_medio_sistema_teorico = numero_medio_fila_teorico = float('inf')

    # Retorna todas as metricas em um dicionario
    return {
        'utilizacao_servidor': utilizacao_servidor,  # Utilizacao do servidor
        'tempo_medio_sistema_simulado': tempo_medio_sistema_simulado,  # Tempo medio no sistema (simulacao)
        'tempo_medio_sistema_teorico': tempo_medio_sistema_teorico,   # Tempo medio no sistema (teoria)
        'tempo_medio_fila_simulado': tempo_medio_fila_simulado,  # Tempo medio na fila (simulacao)
        'tempo_medio_fila_teorico': tempo_medio_fila_teorico,   # Tempo medio na fila (teoria)
        'numero_medio_sistema_simulado': numero_medio_sistema_simulado,    # Numero medio no sistema (simulacao)
        'numero_medio_sistema_teorico': numero_medio_sistema_teorico,     # Numero medio no sistema (teoria)
        'numero_medio_fila_simulado': numero_medio_fila_simulado,  # Numero medio na fila (simulacao)
        'numero_medio_fila_teorico': numero_medio_fila_teorico,   # Numero medio na fila (teoria)
        'total_clientes_atendidos': contador_clientes_atendidos  # Total de clientes atendidos
    }

# Executar simulacao
print("=== CONFIGURACAO DA SIMULACAO ===")
taxa_chegada = 3  # 3 clientes por unidade de tempo
taxa_atendimento = 5      # 5 clientes atendidos por unidade de tempo
tempo_simulacao_total = 1000  # Tempo total da simulacao

print(f"Taxa de chegada (lambda): {taxa_chegada} clientes/unidade de tempo")
print(f"Taxa de atendimento (mu): {taxa_atendimento} clientes/unidade de tempo")
print(f"Utilizacao (rho = lambda/mu): {taxa_chegada/taxa_atendimento:.2f} ou {(taxa_chegada/taxa_atendimento)*100:.0f}%")
print(f"Tempo de simulacao: {tempo_simulacao_total} unidades de tempo")
print(f"{'='*50}")

# Executa a simulacao
resultados_simulacao = simular_fila_mm1(taxa_chegada, taxa_atendimento, tempo_simulacao_total)

# Exibe os resultados comparando simulacao com teoria
print("\n=== COMPARACAO: SIMULACAO vs TEORIA ===")
print(f"p (Utilizacao): {resultados_simulacao['utilizacao_servidor']:.4f}")
print(f"\nTempo Medio no Sistema (W):")
print(f"  Simulado: {resultados_simulacao['tempo_medio_sistema_simulado']:.4f}")
print(f"  Teorico:  {resultados_simulacao['tempo_medio_sistema_teorico']:.4f}")
print(f"\nTempo Medio na Fila (Wq):")
print(f"  Simulado: {resultados_simulacao['tempo_medio_fila_simulado']:.4f}")
print(f"  Teorico:  {resultados_simulacao['tempo_medio_fila_teorico']:.4f}")
print(f"\nNumero Medio no Sistema (L):")
print(f"  Simulado: {resultados_simulacao['numero_medio_sistema_simulado']:.4f}")
print(f"  Teorico:  {resultados_simulacao['numero_medio_sistema_teorico']:.4f}")

# Cria DataFrame com comparacao de resultados
data_frame_comparacao = comparador_matematico(resultados_simulacao)
print("\nDataFrame com resultados detalhados:")
print(data_frame_comparacao.to_string(index=False))

# Cria DataFrame resumido
data_frame_resumo = gerar_dataframe(resultados_simulacao)
print("\nDataFrame resumido:")
print(data_frame_resumo)

# Exporta resultados
exportar(data_frame_comparacao)
