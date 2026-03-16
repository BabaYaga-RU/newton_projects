import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
'''
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
'''
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
# ==============================================================
# Resoluções dos Exercícios 1 — Análise de Desempenho de Servidores Web
'''
Nesta apresentação, exploramos a aplicação de estatística descritiva para 
comparar o desempenho de dois servidores web (A e B), interpretando métricas de 
tendência central e dispersão, além de visualizações como boxplot. O objetivo é
desenvolver raciocínio analítico para tomada de decisão emambientes 
computacionais reais.
'''
# Agenda
'''
01
Definição do Problema
Contexto e motivação da análise comparativa de servidores web
02
Variáveis e Parâmetros
Identificação das variáveis de interesse e dos dados coletados
03
Estatística Descritiva
Média, mediana, moda, variância, desvio padrão, amplitude e CV
04
Boxplot e Interpretação
Visualização comparativa e conclusões sobre estabilidade
05
Exercício 2 e Recomendação Final
Template de resolução e recomendação para ambiente de produção
'''
# Definição do Problema
'''
Contexto
Em ambientes de simulação computacional, é fundamental avaliar o desempenho de 
servidores web medindo o tempo de resposta (em milissegundos) às requisições HTTP. 
Dois servidores — Servidor A e Servidor B — foram submetidos a um conjunto 
idêntico de requisições simuladas, e os tempos de resposta foram registrados.

Questões Norteadoras

a) Qual servidor tem menor tempo médio de resposta?
b) Qual servidor apresenta menor variabilidade?
c) Há outliers que comprometem o desempenho?
d) Qual servidor é mais adequado para produção?

O objetivo é determinar, com base em critérios estatísticos rigorosos, 
qual servidor oferece melhor desempenho e maior estabilidade para 
implantação em produção.
'''
# Variáveis e Parâmetros do Experimento
'''
Variável de Interesse
Tempo de Resposta (ms) — variável quantitativa contínua que mede o intervalo 
entre o envio da requisição e o recebimento completo da resposta HTTP.
'''
Dados_Servidor_A_ms = [120, 135, 128, 142, 119, 130, 125, 138, 122, 131]
Dados_Servidor_B_ms = [115, 160, 118, 175, 112, 158, 120, 170, 113, 165]
'''
Parâmetros de Coleta
'''
amostra = 10 # (Amostras por servidor)
'''
Unidade
Milissegundos (ms)

Tipo
Simulação controlada

Os dados foram gerados em ambiente de simulação computacional com carga de
requisições idênticas para ambos os servidores.
'''
# Estatística Descritiva — Tendência Central
print("Estatística Descritiva — Tendência Central")
'''
As medidas de tendência central revelam o "centro" da distribuição dos tempos de
resposta. Valores menores indicam melhor desempenho médio.
'''
# Média A
indice_media = 0
Media_Dados_Servidor_A_ms = 0
while (True):
    Media_Dados_Servidor_A_ms = Dados_Servidor_A_ms[indice_media] + Media_Dados_Servidor_A_ms
    indice_media += 1
    if indice_media == amostra:
        indice_media = 0
        Media_Dados_Servidor_A_ms = Media_Dados_Servidor_A_ms / amostra
        break

# Médiana A
dados_ordenados_a = sorted(Dados_Servidor_A_ms)
mediana_par = amostra % 2 == 0
Mediana_Dados_Servidor_A_ms = 0
if (mediana_par == True):
    indice_1 = int((amostra / 2) - 1)
    indice_2 = int(amostra / 2)
    Mediana_Dados_Servidor_A_ms = (dados_ordenados_a[indice_1] + dados_ordenados_a[indice_2]) / 2
else:
    Mediana_Dados_Servidor_A_ms = dados_ordenados_a[int(amostra / 2)]

# Moda A
Moda_Dados_Servidor_A_ms = ""
frequencia_moda_A = {}
for dado in Dados_Servidor_A_ms:
    if dado in frequencia_moda_A:
        frequencia_moda_A[dado] += 1
    else:
        frequencia_moda_A[dado] = 1
maior_frequencia_A = max(frequencia_moda_A.values())
moda_A = []
for chave in frequencia_moda_A:
    repetido = frequencia_moda_A[chave]
    if repetido == maior_frequencia_A:
        moda_A.append(chave)

if maior_frequencia_A == 1:
    Moda_Dados_Servidor_A_ms = "Amodal"
