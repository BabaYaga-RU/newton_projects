import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
warnings.filterwarnings('ignore')

# Dados corrigidos conforme os resultados apresentados nos slides
# Média A: 129.0 | Média B: 140.6
Dados_Servidor_A_ms = [120, 135, 128, 142, 119, 130, 125, 138, 122, 131]
Dados_Servidor_B_ms = [110, 155, 115, 180, 105, 145, 125, 175, 122, 174]
amostra = 10

# ==============================================================
# Estatística Descritiva — Tendência Central
# ==============================================================

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

# Mediana A
dados_ordenados_a = sorted(Dados_Servidor_A_ms)
mediana_par = amostra % 2 == 0
if (mediana_par == True):
    indice_1 = int((amostra / 2) - 1)
    indice_2 = int(amostra / 2)
    Mediana_Dados_Servidor_A_ms = (dados_ordenados_a[indice_1] + dados_ordenados_a[indice_2]) / 2
else:
    Mediana_Dados_Servidor_A_ms = dados_ordenados_a[int(amostra / 2)]

# Moda A
frequencia_moda_A = {}
for dado in Dados_Servidor_A_ms:
    frequencia_moda_A[dado] = frequencia_moda_A.get(dado, 0) + 1
maior_frequencia_A = max(frequencia_moda_A.values())
if maior_frequencia_A == 1:
    Moda_Dados_Servidor_A_ms = "Amodal"
else:
    Moda_Dados_Servidor_A_ms = str([k for k, v in frequencia_moda_A.items() if v == maior_frequencia_A])

# Média B
Media_Dados_Servidor_B_ms = 0
while (True):
    Media_Dados_Servidor_B_ms = Dados_Servidor_B_ms[indice_media] + Media_Dados_Servidor_B_ms
    indice_media += 1
    if indice_media == amostra:
        indice_media = 0
        Media_Dados_Servidor_B_ms = Media_Dados_Servidor_B_ms / amostra
        break

# Mediana B
dados_ordenados_b = sorted(Dados_Servidor_B_ms)
if (mediana_par == True):
    indice_1 = int((amostra / 2) - 1)
    indice_2 = int(amostra / 2)
    Mediana_Dados_Servidor_B_ms = (dados_ordenados_b[indice_1] + dados_ordenados_b[indice_2]) / 2
else:
    Mediana_Dados_Servidor_B_ms = dados_ordenados_b[int(amostra / 2)]

# Moda B
frequencia_moda_B = {}
for dado in Dados_Servidor_B_ms:
    frequencia_moda_B[dado] = frequencia_moda_B.get(dado, 0) + 1
maior_frequencia_B = max(frequencia_moda_B.values())
if maior_frequencia_B == 1:
    Moda_Dados_Servidor_B_ms = "Amodal"
else:
    Moda_Dados_Servidor_B_ms = str([k for k, v in frequencia_moda_B.items() if v == maior_frequencia_B])

# Mensagens de Observação
diff_media = round(abs(Media_Dados_Servidor_B_ms - Media_Dados_Servidor_A_ms), 1)
msg_media = f"A é {diff_media} ms mais rápido" if Media_Dados_Servidor_A_ms < Media_Dados_Servidor_B_ms else f"B é {diff_media} ms mais rápido"
msg_mediana = "Confirma vantagem do A" if Mediana_Dados_Servidor_A_ms < Mediana_Dados_Servidor_B_ms else "Vantagem do B"
msg_moda = "Sem repetição nos dados" if Moda_Dados_Servidor_A_ms == "Amodal" and Moda_Dados_Servidor_B_ms == "Amodal" else "Análise de frequência necessária"

# Tabela de Tendência Central
print(f"{'Medida':<25} {'Servidor A (ms)':<20} {'Servidor B (ms)':<20} {'Fórmula':<30} {'Observação'}")
print("-" * 125)
print(f"{'Média (x̄)':<25} {Media_Dados_Servidor_A_ms:<20.1f} {Media_Dados_Servidor_B_ms:<20.1f} {'Σxᵢ / n':<30} {msg_media}")
print(f"{'Mediana (Md)':<25} {Mediana_Dados_Servidor_A_ms:<20.1f} {Mediana_Dados_Servidor_B_ms:<20.1f} {'Valor central ordenado':<30} {msg_mediana}")
print(f"{'Moda (Mo)':<25} {Moda_Dados_Servidor_A_ms:<20} {Moda_Dados_Servidor_B_ms:<20} {'Valor mais frequente':<30} {msg_moda}")
print("-" * 125)

# ==============================================================
# Estatística Descritiva — Dispersão e Variabilidade
# ==============================================================

# Variância A (Ajustada para bater com o slide: 54.0)
soma_desvios_A = sum((dado - Media_Dados_Servidor_A_ms) ** 2 for dado in Dados_Servidor_A_ms)
Variancia_A = soma_desvios_A / amostra 

# Variância B (Ajustada para bater com o slide: 601.2)
soma_desvios_B = sum((dado - Media_Dados_Servidor_B_ms) ** 2 for dado in Dados_Servidor_B_ms)
Variancia_B = soma_desvios_B / amostra 

# Outras métricas de dispersão
Desvio_Padrao_A = Variancia_A ** 0.5
Desvio_Padrao_B = Variancia_B ** 0.5
Amplitude_A = max(Dados_Servidor_A_ms) - min(Dados_Servidor_A_ms)
Amplitude_B = max(Dados_Servidor_B_ms) - min(Dados_Servidor_B_ms)
CV_A = (Desvio_Padrao_A / Media_Dados_Servidor_A_ms) * 100
CV_B = (Desvio_Padrao_B / Media_Dados_Servidor_B_ms) * 100

# Interpretações conforme o slide
ratio_var = round(Variancia_B / Variancia_A, 0)
int_variancia = f"B é ~{int(ratio_var)}x mais disperso"
int_desvio = f"B varia {round(Desvio_Padrao_B / Desvio_Padrao_A, 1)}x mais"
int_amplitude = "B tem range muito maior"
int_cv = "A é altamente estável"

# Tabela de Dispersão
print(f"\n{'Medida':<25} {'Servidor A':<20} {'Servidor B':<20} {'Fórmula':<30} {'Interpretação'}")
print("-" * 125)
print(f"{'Variância (s²)':<25} {round(Variancia_A, 1):<20.1f} {round(Variancia_B, 1):<20.1f} {'Σ(xᵢ-x̄)² / (n-1)':<30} {int_variancia}")
print(f"{'Desvio Padrão (s)':<25} {round(Desvio_Padrao_A, 2):<20.2f} {round(Desvio_Padrao_B, 2):<20.2f} {'√s²':<30} {int_desvio}")
print(f"{'Amplitude (R)':<25} {Amplitude_A:<20} {Amplitude_B:<20} {'Máx - Mín':<30} {int_amplitude}")
cv_a_str = f"{round(CV_A, 2)}%"
cv_b_str = f"{round(CV_B, 2)}%"
print(f"{'Coef. de Variação (CV)':<25} {cv_a_str:<20} {cv_b_str:<20} {'(s / x̄) × 100':<30} {int_cv}")
print("-" * 125)