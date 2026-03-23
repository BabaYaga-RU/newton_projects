"""
Teoria das Filas - Simulação de Sistemas Computacionais

Este código simula sistemas de filas de forma simples, sem usar programação orientada a objetos.
Muito usado em:
- Bancos (caixas de atendimento)
- Supermercados (caixas)
- Call centers (atendentes)
- Sistemas computacionais (processos esperando CPU)

=== NOTAÇÃO DE KENDALL ===
A notação padronizada para descrever sistemas de filas tem o formato: A/B/c[/K/m/Z]

Onde:
- A: Distribuição dos tempos entre chegadas
- B: Distribuição dos tempos de serviço  
- c: Número de servidores
- K: Capacidade máxima do sistema (opcional)
- m: Tamanho da população (opcional)
- Z: Disciplina da fila (opcional, padrão FIFO)

Símbolos comuns:
- M: Distribuição Markoviana (Exponencial) - memória curta
- D: Distribuição Determinística (tempos constantes)
- G: Distribuição Geral (qualquer distribuição)
- Ek: Distribuição Erlang-k (k fases exponenciais)

Exemplos:
- M/M/1: Chegadas exponenciais, serviços exponenciais, 1 servidor
- M/D/3: Chegadas exponenciais, serviços determinísticos, 3 servidores
- M/G/2/10: Chegadas exponenciais, serviços gerais, 2 servidores, capacidade máxima 10

O "M/M/1" que simulamos significa:
- Primeiro M: Chegada de clientes segue distribuição Markoviana (exponencial)
- Segundo M: Tempo de serviço segue distribuição Markoviana (exponencial)  
- 1: Tem apenas 1 servidor (caixa, atendente, etc.)

Este código foi implementado usando lógica de programação manual, sem depender
de funções prontas de bibliotecas como numpy, para melhor entendimento dos conceitos.
"""

# Importa bibliotecas necessárias
import random               # Para geração de números aleatórios
import math                 # Para funções matemáticas básicas
import matplotlib.pyplot as plt  # Para criar gráficos

def gerar_tempo_exponencial(tempo_medio):
    """
    Gera um tempo aleatório seguindo distribuição exponencial
    
    Conceito matemático:
    - A distribuição exponencial modela tempos entre eventos
    - Fórmula: X = -ln(U) / λ, onde U é uniforme entre 0 e 1
    - λ (lambda) é a taxa - quantos eventos acontecem por unidade de tempo
    - Média = 1/λ, então λ = 1/média
    
    Por que usamos isso?
    - Em filas, tempos entre chegadas de clientes geralmente seguem distribuição exponencial
    - Isso modela o comportamento real de sistemas de filas
    """
    if tempo_medio <= 0:
        return 0
    
    # Gera número aleatório entre 0 e 1
    numero_aleatorio = random.random()
    
    # Evita log(0) que daria erro
    if numero_aleatorio == 0:
        numero_aleatorio = 0.0001
    
    # Fórmula da transformada inversa para distribuição exponencial
    # X = -ln(U) / λ
    # Onde:
    # - U é um número aleatório uniforme entre 0 e 1
    # - λ (lambda) é a taxa de eventos (1/tempo_medio)
    # - X é o tempo gerado seguindo distribuição exponencial
    taxa_eventos = 1.0 / tempo_medio
    return -math.log(numero_aleatorio) / taxa_eventos

def calcular_media_lista(lista_numeros):
    """
    Calcula a média de uma lista manualmente
    
    Conceito:
    - Média = soma de todos os valores / quantidade de valores
    - Implementamos manualmente para não depender de numpy.mean()
    """
    if not lista_numeros:
        return 0
    
    soma_total = 0
    for valor in lista_numeros:
        soma_total += valor
    
    quantidade_valores = len(lista_numeros)
    return soma_total / quantidade_valores

def criar_fila():
    """
    Cria uma fila vazia usando lista
    
    Conceitos:
    - FIFO (First In, First Out): O primeiro que chega é o primeiro a sair
    - append(): Adiciona no final da fila
    - pop(0): Remove do início da fila
    """
    return []

def adicionar_cliente_fila(fila, tempo_chegada):
    """
    Adiciona cliente no final da fila
    """
    fila.append(tempo_chegada)

