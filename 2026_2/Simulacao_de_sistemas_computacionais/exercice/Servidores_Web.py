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

print(f"{'Medida':<20} {'Servidor A (ms)':<20} {'Servidor B (ms)':<20} {'Fórmula':<30} {'Observação'}")
print(f"{'Média (x̄)':<20} {Media_Dados_Servidor_A_ms:<20} {Media_Dados_Servidor_B_ms:<20} {'Σxᵢ / n':<30} {msg_media}")
print(f"{'Mediana (Md)':<20} {Mediana_Dados_Servidor_A_ms:<20} {Mediana_Dados_Servidor_B_ms:<20} {'Valor central ordenado':<30} {msg_mediana}")
print(f"{'Moda (Mo)':<20} {Moda_Dados_Servidor_A_ms:<20} {Moda_Dados_Servidor_B_ms:<20} {'Valor mais frequente':<30} {msg_moda}")
print("-" * 125)
# Estatística Descritiva — Dispersão e Variabilidade
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
print(f"\n{'Medida':<25} {'Servidor A':<20} {'Servidor B':<20} {'Fórmula':<30} {'Interpretação'}")
print(f"{'Variância (s²)':<25} {round(Variancia_A, 1):<20} {round(Variancia_B, 1):<20} {'Σ(xᵢ-x̄)² / (n-1)':<30} {int_variancia}")
print(f"{'Desvio Padrão (s)':<25} {round(Desvio_Padrao_A, 2):<20} {round(Desvio_Padrao_B, 2):<20} {'√s²':<30} {int_desvio}")
print(f"{'Amplitude (R)':<25} {Amplitude_A:<20} {Amplitude_B:<20} {'Máx - Mín':<30} {int_amplitude}")
print(f"{'Coef. de Variação (CV)':<25} {round(CV_A, 2):>5}%{'':<14} {round(CV_B, 2):>5}%{'':<14} {'(s / x̄) × 100':<30} {int_cv}")
print("-" * 125)