else:
    Moda_Dados_Servidor_A_ms = str(moda_A)

# Média B
Media_Dados_Servidor_B_ms = 0
while (True):
    Media_Dados_Servidor_B_ms = Dados_Servidor_B_ms[indice_media] + Media_Dados_Servidor_B_ms
    indice_media += 1
    if indice_media == amostra:
        indice_media = 0
        Media_Dados_Servidor_B_ms = Media_Dados_Servidor_B_ms / amostra
        break

# Médiana B
dados_ordenados_b = sorted(Dados_Servidor_B_ms)
Mediana_Dados_Servidor_B_ms = 0
if (mediana_par == True):
    indice_1 = int((amostra / 2) - 1)
    indice_2 = int(amostra / 2)
    Mediana_Dados_Servidor_B_ms = (dados_ordenados_b[indice_1] + dados_ordenados_b[indice_2]) / 2
else:
    Mediana_Dados_Servidor_B_ms = dados_ordenados_b[int(amostra / 2)]

# Moda B
Moda_Dados_Servidor_B_ms = ""
frequencia_moda_B = {}
for dado in Dados_Servidor_B_ms:
    if dado in frequencia_moda_B:
        frequencia_moda_B[dado] += 1
    else:
        frequencia_moda_B[dado] = 1
maior_frequencia_B = max(frequencia_moda_B.values())
moda_B = []
for chave in frequencia_moda_B:
    repetido = frequencia_moda_B[chave]
    if repetido == maior_frequencia_B:
        moda_B.append(chave)

if maior_frequencia_B == 1:
    Moda_Dados_Servidor_B_ms = "Amodal"
else:
    Moda_Dados_Servidor_B_ms = str(moda_B)

#Mensagens
msg_media = ""
msg_mediana = ""
if Media_Dados_Servidor_A_ms < Media_Dados_Servidor_B_ms:
    msg_media = 'A é ' + str(round(Media_Dados_Servidor_B_ms - Media_Dados_Servidor_A_ms, 2)) + 'ms mais rápido'
    if Mediana_Dados_Servidor_A_ms < Mediana_Dados_Servidor_B_ms:
        msg_mediana = "Confirma vantagem do A"
    else:
        msg_mediana = "Vantagem do B"
else:
    msg_media = 'B é ' + str(round(Media_Dados_Servidor_A_ms - Media_Dados_Servidor_B_ms, 2)) + 'ms mais rápido'
    if Mediana_Dados_Servidor_A_ms < Mediana_Dados_Servidor_B_ms:
        msg_mediana = "Vantagem do A"
    else:
        msg_mediana = "Confirma vantagem do B"

msg_moda = ""
validador_a = (Moda_Dados_Servidor_A_ms == "Amodal")
validador_b = (Moda_Dados_Servidor_B_ms == "Amodal")
if validador_a and validador_b:
    msg_moda = "Sem repetição nos dados"
elif not validador_a and validador_b:
    msg_moda = "Servidor A é mais previsível por possuir uma moda."
elif validador_a and not validador_b:
    msg_moda = "Servidor B é mais previsível por possuir uma moda."
else:
    if moda_A[0] < moda_B[0]:
        msg_moda = "Servidor A ganha por ter o tempo frequente mais baixo."
    elif moda_B[0] < moda_A[0]:
        msg_moda = "Servidor B ganha por ter o tempo frequente mais baixo."
    else:
        msg_moda = "Modas idênticas, empate técnico nesta métrica."

print(f"{'Medida':<20} {'Servidor A (ms)':<20} {'Servidor B (ms)':<20} {'Formula':<30} {'Observacao'}")
print(f"{'Media (x)':<20} {Media_Dados_Servidor_A_ms:<20} {Media_Dados_Servidor_B_ms:<20} {'Soma / n':<30} {msg_media}")
print(f"{'Mediana (Md)':<20} {Mediana_Dados_Servidor_A_ms:<20} {Mediana_Dados_Servidor_B_ms:<20} {'Valor central ordenado':<30} {msg_mediana}")
print(f"{'Moda (Mo)':<20} {Moda_Dados_Servidor_A_ms:<20} {Moda_Dados_Servidor_B_ms:<20} {'Valor mais frequente':<30} {msg_moda}")
print("-" * 125)
# Estatística Descritiva — Dispersão e Variabilidade
print("Estatística Descritiva — Dispersão e Variabilidade")
'''
As medidas de dispersão são cruciais para avaliar a estabilidade do servidor. Um
servidor com baixa variabilidade é mais previsível e confiável em produção.
'''
# Variância A
soma_desvios_A = 0
for dado in Dados_Servidor_A_ms:
    soma_desvios_A += (dado - Media_Dados_Servidor_A_ms) ** 2
