# pip install simpy
import simpy
import random

# Configurações
TEMPO_SIMULACAO = 60 # minutos
INTERVALO_CHEGADA = 5 # minutos entre chegadas
TEMPO_ATENDIMENTO = [3, 7] # tempo de atendimento entre 3 e 7 minutos

def atender_cliente(env, nome, caixa):
    tempo = random.randint(*TEMPO_ATENDIMENTO)
    print(f"{nome} começou atendimento às {env.now:.1f} min (tempo: {tempo} min)")
    yield env.timeout(tempo)
    print(f"{nome} terminou atendimento às {env.now:.1f} min")

def chegada_clientes(env, caixa):
    i = 0
    while env.now < TEMPO_SIMULACAO:
        i += 1
        yield env.timeout(random.expovariate(1.0 / INTERVALO_CHEGADA))
        env.process(atender_cliente(env, f"Cliente {i}", caixa))

env = simpy.Environment()
caixa = simpy.Resource(env, capacity=1) # apenas um atendente
env.process(chegada_clientes(env, caixa))
env.run(until=TEMPO_SIMULACAO)


# ================ 1. Gráfico: Tempo de Atendimento por Cliente ================
import matplotlib.pyplot as plt# Suponha que você tenha
uma lista com os tempos de atendimentotempos_atendimento
= [4, 6, 5, 7, 3, 6, 4] # exemplo
plt.figure(figsize=(10, 5))plt.plot(range(1,
len(tempos_atendimento)+1), tempos_atendimento,
marker='o', linestyle='-')plt.title('Tempo de
Atendimento por
Cliente')plt.xlabel('Cliente')plt.ylabel('Tempo
(minutos)')plt.grid(True)plt.show()


# =================== 2. Gráfico: Tempo de Espera por Cliente ==================
tempos_espera = [0, 2, 1, 3, 0, 4, 2]
# exemplo
plt.figure(figsize=(10,
5))plt.bar(range(1, len(tempos_espera)+1),
tempos_espera,
color='orange')plt.title('Tempo de Espera
por
Cliente')plt.xlabel('Cliente')plt.ylabel('
Tempo de Espera (minutos)')plt.show()

# ========= 3. Gráfico: Número de Clientes Atendidos ao Longo do Tempo =========
tempos_chegada = [2, 7, 12, 18, 25, 32,
40] # exemploclientes_atendidos =
list(range(1,
len(tempos_chegada)+1))plt.figure(figsiz
e=(10, 5))plt.step(tempos_chegada,
clientes_atendidos,
where='post')plt.title('Clientes
Atendidos ao Longo do
Tempo')plt.xlabel('Tempo
(minutos)')plt.ylabel('Número de
Clientes')plt.grid(True)plt.show()


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