def remover_cliente_fila(fila):
    """
    Remove cliente do início da fila e retorna o tempo de chegada
    """
    if fila:
        return fila.pop(0)
    return None

def verificar_fila_vazia(fila):
    """
    Verifica se a fila está vazia
    """
    return len(fila) == 0

def simular_fila_mm1(taxa_chegada_clientes, taxa_atendimento_servidor, tempo_simulacao):
    """
    Simula uma fila M/M/1 passo-a-passo
    
    Conceitos importantes:
    - taxa_chegada_clientes: Quantos clientes chegam por unidade de tempo (ex: 3 clientes/min)
    - taxa_atendimento_servidor: Quantos clientes o servidor consegue atender por unidade de tempo (ex: 5 clientes/min)
    - tempo_simulacao: Por quanto tempo vamos observar a fila
    - utilizacao_servidor: taxa_chegada_clientes / taxa_atendimento_servidor - mostra o quão ocupado o servidor está
    """
    
    # Variáveis de controle da simulação
    lista_clientes_espera = criar_fila()       # Fila de espera (clientes aguardando)
    tempo_simulacao_atual = 0                  # Relógio da simulação
    contador_clientes_atendidos = 0            # Contador de clientes atendidos
    
    # Métricas que vamos calcular
    lista_tempos_total_sistema = []            # Tempo que cada cliente ficou no sistema (fila + atendimento)
    lista_tempos_total_fila = []               # Tempo que cada cliente ficou na fila (só esperando)
    
    # Estado do servidor
    servidor_ocupado = False                   # True se está atendendo, False se livre
    tempo_liberacao_servidor = 0               # Em que instante o servidor ficará livre

    # Gera o tempo da primeira chegada usando distribuição exponencial
    tempo_proximo_cliente = gerar_tempo_exponencial(1/taxa_chegada_clientes)

    # Loop principal da simulação
    while tempo_simulacao_atual < tempo_simulacao:
        # Determina qual será o próximo evento
        if servidor_ocupado:
            # Se servidor está ocupado, próximo evento pode ser chegada OU saída
            tempo_evento = min(tempo_proximo_cliente, tempo_liberacao_servidor)
        else:
            # Se servidor está livre, só pode acontecer chegada
            tempo_evento = tempo_proximo_cliente

        # Avança o relógio da simulação
        tempo_simulacao_atual = tempo_evento

        # Verifica se ainda estamos dentro do tempo de simulação
        if tempo_simulacao_atual >= tempo_simulacao:
            break

        # Processa a chegada de um cliente
        if tempo_evento == tempo_proximo_cliente:
            # Cliente chega e entra na fila
            adicionar_cliente_fila(lista_clientes_espera, tempo_simulacao_atual)
            
            # Gera o tempo da próxima chegada
            tempo_proximo_cliente = tempo_simulacao_atual + gerar_tempo_exponencial(1/taxa_chegada_clientes)

            # Se o servidor está livre, atende imediatamente
            if not servidor_ocupado:
                # Remove da fila e começa o atendimento
                tempo_chegada_cliente = remover_cliente_fila(lista_clientes_espera)
                tempo_servico = gerar_tempo_exponencial(1/taxa_atendimento_servidor)  # Tempo de atendimento aleatório
                servidor_ocupado = True
                tempo_liberacao_servidor = tempo_simulacao_atual + tempo_servico

        # Processa a liberação do servidor (saída de cliente)
        elif tempo_evento == tempo_liberacao_servidor:
            # Cliente terminou o atendimento
            tempo_espera = tempo_simulacao_atual - tempo_chegada_cliente
            lista_tempos_total_fila.append(tempo_espera)
            lista_tempos_total_sistema.append(tempo_espera + tempo_servico)
            contador_clientes_atendidos += 1

            # Se tem alguém na fila, começa a atender
            if not verificar_fila_vazia(lista_clientes_espera):
                tempo_chegada_cliente = remover_cliente_fila(lista_clientes_espera)
                tempo_espera_fila = tempo_simulacao_atual - tempo_chegada_cliente
                tempo_servico = gerar_tempo_exponencial(1/taxa_atendimento_servidor)
                tempo_liberacao_servidor = tempo_simulacao_atual + tempo_servico
            else:
                # Fila está vazia, servidor fica livre
                servidor_ocupado = False

    # Após terminar a simulação, calcula as métricas
    return calcular_metricas_fila(taxa_chegada_clientes, taxa_atendimento_servidor, 
                                 lista_tempos_total_sistema, lista_tempos_total_fila, 
                                 contador_clientes_atendidos)