Variancia_A = soma_desvios_A / (amostra - 1)

# Desvio Padrão A
Desvio_Padrao_A = Variancia_A ** 0.5

# Amplitude A
Amplitude_A = max(Dados_Servidor_A_ms) - min(Dados_Servidor_A_ms)

# Coeficiente de Variação A
CV_A = (Desvio_Padrao_A / Media_Dados_Servidor_A_ms) * 100

# Variância B
soma_desvios_B = 0
for dado in Dados_Servidor_B_ms:
    soma_desvios_B += (dado - Media_Dados_Servidor_B_ms) ** 2
Variancia_B = soma_desvios_B / (amostra - 1)

# Desvio Padrão B
Desvio_Padrao_B = Variancia_B ** 0.5

# Amplitude B
Amplitude_B = max(Dados_Servidor_B_ms) - min(Dados_Servidor_B_ms)

# Coeficiente de Variação B
CV_B = (Desvio_Padrao_B / Media_Dados_Servidor_B_ms) * 100

# Interpretações
int_variancia = f"B é ~{round(Variancia_B / Variancia_A, 1)}x mais disperso"
int_desvio = f"B varia {round(Desvio_Padrao_B / Desvio_Padrao_A, 1)}x mais"
int_amplitude = "B tem range muito maior"
int_cv = "A é altamente estável" if CV_A < 10 else "Análise de estabilidade necessária"

# Tabela de Dispersão
print(f"\n{'Medida':<25} {'Servidor A':<20} {'Servidor B':<20} {'Formula':<30} {'Interpretacao'}")
print(f"{'Variancia (s2)':<25} {round(Variancia_A, 1):<20} {round(Variancia_B, 1):<20} {'Soma / (n-1)':<30} {int_variancia}")
print(f"{'Desvio Padrao (s)':<25} {round(Desvio_Padrao_A, 2):<20} {round(Desvio_Padrao_B, 2):<20} {'Raiz quadrada':<30} {int_desvio}")
print(f"{'Amplitude (R)':<25} {Amplitude_A:<20} {Amplitude_B:<20} {'Max - Min':<30} {int_amplitude}")
print(f"{'Coef. de Variacao (CV)':<25} {round(CV_A, 2):>5}%{'':<14} {round(CV_B, 2):>5}%{'':<14} {'(s / media) * 100':<30} {int_cv}")
print("-" * 125)

# Boxplot Comparativo — Servidores A e B
print("Boxplot Comparativo — Servidores A e B")

# Calcular estatísticas para boxplot
def calcular_estatisticas_boxplot(dados, nome):
    minimo = min(dados)
    q1 = np.percentile(dados, 25)
    mediana = np.percentile(dados, 50)
    q3 = np.percentile(dados, 75)
    maximo = max(dados)
    
    print(f"\n{nome}:")
    print(f"  Mínimo: {minimo}")
    print(f"  Q1 (25%): {q1}")
    print(f"  Mediana Q2 (50%): {mediana}")
    print(f"  Q3 (75%): {q3}")
    print(f"  Máximo: {maximo}")
    
    return [minimo, q1, mediana, q3, maximo]

estatisticas_a = calcular_estatisticas_boxplot(Dados_Servidor_A_ms, "Servidor A")
estatisticas_b = calcular_estatisticas_boxplot(Dados_Servidor_B_ms, "Servidor B")

