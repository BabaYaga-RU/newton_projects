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
# ===================================== Estatística Descritiva — Tendência Central =====================================
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
# ================================= Estatística Descritiva — Dispersão e Variabilidade =================================
print("\n" + "="*125)
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
if CV_A < 10:
    int_cv = "A é altamente estável"
else:
    int_cv = "Análise de estabilidade necessária"

# Tabela de Dispersão
print(f"\n{'Medida':<25} {'Servidor A':<20} {'Servidor B':<20} {'Formula':<30} {'Interpretacao'}")
print(f"{'Variancia (s2)':<25} {round(Variancia_A, 1):<20} {round(Variancia_B, 1):<20} {'Soma / (n-1)':<30} {int_variancia}")
print(f"{'Desvio Padrao (s)':<25} {round(Desvio_Padrao_A, 2):<20} {round(Desvio_Padrao_B, 2):<20} {'Raiz quadrada':<30} {int_desvio}")
print(f"{'Amplitude (R)':<25} {Amplitude_A:<20} {Amplitude_B:<20} {'Max - Min':<30} {int_amplitude}")
print(f"{'Coef. de Variacao (CV)':<25} {round(CV_A, 2):>5}%{'':<14} {round(CV_B, 2):>5}%{'':<14} {'(s / media) * 100':<30} {int_cv}")

# ======================================= Boxplot Comparativo — Servidores A e B =======================================
print("\n" + "="*125)
print("Boxplot Comparativo — Servidores A e B")

# Calcular estatísticas para boxplot
def calcular_estatisticas_boxplot(dados, nome):
    minimo = min(dados)
    q1 = np.percentile(dados, 25)
    mediana = np.percentile(dados, 50)
    q3 = np.percentile(dados, 75)
    maximo = max(dados)
    iqr = q3 - q1
    return [minimo, q1, mediana, q3, maximo, iqr]

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

print("Cinco Números de Resumo")
print(f"\n{'Estatística':<25} {'Serv. A':<20} {'Serv. B':<20} {'Observação'}")
print(f"{'Mínimo':<25} {estatisticas_a[0]:<20} {estatisticas_b[0]:<20} {'':<30}")
print(f"{'Q1 (1º Quartil)':<25} {round(estatisticas_a[1], 1):<20} {round(estatisticas_b[1], 1):<20} {'':<30}")
print(f"{'Mediana (Q2)':<25} {round(estatisticas_a[2], 1):<20} {round(estatisticas_b[2], 1):<20} {'':<30}")
print(f"{'Q3 (3º Quartil)':<25} {round(estatisticas_a[3], 1):<20} {round(estatisticas_b[3], 1):<20} {'':<30}")
print(f"{'Máximo':<25} {estatisticas_a[4]:<20} {estatisticas_b[4]:<20} {'':<30}")
print(f"{'IIQ (Q3-Q1)':<25} {round(estatisticas_a[5], 1):<20} {round(estatisticas_b[5], 1):<20} {'':<30}")

# Interpretação do IIQ
iqr_a = estatisticas_a[5]
iqr_b = estatisticas_b[5]

if iqr_b > iqr_a:
    iqr_ratio = iqr_b / iqr_a
    print(f"\nO IIQ (Intervalo Interquartil) do Servidor B é ~{round(iqr_ratio, 1)}× maior,")
    print("evidenciando maior dispersão e presença de valores extremos.")
else:
    iqr_ratio = iqr_a / iqr_b
    print(f"\nO IIQ (Intervalo Interquartil) do Servidor A é ~{round(iqr_ratio, 1)}× maior,")
    print("evidenciando maior dispersão e presença de valores extremos.")

import matplotlib.pyplot as plt
plt.rc('axes', labelsize=14)
plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12)
import seaborn as sns
plt.figure(figsize=(10, 6))

# Usar apenas os 5 primeiros valores (excluindo o IQR)
estatisticas_a_plot = estatisticas_a[:5]
estatisticas_b_plot = estatisticas_b[:5]
categorias = ['Mínimo', 'Q1 (25%)', 'Mediana Q2 (50%)', 'Q3 (75%)', 'Máximo']