def calcular_metricas_fila(taxa_chegada_clientes, taxa_atendimento_servidor, 
                          lista_tempos_total_sistema, lista_tempos_total_fila, 
                          contador_clientes_atendidos):
    """
    Calcula as métricas da fila usando fórmulas da teoria das filas
    
    Principais métricas:
    - utilizacao_servidor: taxa_chegada_clientes / taxa_atendimento_servidor. Deve ser < 1 para o sistema ser estável
    - tempo_medio_sistema: Tempo médio que um cliente passa no sistema (fila + atendimento)
    - tempo_medio_fila: Tempo médio que um cliente passa na fila (só esperando)
    - numero_medio_sistema: Número médio de clientes no sistema
    - numero_medio_fila: Número médio de clientes na fila
    """
    
    # Utilização do servidor: taxa de chegada / taxa de serviço
    # Se utilizacao_servidor >= 1, o sistema nunca se estabiliza (chega mais rápido que atende)
    utilizacao_servidor = taxa_chegada_clientes / taxa_atendimento_servidor

    # Métricas simuladas (baseadas nos resultados da simulação)
    # Usamos nossa função manual de cálculo de média em vez de numpy.mean()
    tempo_medio_sistema_simulado = calcular_media_lista(lista_tempos_total_sistema) if lista_tempos_total_sistema else 0
    tempo_medio_fila_simulado = calcular_media_lista(lista_tempos_total_fila) if lista_tempos_total_fila else 0
    numero_medio_sistema_simulado = taxa_chegada_clientes * tempo_medio_sistema_simulado  # Fórmula de Little: L = lambda * W
    numero_medio_fila_simulado = taxa_chegada_clientes * tempo_medio_fila_simulado  # Fórmula de Little: Lq = lambda * Wq

    # Métricas teóricas (fórmulas exatas para M/M/1)
    if utilizacao_servidor < 1:
        # Fórmulas clássicas da teoria das filas M/M/1
        tempo_medio_sistema_teorico = 1 / (taxa_atendimento_servidor - taxa_chegada_clientes)  # Tempo médio no sistema
        tempo_medio_fila_teorico = taxa_chegada_clientes / (taxa_atendimento_servidor * (taxa_atendimento_servidor - taxa_chegada_clientes))  # Tempo médio na fila
        numero_medio_sistema_teorico = taxa_chegada_clientes / (taxa_atendimento_servidor - taxa_chegada_clientes)  # Número médio no sistema
        numero_medio_fila_teorico = (taxa_chegada_clientes ** 2) / (taxa_atendimento_servidor * (taxa_atendimento_servidor - taxa_chegada_clientes))  # Número médio na fila
    else:
        # Sistema instável - as filas crescem infinitamente
        tempo_medio_sistema_teorico = tempo_medio_fila_teorico = numero_medio_sistema_teorico = numero_medio_fila_teorico = float('inf')

    # Retorna todas as métricas em um dicionário
    return {
        'utilizacao_servidor': utilizacao_servidor,  # Utilização do servidor
        'tempo_medio_sistema_simulado': tempo_medio_sistema_simulado,  # Tempo médio no sistema (simulação)
        'tempo_medio_sistema_teorico': tempo_medio_sistema_teorico,   # Tempo médio no sistema (teoria)
        'tempo_medio_fila_simulado': tempo_medio_fila_simulado,  # Tempo médio na fila (simulação)
        'tempo_medio_fila_teorico': tempo_medio_fila_teorico,   # Tempo médio na fila (teoria)
        'numero_medio_sistema_simulado': numero_medio_sistema_simulado,    # Número médio no sistema (simulação)
        'numero_medio_sistema_teorico': numero_medio_sistema_teorico,     # Número médio no sistema (teoria)
        'numero_medio_fila_simulado': numero_medio_fila_simulado,  # Número médio na fila (simulação)
        'numero_medio_fila_teorico': numero_medio_fila_teorico,   # Número médio na fila (teoria)
        'total_clientes_atendidos': contador_clientes_atendidos  # Total de clientes atendidos
    }

