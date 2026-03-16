

# Importar as bibliotecas e configurar o notebook
import pandas as pd
import numpy as np

print("Bibliotecas carregadas com sucesso!")
print("Versão do NumPy:", np.__version__)
print('Setup completo!')

# Dados dos servidores (convertendo para listas para trabalhar com numpy/pandas)
tempo_resposta_servidor_a = [120, 135, 128, 142, 119, 130, 125, 138, 122, 131]
tempo_resposta_servidor_b = [115, 160, 118, 175, 112, 158, 120, 170, 113, 165]

# Criar DataFrames para análise
df_servidor_a = pd.DataFrame({'tempo_resposta_ms': tempo_resposta_servidor_a, 'servidor': 'A'})
df_servidor_b = pd.DataFrame({'tempo_resposta_ms': tempo_resposta_servidor_b, 'servidor': 'B'})
df_completo = pd.concat([df_servidor_a, df_servidor_b], ignore_index=True)

print("Dados carregados com sucesso!")
print("Dataset completo:")
print(df_completo.head(10))

# Estatística Descritiva - Tendência Central usando NumPy e Pandas
print("\n" + "="*60)
print("ESTATÍSTICA DESCRITIVA - TENDÊNCIA CENTRAL")
print("="*60)

# Média usando NumPy
media_servidor_a = np.mean(tempo_resposta_servidor_a)
media_servidor_b = np.mean(tempo_resposta_servidor_b)

print(f'Média (x̄) Servidor A (ms): {media_servidor_a:.2f}')
print(f'Média (x̄) Servidor B (ms): {media_servidor_b:.2f}')

if media_servidor_a < media_servidor_b:
    diferenca_media = media_servidor_b - media_servidor_a
    print(f'Observação: O Servidor A é {diferenca_media:.2f}ms mais rápido que o Servidor B')
else:
    diferenca_media = media_servidor_a - media_servidor_b
    print(f'Observação: O Servidor B é {diferenca_media:.2f}ms mais rápido que o Servidor A')

# Mediana usando NumPy
mediana_servidor_a = np.median(tempo_resposta_servidor_a)
mediana_servidor_b = np.median(tempo_resposta_servidor_b)

print(f'\nMediana (Md) Servidor A (ms): {mediana_servidor_a:.2f}')
print(f'Mediana (Md) Servidor B (ms): {mediana_servidor_b:.2f}')

# Moda usando scipy (mais robusto que numpy para moda)
from scipy import stats
moda_servidor_a = stats.mode(tempo_resposta_servidor_a, keepdims=True)
moda_servidor_b = stats.mode(tempo_resposta_servidor_b, keepdims=True)

print(f'Moda Servidor A (ms): {moda_servidor_a.mode[0]} (frequência: {moda_servidor_a.count[0]})')
print(f'Moda Servidor B (ms): {moda_servidor_b.mode[0]} (frequência: {moda_servidor_b.count[0]})')

# Estatística Descritiva - Dispersão
print("\n" + "="*60)
print("ESTATÍSTICA DESCRITIVA - DISPERÇÃO")
print("="*60)

# Variância e Desvio Padrão usando NumPy
variancia_servidor_a = np.var(tempo_resposta_servidor_a, ddof=1)  # ddof=1 para amostra
variancia_servidor_b = np.var(tempo_resposta_servidor_b, ddof=1)
desvio_padrao_servidor_a = np.std(tempo_resposta_servidor_a, ddof=1)
desvio_padrao_servidor_b = np.std(tempo_resposta_servidor_b, ddof=1)

print(f'Variância Servidor A: {variancia_servidor_a:.2f}')
print(f'Variância Servidor B: {variancia_servidor_b:.2f}')
print(f'Desvio Padrão Servidor A (ms): {desvio_padrao_servidor_a:.2f}')
print(f'Desvio Padrão Servidor B (ms): {desvio_padrao_servidor_b:.2f}')

# Amplitude (Range)
amplitude_servidor_a = np.max(tempo_resposta_servidor_a) - np.min(tempo_resposta_servidor_a)
amplitude_servidor_b = np.max(tempo_resposta_servidor_b) - np.min(tempo_resposta_servidor_b)

print(f'Amplitude Servidor A (ms): {amplitude_servidor_a}')
print(f'Amplitude Servidor B (ms): {amplitude_servidor_b}')

# Coeficiente de Variação
coeficiente_variacao_servidor_a = (desvio_padrao_servidor_a / media_servidor_a) * 100
coeficiente_variacao_servidor_b = (desvio_padrao_servidor_b / media_servidor_b) * 100

print(f'Coeficiente de Variação Servidor A (%): {coeficiente_variacao_servidor_a:.2f}%')
print(f'Coeficiente de Variação Servidor B (%): {coeficiente_variacao_servidor_b:.2f}%')

# Quartis e IQR usando NumPy
q1_servidor_a, q3_servidor_a = np.percentile(tempo_resposta_servidor_a, [25, 75])
q1_servidor_b, q3_servidor_b = np.percentile(tempo_resposta_servidor_b, [25, 75])
iqr_servidor_a = q3_servidor_a - q1_servidor_a
iqr_servidor_b = q3_servidor_b - q1_servidor_b