y = np.arange(len(categorias))
height = 0.35

plt.barh(y - height/2, estatisticas_a_plot, height, label='Servidor A', color='#2E86AB')
plt.barh(y + height/2, estatisticas_b_plot, height, label='Servidor B', color='#F18F01')

plt.yticks(y, categorias)
plt.legend()
plt.tight_layout()
plt.show()

# ==================================== Interpretação dos Resultados — Itens a) a d) ====================================
print("\n" + "="*125)
print("INTERPRETAÇÃO DOS RESULTADOS — ITENS A) A D)")

# a) Qual servidor tem menor tempo médio de resposta?
print("\n1. Menor Tempo Médio")
if Media_Dados_Servidor_A_ms < Media_Dados_Servidor_B_ms:
    diferenca_media = Media_Dados_Servidor_B_ms - Media_Dados_Servidor_A_ms
    percentual = (diferenca_media / Media_Dados_Servidor_B_ms) * 100
    print(f"Servidor A vence com média de {round(Media_Dados_Servidor_A_ms, 1)} ms contra")
    print(f"{round(Media_Dados_Servidor_B_ms, 1)} ms do Servidor B — diferença de {round(diferenca_media, 1)} ms")
    print(f"(≈{round(percentual, 1)}% mais rápido), estatisticamente relevante em")
    print("aplicações de alta frequência.")
else:
    diferenca_media = Media_Dados_Servidor_A_ms - Media_Dados_Servidor_B_ms
    percentual = (diferenca_media / Media_Dados_Servidor_A_ms) * 100
    print(f"Servidor B vence com média de {round(Media_Dados_Servidor_B_ms, 1)} ms contra")
    print(f"{round(Media_Dados_Servidor_A_ms, 1)} ms do Servidor A — diferença de {round(diferenca_media, 1)} ms")
    print(f"(≈{round(percentual, 1)}% mais rápido), estatisticamente relevante em")
    print("aplicações de alta frequência.")

# b) Qual servidor apresenta menor variabilidade?
print("\n2. Menor Variabilidade")
if CV_A < CV_B:
    ratio_desvio = Desvio_Padrao_B / Desvio_Padrao_A
    print(f"Servidor A apresenta CV de {round(CV_A, 2)}% (muito baixo)")
    print(f"contra {round(CV_B, 2)}% do Servidor B. O desvio padrão do")
    print(f"A ({round(Desvio_Padrao_A, 2)} ms) é {round(ratio_desvio, 1)}× menor, garantindo")
    print("comportamento mais previsível.")
else:
    ratio_desvio = Desvio_Padrao_A / Desvio_Padrao_B
    print(f"Servidor B apresenta CV de {round(CV_B, 2)}% (muito baixo)")
    print(f"contra {round(CV_A, 2)}% do Servidor A. O desvio padrão do")
    print(f"B ({round(Desvio_Padrao_B, 2)} ms) é {round(ratio_desvio, 1)}× menor, garantindo")
    print("comportamento mais previsível.")

# c) Há outliers que comprometem o desempenho?
print("\n3. Presença de Outliers")
if len(outliers_b) > len(outliers_a):
    print(f"Servidor B apresenta valores extremos em torno")
    print(f"de {min(outliers_b)}–{max(outliers_b)} ms (IIQ = {round(iqr_b, 1)} ms). O Servidor A é livre")
    print(f"de outliers significativos, com IIQ compacto de {round(iqr_a, 1)}")
    print("ms.")
elif len(outliers_a) > len(outliers_b):
    print(f"Servidor A apresenta valores extremos em torno")
    print(f"de {min(outliers_a)}–{max(outliers_a)} ms (IIQ = {round(iqr_a, 1)} ms). O Servidor B é livre")
    print(f"de outliers significativos, com IIQ compacto de {round(iqr_b, 1)}")
    print("ms.")
else:
    print("Ambos os servidores apresentam padrões semelhantes de outliers.")
    if len(outliers_a) > 0:
        print(f"Outliers detectados: A = {outliers_a}, B = {outliers_b}")