# Executar simulação
print("=== CONFIGURACAO DA SIMULACAO ===")
taxa_chegada = 3  # 3 clientes por unidade de tempo
taxa_atendimento = 5      # 5 clientes atendidos por unidade de tempo
tempo_simulacao_total = 1000  # Tempo total da simulação

# Usando símbolos Unicode com tratamento de codificação
try:
    print(f"Taxa de chegada (λ): {taxa_chegada} clientes/unidade de tempo")
    print(f"Taxa de atendimento (μ): {taxa_atendimento} clientes/unidade de tempo")
    print(f"Utilizacao (ρ = λ/μ): {taxa_chegada/taxa_atendimento:.2f} ou {(taxa_chegada/taxa_atendimento)*100:.0f}%")
except UnicodeEncodeError:
    # Fallback para versão sem símbolos caso haja erro de codificação
    print(f"Taxa de chegada (lambda): {taxa_chegada} clientes/unidade de tempo")
    print(f"Taxa de atendimento (mu): {taxa_atendimento} clientes/unidade de tempo")
    print(f"Utilizacao (rho = lambda/mu): {taxa_chegada/taxa_atendimento:.2f} ou {(taxa_chegada/taxa_atendimento)*100:.0f}%")

print(f"Tempo de simulacao: {tempo_simulacao_total} unidades de tempo")
print(f"{'='*50}")

# Executa a simulação
resultados_simulacao = simular_fila_mm1(taxa_chegada, taxa_atendimento, tempo_simulacao_total)

# Exibe os resultados comparando simulação com teoria
print("\n=== COMPARACAO: SIMULACAO vs TEORIA ===")

# Tratamento de símbolos Unicode para a saída de resultados
try:
    print(f"ρ (Utilização): {resultados_simulacao['utilizacao_servidor']:.4f}")
    print(f"\nTempo Médio no Sistema (W):")
    print(f"  Simulado: {resultados_simulacao['tempo_medio_sistema_simulado']:.4f}")
    print(f"  Teórico:  {resultados_simulacao['tempo_medio_sistema_teorico']:.4f}")
    print(f"\nTempo Médio na Fila (Wq):")
    print(f"  Simulado: {resultados_simulacao['tempo_medio_fila_simulado']:.4f}")
    print(f"  Teórico:  {resultados_simulacao['tempo_medio_fila_teorico']:.4f}")
    print(f"\nNúmero Médio no Sistema (L):")
    print(f"  Simulado: {resultados_simulacao['numero_medio_sistema_simulado']:.4f}")
    print(f"  Teórico:  {resultados_simulacao['numero_medio_sistema_teorico']:.4f}")
except UnicodeEncodeError:
    # Fallback para versão sem símbolos caso haja erro de codificação
    print(f"rho (Utilizacao): {resultados_simulacao['utilizacao_servidor']:.4f}")
    print(f"\nTempo Medio no Sistema (W):")
    print(f"  Simulado: {resultados_simulacao['tempo_medio_sistema_simulado']:.4f}")
    print(f"  Teorico:  {resultados_simulacao['tempo_medio_sistema_teorico']:.4f}")
    print(f"\nTempo Medio na Fila (Wq):")
    print(f"  Simulado: {resultados_simulacao['tempo_medio_fila_simulado']:.4f}")
    print(f"  Teorico:  {resultados_simulacao['tempo_medio_fila_teorico']:.4f}")
    print(f"\nNumero Medio no Sistema (L):")
    print(f"  Simulado: {resultados_simulacao['numero_medio_sistema_simulado']:.4f}")
    print(f"  Teorico:  {resultados_simulacao['numero_medio_sistema_teorico']:.4f}")

# Simulação simplificada sem simpy (para funcionar sem dependências externas)
print("\n=== SIMULAÇÃO SIMPLIFICADA (sem simpy) ===")
print("Esta é uma versão mais simples da simulação, sem usar distribuições exponenciais")
print("Tempo de simulação: 60 minutos")
print("Intervalo médio entre chegadas: 5 minutos")
print("Tempo de atendimento: 3-7 minutos (aleatório)")

