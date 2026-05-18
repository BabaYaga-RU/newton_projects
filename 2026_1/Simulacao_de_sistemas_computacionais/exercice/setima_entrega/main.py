
# pip install simpy numpy matplotlib
import simpy
import numpy as np
import matplotlib.pyplot as plt

# Configuração de semente para reprodutibilidade dos resultados estocásticos
np.random.seed(42)

# ============================================================================
# ATIVIDADE 3.1: SIMULAÇÃO DE ESTRESSE DE MEMÓRIA (Eng. de Computação)
# ============================================================================

class SimuladorMemoria:
    def __init__(self, capacidade_total):
        self.pool_memoria = capacidade_total
        self.memoria_em_uso = 0
        self.historico_uso = []  # Para geração do gráfico posterior

    def alocar_bloco(self, tamanho):
        if (self.memoria_em_uso + tamanho) <= self.pool_memoria:
            self.memoria_em_uso += tamanho
            self.historico_uso.append(self.memoria_em_uso)
            return True
        self.historico_uso.append(self.memoria_em_uso)
        return False

    def liberar_bloco(self, tamanho):
        self.memoria_em_uso = max(0, self.memoria_em_uso - tamanho)
        self.historico_uso.append(self.memoria_em_uso)

# --- Configuração e Execução da Simulação de Memória ---
tamanho_pool = 1024  # MB
simulador = SimuladorMemoria(tamanho_pool)

# Geração estocástica com NumPy (Distribuição Normal)
requisicoes = np.random.normal(loc=50, scale=15, size=100) # Média 50MB, DP 15MB

print("\n========== INICIANDO SIMULAÇÃO DE MEMÓRIA (3.1) ==========\n")
print(f"Tamanho do Pool de Memória: {tamanho_pool}MB\n")

sucessos = 0
falhas = 0

for i, bloco_alocado in enumerate(requisicoes):
    # Trata valores negativos gerados pela distribuição normal (caso ocorram)
    bloco_alocado = max(0.1, bloco_alocado) 
    
    sucesso = simulador.alocar_bloco(bloco_alocado)
    fragmentacao = (simulador.memoria_em_uso / simulador.pool_memoria) * 100
    status = "Sucesso" if sucesso else "Falha (Memória Insuficiente)"
    
    if sucesso:
        sucessos += 1
    else:
        falhas += 1
        
    print(f"Req #{i+1:03d} | Solicitado: {bloco_alocado:.2f}MB | Status: {status} | Uso Atual: {fragmentacao:.2f}%")

print("\n========== RESUMO DA SIMULAÇÃO DE MEMÓRIA ==========\n")
print(f"Total de Requisições: {len(requisicoes)}")
print(f"Alocações Bem-sucedidas: {sucessos}")
print(f"Falhas por Falta de Memória: {falhas}")
print(f"Percentil 95 de Memória Solicitada: {np.percentile(requisicoes, 95):.2f} MB")

# --- Gráfico de Uso da Memória ---
plt.figure(figsize=(10, 5))
plt.plot(simulador.historico_uso, color='blue', label='Memória Alocada (MB)')
plt.axhline(y=tamanho_pool, color='red', linestyle='--', label='Capacidade Máxima (1024 MB)')
plt.title('Simulação de Estresse de Memória - Ocupação ao Longo das Requisições')
plt.xlabel('Número da Operação / Evento')
plt.ylabel('Memória em Uso (MB)')
plt.legend()
plt.grid(True)
plt.show()


# ============================================================================
# ATIVIDADE 3.2: SIMULAÇÃO DE FILA HÍBRIDA (M/G/1)
# ============================================================================

def processo_servidor(ambiente, nome, servidor, tempos_espera):
    chegada = ambiente.now
    
    # Solicita o recurso do servidor
    with servidor.request() as requisicao:
        yield requisicao
        
        # Calcula o tempo que ficou esperando na fila
        espera = ambiente.now - llegada
        tempos_espera.append(espera)
        
        # Tempo de atendimento gerado pelo NumPy (Distribuição Normal)
        duracao_atendimento = max(0.1, np.random.normal(5, 1))
        yield ambiente.timeout(duracao_atendimento)

def gerador_pacotes(ambiente, servidor, tempos_espera):
    contador = 0
    while True:
        # Intervalo entre chegadas (Distribuição Exponencial - Processo de Poisson)
        intervalo = np.random.exponential(4)
        yield ambiente.timeout(intervalo)
        
        contador += 1
        ambiente.process(processo_servidor(ambiente, f"Pacote {contador}", servidor, tempos_espera))

# --- Configuração e Execução da Simulação do SimPy ---
print("\n========== INICIANDO SIMULAÇÃO DE FILA HÍBRIDA (3.2) ==========\n")

ambiente_simpy = simpy.Environment()
servidor_recurso = simpy.Resource(ambiente_simpy, capacity=1)
historico_tempos_espera = []

# Inicializa o processo gerador
ambiente_simpy.process(gerador_pacotes(ambiente_simpy, servidor_recurso, historico_tempos_espera))

# Executa até o tempo limite de 50 unidades de tempo
ambiente_simpy.run(until=50)

print("\n========== RESULTADO FINAL DA FILA ==========\n")
if historico_tempos_espera:
    tempo_medio = np.mean(historico_tempos_espera)
    percentil_95_espera = np.percentile(historico_tempos_espera, 95)
    print(f"Tempo Médio de Espera na Fila: {tempo_medio:.2f} unidades de tempo")
    print(f"Percentil 95 do Tempo de Espera: {percentil_95_espera:.2f} unidades de tempo")
    print(f"Total de pacotes que passaram pela fila: {len(historico_tempos_espera)}")
else:
    print("Nenhum pacote foi processado no tempo estipulado.")

# --- Gráfico de Tempo de Espera dos Pacotes ---
plt.figure(figsize=(10, 5))
plt.bar(range(len(historico_tempos_espera)), historico_tempos_espera, color='purple', alpha=0.7)
plt.axhline(y=np.mean(historico_tempos_espera), color='orange', linestyle='-', label=f'Média ({np.mean(historico_tempos_espera):.2f})')
plt.title('Tempo de Espera na Fila por Pacote Processado')
plt.xlabel('Índice do Pacote')
plt.ylabel('Tempo de Espera (unidades de tempo)')
plt.legend()
plt.grid(axis='y')
plt.show()