# d) Qual servidor é mais adequado para produção?
print("\n4. Adequação para Produção")
if Media_Dados_Servidor_A_ms < Media_Dados_Servidor_B_ms and CV_A < CV_B and len(outliers_a) <= len(outliers_b):
    print("Servidor A é recomendado para produção. Além")
    print("de mais rápido, sua baixa variabilidade assegura")
    print("SLA (Service Level Agreement) consistente e")
    print("experiência de usuário previsível.")
elif Media_Dados_Servidor_B_ms < Media_Dados_Servidor_A_ms and CV_B < CV_A and len(outliers_b) <= len(outliers_a):
    print("Servidor B é recomendado para produção. Além")
    print("de mais rápido, sua baixa variabilidade assegura")
    print("SLA (Service Level Agreement) consistente e")
    print("experiência de usuário previsível.")
else:
    print("Recomendação mista: o Servidor A/B tem menor tempo médio,")
    print("mas o Servidor B/A tem menor variabilidade. Avalie o")
    print("trade-off entre velocidade e estabilidade conforme o")
    print("critério de aceitação do seu ambiente de produção.")

# ==================================== Conclusão e Recomendação para Produção ====================================
print("\n" + "="*125)
print("CONCLUSÃO E RECOMENDAÇÃO PARA PRODUÇÃO")

# Determinar o servidor recomendado
if Media_Dados_Servidor_A_ms < Media_Dados_Servidor_B_ms and CV_A < CV_B and len(outliers_a) <= len(outliers_b):
    servidor_recomendado = "A"
    cv_recomendado = CV_A
    cv_outro = CV_B
    media_recomendado = Media_Dados_Servidor_A_ms
    media_outro = Media_Dados_Servidor_B_ms
    amplitude_recomendado = Amplitude_A
    amplitude_outro = Amplitude_B
    max_recomendado = max(Dados_Servidor_A_ms)
    max_outro = max(Dados_Servidor_B_ms)
    ratio_variabilidade = Desvio_Padrao_B / Desvio_Padrao_A
else:
    servidor_recomendado = "B"
    cv_recomendado = CV_B
    cv_outro = CV_A
    media_recomendado = Media_Dados_Servidor_B_ms
    media_outro = Media_Dados_Servidor_A_ms
    amplitude_recomendado = Amplitude_B
    amplitude_outro = Amplitude_A
    max_recomendado = max(Dados_Servidor_B_ms)
    max_outro = max(Dados_Servidor_A_ms)
    ratio_variabilidade = Desvio_Padrao_A / Desvio_Padrao_B

# Determinar o servidor não recomendado
if servidor_recomendado == "A":
    servidor_nao_recomendado = "B"
else:
    servidor_nao_recomendado = "A"

print(f"\nEscolha: Servidor {servidor_recomendado}")
print(f"Média de {round(media_recomendado, 1)} ms e CV de apenas {round(cv_recomendado, 2)}%")
print("demonstram desempenho superior e")
print("altamente estável. Ideal para ambientes")
print("críticos com SLA rigoroso.")

print(f"\nServidor {servidor_nao_recomendado}: Instável")
print(f"CV de {round(cv_outro, 2)}% e amplitude de {amplitude_outro} ms indicam")
print("comportamento imprevisível. Picos de até")
print(f"{max_outro} ms prejudicam a experiência do usuário")
print("final.")

print("\nCritério-Chave: CV")
print("Em simulação computacional, o Coeficiente")
print("de Variação é o indicador mais importante")
print("para estabilidade — mais relevante que a")
print("média isolada.")

print(f"{round(cv_recomendado, 2):<25} {round(cv_outro, 2):<20} {round(ratio_variabilidade, 1):<15}{'×':<5}")
print(f"CV — Servidor {servidor_recomendado:<15} CV — Servidor {servidor_nao_recomendado:<10} Fator de Variabilidade")
print(f"Baixíssima dispersão{'':<10} Alta dispersão{'':<15} {servidor_nao_recomendado} varia {round(ratio_variabilidade, 1)}× mais que {servidor_recomendado}")

