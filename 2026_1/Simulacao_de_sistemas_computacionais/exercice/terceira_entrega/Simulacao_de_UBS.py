import simpy
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

MINUTO_HORA = 60
MINUTO_DIA = 24 * MINUTO_HORA
DIAS_SIMULACAO = 14
REPLICACOES = 30

def obter_capacidade(tempo_atual, parametros):
    dia = int(tempo_atual // MINUTO_DIA)
    dia_semana = dia % 7
    minuto_dia = tempo_atual % MINUTO_DIA
    if dia_semana < 5:
        if (7 * MINUTO_HORA <= minuto_dia) and (minuto_dia < 13 * MINUTO_HORA):
            return parametros['odonto_manha'], parametros['mulher_manha']
        
        elif (13 * MINUTO_HORA <= minuto_dia) and (minuto_dia < 17 * MINUTO_HORA):
            return parametros['odonto_tarde'], parametros['mulher_tarde']
    
    elif dia_semana == 5:
        if (8 * MINUTO_HORA <= minuto_dia) and (minuto_dia < 14 * MINUTO_HORA):
            return parametros['odonto_sab'], parametros['mulher_sab']
    
    return 0, 0

class UBSMutirao:
    
    def __init__(self, ambiente, parametros):
        self.ambiente = ambiente
        self.parametros = parametros
        
        # Cada item no Store representa um profissional livre para atender
        self.servidores_odonto = simpy.Store(ambiente)
        self.servidores_mulher = simpy.Store(ambiente)
        
        # Rastreia quantos servidores estão atualmente disponíveis
        # Usado para calcular quantos adicionar/remover quando o turno muda
        self.current_cap_odonto = 0
        self.current_cap_mulher = 0
        
        # Lista que armazena dados de todos os pacientes atendidos
        # Cada elemento é um dicionário com: {'fluxo': tipo, 'espera': tempo_espera}
        # ou {'fluxo': tipo, 'evento': 'bloqueio', 'tempo': momento}
        self.dados = []
        
        # Inicia o processo de atualização dinâmica de capacidade
        # Este processo roda em paralelo com o resto da simulação
        self.ambiente.process(self.atualizar_recursos())

    def atualizar_recursos(self):
        """
        1. Consulta obter_capacidade() para saber quantos profissionais deveriam estar trabalhando
        2. Compara com a capacidade atual
        3. Adiciona tokens ao Store se precisar de mais profissionais
        4. Remove tokens do Store se precisar de menos profissionais
        """
        while True:
            cap_odonto, cap_mulher = obter_capacidade(self.ambiente.now, self.parametros)

            
            # Se precisa de MAIS dentistas do que tem atualmente
            if cap_odonto > self.current_cap_odonto:
                # Adiciona novos tokens (profissionais) ao Store
                for _ in range(cap_odonto - self.current_cap_odonto):
                    yield self.servidores_odonto.put(object())
            
            # Se precisa de MENOS dentistas do que tem atualmente
            elif cap_odonto < self.current_cap_odonto:
                # Remove tokens (profissionais) do Store
                # Só remove se houver tokens disponíveis (profissionais ociosos)
                for _ in range(self.current_cap_odonto - cap_odonto):
                    if self.servidores_odonto.items:  # Verifica se há tokens no Store
                        yield self.servidores_odonto.get()
            
            # Atualiza o rastreador de capacidade
            self.current_cap_odonto = cap_odonto

            if cap_mulher > self.current_cap_mulher:
                for _ in range(cap_mulher - self.current_cap_mulher):
                    yield self.servidores_mulher.put(object())
            elif cap_mulher < self.current_cap_mulher:
                for _ in range(self.current_cap_mulher - cap_mulher):
                    if self.servidores_mulher.items:
                        yield self.servidores_mulher.get()
            
            self.current_cap_mulher = cap_mulher

            yield self.ambiente.timeout(1)

def processo_paciente(ambiente, ubs, fluxo):
    """
    Processo que modela a jornada de um único paciente na UBS.
    
    Fluxo do paciente:
    1. Chega na UBS
    2. Verifica se há vaga no sistema (fila + atendimento)
    3. Se houver vaga: espera por um profissional, é atendido e libera o profissional
    4. Se não houver vaga: vai embora (bloqueio)
    
    Parâmetros:
    -----------
    ambiente : simpy.Environment
        Ambiente de simulação
    ubs : UBSMutirao
        Referência à UBS para acessar servidores e registrar dados
    fluxo : str
        Tipo de atendimento: 'odonto' ou 'mulher'
    """
    
    # Registra o momento exato da chegada do paciente
    chegada = ambiente.now

    # Seleciona qual conjunto de servidores usar baseado no tipo de atendimento
    servidores = ubs.servidores_odonto if fluxo == 'odonto' else ubs.servidores_mulher
    
    # Obtém a capacidade atual (quantos profissionais estão trabalhando agora)
    current_capacity = ubs.current_cap_odonto if fluxo == 'odonto' else ubs.current_cap_mulher

    # ========== PARÂMETROS DE FILA E ATENDIMENTO ==========
    
    # Capacidade máxima do sistema (fila + sendo atendido)
    # Por que esses valores?
    # - Odonto: 36 = 3 profissionais × 12 pacientes por profissional (margem de segurança)
    # - Mulher: 40 = 4 profissionais × 10 pacientes por profissional (margem de segurança)
    capacidade_fila = 36 if fluxo == 'odonto' else 40
    
    # Tempo médio de atendimento em minutos
    # Por que esses valores?
    # - Odonto: 20 minutos (consulta odontológica básica)
    # - Mulher: 25 minutos (consulta ginecológica/obstétrica mais detalhada)
    tempo_servico = 20 if fluxo == 'odonto' else 25

    # ========== CÁLCULO DE PACIENTES NO SISTEMA ==========
    
    # Calcula quantos pacientes estão atualmente no sistema:
    # 1. len(servidores.get_queue) = pacientes esperando na fila por um profissional
    # 2. (current_capacity - len(servidores.items)) = profissionais ocupados no momento
    #    (capacidade total menos profissionais livres = profissionais ocupados)
    patients_in_system = len(servidores.get_queue) + (current_capacity - len(servidores.items))

    # ========== DECISÃO: ENTRAR OU IR EMBORA? ==========
    
    if patients_in_system < capacidade_fila:
        # HÁ VAGA: paciente entra no sistema
        
        # Solicita um token (profissional) do Store
        # Se não houver tokens disponíveis, o processo fica em espera nesta linha
        # até que um profissional termine outro atendimento e devolva o token
        token = yield servidores.get()
        
        # Calcula quanto tempo o paciente esperou na fila
        # (tempo atual - tempo de chegada = tempo de espera)
        espera = ambiente.now - chegada
        
        # Registra os dados do atendimento para análise posterior
        ubs.dados.append({'fluxo': fluxo, 'espera': espera})
        
        # Simula o tempo de atendimento
        # Durante este período, o profissional está ocupado com este paciente
        yield ambiente.timeout(tempo_servico)
        
        # Libera o profissional (devolve o token ao Store)
        # Outro paciente em espera poderá pegar este token agora
        yield servidores.put(token)
    else:
        # NÃO HÁ VAGA: sistema lotado, paciente vai embora (bloqueio)
        # Registra que houve um paciente que não conseguiu entrar no sistema
        ubs.dados.append({'fluxo': fluxo, 'evento': 'bloqueio', 'tempo': ambiente.now})

# =============================================================================
# PROCESSO: GERADOR DE CHEGADAS DE PACIENTES
# =============================================================================

def gerador_chegadas(ambiente, ubs, fluxo, taxa_hora):
    """
    Processo que gera chegadas de pacientes ao longo do tempo.
    
    Modelo de chegadas: Processo de Poisson
    - As chegadas são aleatórias mas com taxa média constante
    - O tempo entre chegadas segue distribuição exponencial
    - Por que exponencial? Modelo padrão para chegadas aleatórias em filas
    
    Parâmetros:
    -----------
    ambiente : simpy.Environment
        Ambiente de simulação
    ubs : UBSMutirao
        Referência à UBS
    fluxo : str
        Tipo de atendimento: 'odonto' ou 'mulher'
    taxa_hora : float
        Número médio de pacientes por hora (ex: 6 = 6 pacientes/hora em média)
    """
    
    # Converte taxa de pacientes/hora para pacientes/minuto
    # Por que? A simulação trabalha em minutos como unidade de tempo
    taxa_minuto = taxa_hora / 60.0
    
    # Loop infinito: gera pacientes continuamente durante toda a simulação
    while True:
        # Gera tempo até próxima chegada usando distribuição exponencial
        # random.expovariate(lambda) gera valor aleatório onde:
        # - lambda = taxa de ocorrência (pacientes por minuto)
        # - Valor esperado (média) = 1/lambda minutos entre chegadas
        # Exemplo: taxa_hora=6 → taxa_minuto=0.1 → média de 10 minutos entre chegadas
        yield ambiente.timeout(random.expovariate(taxa_minuto))
        
        # Cria um novo processo para atender este paciente
        ambiente.process(processo_paciente(ambiente, ubs, fluxo))

# =============================================================================
# FUNÇÃO: EXECUTAR UMA REPLICACÃO DA SIMULAÇÃO
# =============================================================================

def executar_replicacao(parametros, semente):
    """
    Executa uma única replicação (rodada) da simulação.
    
    Cada replicação:
    1. Configura ambiente e semente aleatória
    2. Cria a UBS com capacidade dinâmica
    3. Inicia geradores de chegadas para ambos os fluxos
    4. Executa simulação por 14 dias
    5. Retorna dados coletados em DataFrame
    
    Por que múltiplas replicações?
    - Cada replicação usa semente diferente → resultados ligeiramente diferentes
    - Média de várias replicações → resultado estatisticamente confiável
    - Permite calcular intervalos de confiança e variabilidade
    
    Parâmetros:
    -----------
    parametros : dict
        Configurações de capacidade de profissionais
    semente : int
        Semente para gerador de números aleatórios (reprodutibilidade)
    
    Retorna:
    --------
    pd.DataFrame
        Dados de todos os pacientes com colunas: 'fluxo', 'espera' (ou 'evento')
    """
    
    # Configura semente aleatória para reprodutibilidade
    # Mesma semente → mesma sequência de números aleatórios → resultados idênticos
    random.seed(semente)
    
    # Cria ambiente de simulação SimPy
    ambiente = simpy.Environment()
    
    # Cria a UBS com parâmetros de capacidade
    ubs = UBSMutirao(ambiente, parametros)
    
    # Inicia processo de chegadas para atendimento odontológico
    # Taxa: 6 pacientes por hora em média (um a cada 10 minutos em média)
    ambiente.process(gerador_chegadas(ambiente, ubs, 'odonto', 6))
    
    # Inicia processo de chegadas para atendimento da mulher
    # Taxa: 8 pacientes por hora em média (um a cada 7.5 minutos em média)
    ambiente.process(gerador_chegadas(ambiente, ubs, 'mulher', 8))
    
    # Executa a simulação por 14 dias (em minutos)
    ambiente.run(until=DIAS_SIMULACAO * MINUTO_DIA)
    
    # Converte dados coletados em DataFrame pandas para análise
    return pd.DataFrame(ubs.dados)

# =============================================================================
# EXECUÇÃO DOS CENÁRIOS DE SIMULAÇÃO
# =============================================================================

# ========== CENÁRIO 1: MUTIRÃO (PROFISSIONAIS CONTRATADOS + SÁBADO) ==========

# Configuração do mutirão: mais profissionais e atendimento aos sábados
parametros_mutirao = {
    'odonto_manha': 3,   # 3 dentistas no turno da manhã (seg-sex)
    'odonto_tarde': 3,   # 3 dentistas no turno da tarde (seg-sex)
    'odonto_sab': 3,     # 3 dentistas aos sábados
    'mulher_manha': 4,   # 4 médicos da mulher no turno da manhã (seg-sex)
    'mulher_tarde': 4,   # 4 médicos da mulher no turno da tarde (seg-sex)
    'mulher_sab': 4      # 4 médicos da mulher aos sábados
}

# Executa 30 replicações do cenário de mutirão
# Cada replicação gera um DataFrame com dados de todos os pacientes
resultados = [executar_replicacao(parametros_mutirao, s) for s in range(REPLICACOES)]

# Combina todos os DataFrames em um único DataFrame grande
# pd.concat empilha os DataFrames verticalmente
df_final = pd.concat(resultados)

# Calcula tempo médio de espera por tipo de atendimento
# groupby('fluxo') agrupa por 'odonto' e 'mulher'
# ['espera'].mean() calcula a média do tempo de espera em cada grupo
print(df_final.groupby('fluxo')['espera'].mean())

# =============================================================================
# CENÁRIO 2: ANTES DO MUTIRÃO (APENAS CONCURSADOS)
# =============================================================================

# Configuração atual: apenas profissionais concursados, sem sábado
parametros_atual = {
    'odonto_manha': 1,   # 1 dentista concursado no turno da manhã
    'odonto_tarde': 1,   # 1 dentista concursado no turno da tarde
    'odonto_sab': 0,     # Nenhum dentista aos sábados (UBS fechada)
    'mulher_manha': 1,   # 1 médico concursado no turno da manhã
    'mulher_tarde': 1,   # 1 médico concursado no turno da tarde
    'mulher_sab': 0      # Nenhum médico aos sábados (UBS fechada)
}

# Executa 30 replicações do cenário atual (antes do mutirão)
resultados_atual = [executar_replicacao(parametros_atual, s) for s in range(REPLICACOES)]
df_atual = pd.concat(resultados_atual)

# Executa 30 replicações do cenário de mutirão para comparação
resultados_mutirao = [executar_replicacao(parametros_mutirao, s) for s in range(REPLICACOES)]
df_mutirao = pd.concat(resultados_mutirao)

# =============================================================================
# ANÁLISE GRÁFICA COMPARATIVA
# =============================================================================

# Adiciona coluna 'dia' para identificar qual day da simulação cada atendimento ocorreu
# (índice // MINUTO_DIA) calcula quantos dias completos se passaram
df_atual['dia'] = (df_atual.index // MINUTO_DIA).astype(int)
df_mutirao['dia'] = (df_mutirao.index // MINUTO_DIA).astype(int)

# Conta número de atendimentos por dia e por tipo de fluxo
# groupby(['dia', 'fluxo']) agrupa por dia e tipo de atendimento
# .size() conta quantos atendimentos em cada grupo
# .unstack(fill_value=0) transforma em tabela com dias nas linhas e fluxos nas colunas
atend_atual = df_atual.groupby(['dia', 'fluxo']).size().unstack(fill_value=0)
atend_mutirao = df_mutirao.groupby(['dia', 'fluxo']).size().unstack(fill_value=0)

# ========== CRIAÇÃO DO GRÁFICO COMPARATIVO ==========

plt.figure(figsize=(10, 6))  # Tamanho da figura: 10x6 polegadas

# Plota atendimentos de odontologia - cenário atual (apenas concursados)
plt.plot(atend_atual.index, atend_atual['odonto'], 
         label='Odonto - Antes', color='blue', linestyle='-', marker='o')

# Plota atendimentos de odontologia - cenário mutirão
plt.plot(atend_mutirao.index, atend_mutirao['odonto'], 
         label='Odonto - Mutirão', color='green', linestyle='--', marker='s')

# Plota atendimentos da mulher - cenário atual
plt.plot(atend_atual.index, atend_atual['mulher'], 
         label='Mulher - Antes', color='red', linestyle='-', marker='^')

# Plota atendimentos da mulher - cenário mutirão
plt.plot(atend_mutirao.index, atend_mutirao['mulher'], 
         label='Mulher - Mutirão', color='purple', linestyle='--', marker='d')

# Configurações do gráfico
plt.xlabel("Dias da Simulação", fontsize=12)           # Rótulo do eixo X
plt.ylabel("Número de Atendimentos", fontsize=12)      # Rótulo do eixo Y
plt.title("Comparação de Atendimentos - Antes e Depois do Mutirão", fontsize=14, fontweight='bold')
plt.legend(loc='best', fontsize=10)                    # Legenda automática na melhor posição
plt.grid(True, alpha=0.3)                              # Grade de fundo com transparência

# Exibe o gráfico
plt.show()

# =============================================================================
# ANÁLISE ESTATÍSTICA ADICIONAL
# =============================================================================

# Calcula estatísticas descritivas por cenário e fluxo
print("\n=== ESTATÍSTICAS DO CENÁRIO ATUAL (ANTES) ===")
print(df_atual.groupby('fluxo')['espera'].describe())

print("\n=== ESTATÍSTICAS DO CENÁRIO MUTIRÃO (DEPOIS) ===")
print(df_mutirao.groupby('fluxo')['espera'].describe())

# Calcula redução percentual no tempo médio de espera
media_espera_atual = df_atual.groupby('fluxo')['espera'].mean()
media_espera_mutirao = df_mutirao.groupby('fluxo')['espera'].mean()

print("\n=== REDUÇÃO PERCENTUAL NO TEMPO DE ESPERA ===")
for fluxo in ['odonto', 'mulher']:
    reducao = ((media_espera_atual[fluxo] - media_espera_mutirao[fluxo]) / media_espera_atual[fluxo]) * 100
    print(f"{fluxo.capitalize()}: {reducao:.1f}% de redução")

# Conta número total de bloqueios (pacientes que não conseguiram entrar)
bloqueios_atual = df_atual[df_atual['evento'] == 'bloqueio'].shape[0] if 'evento' in df_atual.columns else 0
bloqueios_mutirao = df_mutirao[df_mutirao['evento'] == 'bloqueio'].shape[0] if 'evento' in df_mutirao.columns else 0

print(f"\nBloqueios (pacientes que foram embora):")
print(f"  Cenário atual: {bloqueios_atual}")
print(f"  Cenário mutirão: {bloqueios_mutirao}")