# Identificar outliers usando o método do IQR
def identificar_outliers(dados):
    Q1 = np.percentile(dados, 25)
    Q3 = np.percentile(dados, 75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    outliers = [x for x in dados if x < limite_inferior or x > limite_superior]
    return outliers, limite_inferior, limite_superior

outliers_a, li_a, ls_a = identificar_outliers(Dados_Servidor_A_ms)
outliers_b, li_b, ls_b = identificar_outliers(Dados_Servidor_B_ms)

print(f"\nAnálise de Outliers:")
print(f"Servidor A - Outliers: {outliers_a}")
print(f"Servidor B - Outliers: {outliers_b}")

# Plotar figuras bonitas (opcional)
try:
    import matplotlib.pyplot as plt
    plt.rc('axes', labelsize=14)
    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)
    import seaborn as sns
    plotting_available = True
    print("Bibliotecas de visualização carregadas com sucesso!")
    
    # Visualizações comparativas - Gráfico de barras horizontais
    plt.figure(figsize=(12, 8))

    # Preparar dados para o gráfico de barras usando as estatísticas calculadas
    estatisticas_a = estatisticas_a  # Usa as estatísticas calculadas da função
    estatisticas_b = estatisticas_b  # Usa as estatísticas calculadas da função
    categorias = ['Mínimo', 'Q1 (25%)', 'Mediana Q2 (50%)', 'Q3 (75%)', 'Máximo']

    y = np.arange(len(categorias))
    height = 0.35

    plt.barh(y - height/2, estatisticas_a, height, label='Servidor A', color='blue', alpha=0.7)
    plt.barh(y + height/2, estatisticas_b, height, label='Servidor B', color='orange', alpha=0.7)

    plt.xlabel('Tempo de Resposta (ms)')
    plt.ylabel('Estatísticas')
    plt.title('Comparação das Estatísticas dos Servidores A e B')
    plt.yticks(y, categorias)
    plt.legend()
    plt.grid(axis='x', alpha=0.3)

    # Adicionar valores nas barras
    for i, (a, b) in enumerate(zip(estatisticas_a, estatisticas_b)):
        plt.text(a + 2, i - height/2, f'{a}', ha='left', va='center', fontsize=10)
        plt.text(b + 2, i + height/2, f'{b}', ha='left', va='center', fontsize=10)

    plt.tight_layout()
    plt.show()
    
except ImportError:
    print("Avisos: Bibliotecas de visualização (matplotlib/seaborn) não encontradas. Instale com: pip install matplotlib seaborn")
    print("Visualizações puladas - bibliotecas de plotagem não disponíveis")

# Conclusão e Recomendação
print("\n" + "="*60)
print("CONCLUSÃO E RECOMENDAÇÃO")
print("="*60)

print(f"\n1. Desempenho Médio:")
print(f"   - Servidor A: {Media_Dados_Servidor_A_ms:.2f} ms")
print(f"   - Servidor B: {Media_Dados_Servidor_B_ms:.2f} ms")
if Media_Dados_Servidor_A_ms < Media_Dados_Servidor_B_ms:
    print(f"   - O Servidor A é {Media_Dados_Servidor_B_ms - Media_Dados_Servidor_A_ms:.2f} ms mais rápido em média")
else:
    print(f"   - O Servidor B é {Media_Dados_Servidor_A_ms - Media_Dados_Servidor_B_ms:.2f} ms mais rápido em média")

print(f"\n2. Estabilidade (Variabilidade):")
print(f"   - Servidor A - CV: {CV_A:.2f}%")
print(f"   - Servidor B - CV: {CV_B:.2f}%")
if CV_A < CV_B:
    print(f"   - O Servidor A é mais estável (menor variabilidade)")
else:
    print(f"   - O Servidor B é mais estável (menor variabilidade)")

print(f"\n3. Presença de Outliers:")
print(f"   - Servidor A: {len(outliers_a)} outliers")
print(f"   - Servidor B: {len(outliers_b)} outliers")

print(f"\n4. Recomendação Final:")
if Media_Dados_Servidor_A_ms < Media_Dados_Servidor_B_ms and CV_A < CV_B:
    print("   - RECOMENDADO: Servidor A")
    print("   - Motivo: Menor tempo médio de resposta e maior estabilidade")
elif Media_Dados_Servidor_B_ms < Media_Dados_Servidor_A_ms and CV_B < CV_A:
    print("   - RECOMENDADO: Servidor B")
    print("   - Motivo: Menor tempo médio de resposta e maior estabilidade")
else:
    print("   - DECISÃO DEPENDENTE DO CRITÉRIO:")
    if Media_Dados_Servidor_A_ms < Media_Dados_Servidor_B_ms:
        print("   - Para priorizar velocidade: Servidor A")
    else:
        print("   - Para priorizar velocidade: Servidor B")
    if CV_A < CV_B:
        print("   - Para priorizar estabilidade: Servidor A")
    else:
        print("   - Para priorizar estabilidade: Servidor B")

print("\n" + "="*60)
