import simpy
import random

TEMPO_SIMULACAO = 60  # minutos - Duração total da simulação
INTERVALO_CHEGADA = 5  # minutos entre chegadas - Média do intervalo entre chegadas de clientes
TEMPO_ATENDIMENTO = [3, 7]  # tempo de atendimento entre 3 e 7 minutos - Intervalo de tempo de serviço

def atender_cliente(env, nome, caixa):
    tempo = random.randint(*TEMPO_ATENDIMENTO)
    print(f"{nome} começou atendimento às {env.now:.1f} min (tempo: {tempo} min)")
    yield env.timeout(tempo)  # Aguarda o tempo de atendimento
    print(f"{nome} terminou atendimento às {env.now:.1f} min")

def chegada_clientes(env, caixa):
    i = 0
    while env.now < TEMPO_SIMULACAO:
        i += 1
        yield env.timeout(random.expovariate(1.0 / INTERVALO_CHEGADA))
        env.process(atender_cliente(env, f"Cliente {i}", caixa))

# Configuração e execução da simulação
env = simpy.Environment()  # Cria o ambiente de simulação
caixa = simpy.Resource(env, capacity=1)  # Cria um recurso (caixa) com capacidade 1 (um atendente)
env.process(chegada_clientes(env, caixa))  # Inicia o processo de chegada de clientes
env.run(until=TEMPO_SIMULACAO)  # Executa a simulação pelo tempo especificado

# ================ 1. Gráfico: Tempo de Atendimento por Cliente ================

import matplotlib.pyplot as plt

# Suponha que você tenha uma lista com os tempos de atendimento
tempos_atendimento = [4, 6, 5, 7, 3, 6, 4]  # exemplo

plt.figure(figsize=(10, 5))  # figsize define o tamanho da figura em polegadas (largura, altura)
plt.plot(range(1, len(tempos_atendimento)+1), tempos_atendimento, marker='o', linestyle='-')
plt.title('Tempo de Atendimento por Cliente')
plt.xlabel('Cliente')  # ylabel define o rótulo do eixo Y (vertical)
plt.ylabel('Tempo (minutos)')  # xlabel define o rótulo do eixo X (horizontal)
plt.grid(True)  # grid(True) adiciona linhas de grade para facilitar a leitura dos valores
plt.show()

# =================== 2. Gráfico: Tempo de Espera por Cliente ==================

tempos_espera = [0, 2, 1, 3, 0, 4, 2]  # exemplo
plt.figure(figsize=(10, 5))
plt.bar(range(1, len(tempos_espera)+1), tempos_espera, color='orange')  # color define a cor das barras
plt.title('Tempo de Espera por Cliente')
plt.xlabel('Cliente')
plt.ylabel('Tempo de Espera (minutos)')
plt.show()

# ========= 3. Gráfico: Número de Clientes Atendidos ao Longo do Tempo =========

tempos_chegada = [2, 7, 12, 18, 25, 32, 40]  # exemplo
clientes_atendidos = list(range(1, len(tempos_chegada)+1))  # [1, 2, 3, 4, 5, 6, 7]
plt.figure(figsize=(10, 5))
plt.step(tempos_chegada, clientes_atendidos, where='post')  # where='post' define que o degrau ocorre após o ponto
plt.title('Clientes Atendidos ao Longo do Tempo')
plt.xlabel('Tempo (minutos)')
plt.ylabel('Número de Clientes')
plt.grid(True)
plt.show()

# =============================== Próximos Passos ==============================

# Painel Interativo
'''
Transformar os gráficos em um painel interativo com Plotly
'''

# Exportação de Dados
'''
Exportar os dados para análise em Excel
'''

# Análise Avançada
'''
Integrar com Power BI para análises mais complexas
'''