print(f'Q1 Servidor A (ms): {q1_servidor_a:.2f}')
print(f'Q3 Servidor A (ms): {q3_servidor_a:.2f}')
print(f'IQR Servidor A (ms): {iqr_servidor_a:.2f}')
print(f'Q1 Servidor B (ms): {q1_servidor_b:.2f}')
print(f'Q3 Servidor B (ms): {q3_servidor_b:.2f}')
print(f'IQR Servidor B (ms): {iqr_servidor_b:.2f}')

# Boxplot e Interpretação
print("\n" + "="*60)
print("BOXPLOT E INTERPRETAÇÃO")
print("="*60)

# Identificar outliers usando método do IQR
def identificar_outliers(dados, q1, q3, iqr):
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    outliers = [x for x in dados if x < limite_inferior or x > limite_superior]
    return outliers, limite_inferior, limite_superior

outliers_servidor_a, limite_inferior_a, limite_superior_a = identificar_outliers(tempo_resposta_servidor_a, q1_servidor_a, q3_servidor_a, iqr_servidor_a)
outliers_servidor_b, limite_inferior_b, limite_superior_b = identificar_outliers(tempo_resposta_servidor_b, q1_servidor_b, q3_servidor_b, iqr_servidor_b)

print(f'Outliers Servidor A: {outliers_servidor_a}')
print(f'Outliers Servidor B: {outliers_servidor_b}')
print(f'Limite inferior Servidor A: {limite_inferior_a:.2f}')
print(f'Limite superior Servidor A: {limite_superior_a:.2f}')
print(f'Limite inferior Servidor B: {limite_inferior_b:.2f}')
print(f'Limite superior Servidor B: {limite_superior_b:.2f}')

# Conclusões e Recomendações
print("\n" + "="*60)
print("CONCLUSÕES E RECOMENDAÇÕES")
print("="*60)

print("\nAnálise Comparativa:")
print(f"1. Desempenho Médio:")
print(f"   - Servidor A: {media_servidor_a:.2f}ms")
print(f"   - Servidor B: {media_servidor_b:.2f}ms")
if media_servidor_a < media_servidor_b:
    print(f"   - O Servidor A é {((media_servidor_b-media_servidor_a)/media_servidor_b*100):.1f}% mais rápido que o Servidor B")
else:
    print(f"   - O Servidor B é {((media_servidor_a-media_servidor_b)/media_servidor_a*100):.1f}% mais rápido que o Servidor A")

print(f"\n2. Estabilidade (Variabilidade):")
print(f"   - Desvio Padrão A: {desvio_padrao_servidor_a:.2f}ms (CV: {coeficiente_variacao_servidor_a:.2f}%)")
print(f"   - Desvio Padrão B: {desvio_padrao_servidor_b:.2f}ms (CV: {coeficiente_variacao_servidor_b:.2f}%)")
if coeficiente_variacao_servidor_a < coeficiente_variacao_servidor_b:
    print(f"   - O Servidor A é mais estável (menor variabilidade)")
else:
    print(f"   - O Servidor B é mais estável (menor variabilidade)")

print(f"\n3. Presença de Outliers:")
print(f"   - Servidor A tem {len(outliers_servidor_a)} outlier(s): {outliers_servidor_a}")
print(f"   - Servidor B tem {len(outliers_servidor_b)} outlier(s): {outliers_servidor_b}")

print(f"\n4. Robustez (Mediana vs Média):")
print(f"   - Servidor A: Média = {media_servidor_a:.2f}ms, Mediana = {mediana_servidor_a:.2f}ms")
print(f"   - Servidor B: Média = {media_servidor_b:.2f}ms, Mediana = {mediana_servidor_b:.2f}ms")

# Recomendação Final
if media_servidor_a < media_servidor_b and coeficiente_variacao_servidor_a < coeficiente_variacao_servidor_b and len(outliers_servidor_a) <= len(outliers_servidor_b):
    recomendacao_final = "SERVIDOR A"
    motivo_recomendacao = "Melhor desempenho médio, maior estabilidade e menor quantidade de outliers"
elif media_servidor_b < media_servidor_a and coeficiente_variacao_servidor_b < coeficiente_variacao_servidor_a and len(outliers_servidor_b) <= len(outliers_servidor_a):
    recomendacao_final = "SERVIDOR B"
    motivo_recomendacao = "Melhor desempenho médio, maior estabilidade e menor quantidade de outliers"
else:
    if media_servidor_a < media_servidor_b:
        recomendacao_final = "SERVIDOR A"
        motivo_recomendacao = "Melhor desempenho médio, apesar de maior variabilidade"
    else:
        recomendacao_final = "SERVIDOR B"
        motivo_recomendacao = "Melhor desempenho médio, apesar de maior variabilidade"

print(f"\n5. RECOMENDAÇÃO FINAL PARA PRODUÇÃO:")
print(f"   SERVIDOR RECOMENDADO: {recomendacao_final}")
print(f"   MOTIVO: {motivo_recomendacao}")

print(f"\n6. Observações Adicionais:")
print(f"   - O Servidor A apresenta tempos de resposta mais consistentes")
print(f"   - O Servidor B tem picos de latência que podem comprometer a experiência do usuário")
print(f"   - Para ambientes críticos, a estabilidade do Servidor A é preferível")

print("\n" + "="*60)
print("ANÁLISE CONCLUÍDA COM SUCESSO!")
print("="*60)