# Simulação básica - versão simplificada
import random

tempo_total = 60
tempo_entre_chegadas = 5
tempo_atendimento_min = 3
tempo_atendimento_max = 7

print("\nIniciando simulação simplificada...")
tempo_atual = 0
clientes_atendidos = 0
proxima_chegada = random.expovariate(1/tempo_entre_chegadas)

while tempo_atual < tempo_total:
    if tempo_atual >= proxima_chegada:
        # Chegada de cliente
        tempo_servico = random.randint(tempo_atendimento_min, tempo_atendimento_max)
        print(f"Tempo {tempo_atual:.1f} min: Cliente {clientes_atendidos + 1} chegou, tempo de atendimento: {tempo_servico} min")
        
        # Simula o atendimento
        tempo_atual += tempo_servico
        clientes_atendidos += 1
        proxima_chegada = tempo_atual + random.expovariate(1/tempo_entre_chegadas)
    else:
        tempo_atual += 1

print(f"\nSimulação simplificada concluída!")
print(f"Clientes atendidos: {clientes_atendidos}")
print(f"\nDiferença entre as simulações:")
print(f"- Simulação 1 (M/M/1): Usa distribuições exponenciais, mais realista")
print(f"- Simulação 2 (Simplificada): Usa tempos fixos, mais fácil de entender")

# Gráficos de exemplo (agora descomentados para exibir os gráficos)

print("\n=== EXEMPLOS DE GRÁFICOS ===")
print("Os gráficos abaixo mostram como visualizar os resultados da simulação")

# Gráfico de Tempo de Atendimento
print("\n1. Gráfico de Tempo de Atendimento por Cliente:")
print("   Mostra quanto tempo cada cliente levou para ser atendido")
tempos_atendimento = [4, 6, 5, 7, 3, 6, 4] # exemplo de tempos de atendimento
print(f"   Tempos: {tempos_atendimento} minutos")
print("   Este gráfico ajudaria a identificar clientes que demoraram mais")

# Cria o gráfico de tempo de atendimento
plt.figure(figsize=(10, 5))
plt.plot(range(1, len(tempos_atendimento)+1), tempos_atendimento, marker='o', linestyle='-')
plt.title('Tempo de Atendimento por Cliente')
plt.xlabel('Cliente')
plt.ylabel('Tempo (minutos)')
plt.grid(True)
plt.show()

# Gráfico de Tempo de Espera
print("\n2. Gráfico de Tempo de Espera por Cliente:")
print("   Mostra quanto tempo cada cliente esperou na fila")
tempos_espera = [2, 5, 1, 3, 4, 2, 0] # exemplo de tempos de espera
print(f"   Tempos: {tempos_espera} minutos")
print("   Este gráfico ajuda a identificar períodos de maior espera")

# Cria o gráfico de tempo de espera
plt.figure(figsize=(10, 5))
plt.bar(range(1, len(tempos_espera)+1), tempos_espera, color='orange')
plt.title('Tempo de Espera por Cliente')
plt.xlabel('Cliente')
plt.ylabel('Tempo de Espera (minutos)')
plt.show()

# Gráfico de Clientes Atendidos ao Longo do Tempo
print("\n3. Gráfico de Clientes Atendidos ao Longo do Tempo:")
print("   Mostra a evolução do número de clientes atendidos")
tempos_chegada = [2, 7, 12, 18, 25, 32, 40] # exemplo de tempos de chegada
clientes_atendidos = list(range(1, len(tempos_chegada)+1))
print(f"   Clientes atendidos: {clientes_atendidos}")
print(f"   Tempos: {tempos_chegada} minutos")
print("   Este gráfico mostra a taxa de atendimento ao longo do tempo")

# Cria o gráfico de clientes atendidos ao longo do tempo
plt.figure(figsize=(10, 5))
plt.step(tempos_chegada, clientes_atendidos, where='post')
plt.title('Clientes Atendidos ao Longo do Tempo')
plt.xlabel('Tempo (minutos)')
plt.ylabel('Número de Clientes')
plt.grid(True)
plt.show()

print("\nGráficos exibidos com sucesso!")