import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
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
Em ambientes de simulação computacional, é fundamental avaliar o
desempenho de servidores web medindo o tempo de resposta 
(em milissegundos) às requisições HTTP. 
Dois servidores — Servidor A e Servidor B — foram submetidos a 
um conjunto idêntico de requisições simuladas, e os tempos de
resposta foram registrados.

Questões Norteadoras

a) Qual servidor tem
menor tempo médio
de resposta?
b) Qual servidor apresenta
menor variabilidade?
c) Há outliers que
comprometem o
desempenho?
d) Qual servidor é mais
adequado para
produção?

O objetivo é determinar, com base em critérios estatísticos rigorosos, 
qual servidor oferece melhor desempenho e maior estabilidade para 
implantação em produção.
'''
# Variáveis e Parâmetros do Experimento
'''
Variável de Interesse
Tempo de Resposta (ms) — variável quantitativa contínua que mede o intervalo 
entre o envio da requisição e o recebimento completo da resposta HTTP.
Dados — Servidor A (ms) 120, 135, 128, 142, 119, 130, 125, 138, 122, 131
Dados — Servidor B (ms) 115, 160, 118, 175, 112, 158, 120, 170, 113, 165
'''
Dados_Servidor_A_ms = {120, 135, 128, 142, 119, 130, 125, 138, 122, 131}
Dados_Servidor_B_ms = {115, 160, 118, 175, 112, 158, 120, 170, 113, 165}
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
# Média
counter = 0
Media_Dados_Servidor_A_ms = 0
while (True):
    Media_Dados_Servidor_A_ms = Dados_Servidor_A_ms[counter] + Media_Dados_Servidor_A_ms
    counter +=1
    if counter == 9:
        counter = 0
        Media_Dados_Servidor_A_ms = Media_Dados_Servidor_A_ms / amostra
        break
Media_Dados_Servidor_B_ms = 0
while (True):
    Media_Dados_Servidor_B_ms = Dados_Servidor_B_ms[counter] + Media_Dados_Servidor_B_ms
    counter +=1
    if counter == 9:
        Media_Dados_Servidor_B_ms = Media_Dados_Servidor_B_ms / amostra
        break
msg_1 = ""
msg_2 = ""
if Media_Dados_Servidor_A_ms < Media_Dados_Servidor_B_ms:
    msg_1 = 'A é ' + (Media_Dados_Servidor_B_ms - Media_Dados_Servidor_A_ms) + 'ms mais rápido'

print ('Dados Servidor A (ms): ' + Dados_Servidor_A_ms)
print ('Dados Servidor B (ms): ' + Dados_Servidor_B_ms + '\n')
print ('Média (x̄) Servidor A (ms): ' + Media_Dados_Servidor_A_ms)
print ('Média (x̄) Servidor B (ms): ' + Media_Dados_Servidor_B_ms)
print ('Observação: ' + msg_1)
