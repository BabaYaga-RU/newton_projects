"""
Simulacao de Sistemas Computacionais
Atividade Pratica: Simulacao de Salarios de Profissionais de TI

Objetivo: Desenvolver um algoritmo de simulacao computacional capaz de estimar 
o salario de profissionais de TI, com base em variaveis presentes no dataset, 
atingindo acuracia minima de 75%.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')


# ========== ETAPA 1: CARREGAMENTO DOS DADOS ==========
print("=" * 70)
print("SIMULACAO DE SALARIOS DE PROFISSIONAIS DE TI")
print("=" * 70)

print("\n[1] Carregando datasets...")
try:
    df_train = pd.read_csv('train.csv')
    df_test = pd.read_csv('test.csv')
    print(f"  [OK] Dados de treino: {df_train.shape[0]} registros, {df_train.shape[1]} colunas")
    print(f"  [OK] Dados de teste: {df_test.shape[0]} registros, {df_test.shape[1]} colunas")
except FileNotFoundError:
    print("  Erro: Arquivos train.csv ou test.csv nao encontrados!")
    exit()


# ========== ETAPA 2: EXPLORAÇÃO DOS DADOS ==========
print("\n[2] Explorando dados...")
print("\nVariaveis do dataset:")
print(df_train.head())
print("\nTipos de dados:")
print(df_train.dtypes)
print("\nEstatisticas das variaveis numericas:")
print(df_train.describe())
print("\nValores ausentes:")
print(df_train.isnull().sum())


# ========== ETAPA 3: PRÉ-PROCESSAMENTO DOS DADOS ==========
print("\n[3] Pre-processamento dos dados...")

# Separar features e target
X_train = df_train.drop('salary_usd', axis=1)
y_train = df_train['salary_usd']

# Obter as mesmas colunas para teste (sem target)
X_test = df_test.drop('salary_usd', axis=1) if 'salary_usd' in df_test.columns else df_test.copy()
y_test = df_test['salary_usd'] if 'salary_usd' in df_test.columns else None

print(f"  [OK] Separadas features e target")
print(f"  [OK] Features: {list(X_train.columns)}")

# Codificar variáveis categóricas
encoders = {}
categorical_columns = X_train.select_dtypes(include=['object']).columns

print(f"\n  Colunas categoricas identificadas: {list(categorical_columns)}")

for col in categorical_columns:
    encoder = LabelEncoder()
    X_train[col] = encoder.fit_transform(X_train[col].astype(str))
    encoders[col] = encoder
    print(f"    • {col}: {len(encoder.classes_)} categorias")

# Aplicar as mesmas transformações nos dados de teste
for col in categorical_columns:
    if col in X_test.columns:
        X_test[col] = encoders[col].transform(X_test[col].astype(str))

# Tratamento de valores ausentes (se houver)
X_train = X_train.fillna(X_train.mean(numeric_only=True))
X_test = X_test.fillna(X_test.mean(numeric_only=True))

print(f"  [OK] Variaveis categoricas codificadas com sucesso")
print(f"  [OK] Dados pre-processados: {X_train.shape[0]} x {X_train.shape[1]}")


# ========== ETAPA 4: TREINAMENTO DO MODELO ==========
print("\n[4] Treinando modelo de simulacao (Random Forest)...")

modelo = RandomForestRegressor(
    n_estimators=100,
    max_depth=20,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1,
    verbose=0
)

modelo.fit(X_train, y_train)
print("  [OK] Modelo treinado com sucesso!")


# ========== ETAPA 5: AVALIACAO E SIMULACAO ==========
print("\n[5] Avaliando desempenho da simulação...")

# Simulação (previsão) nos dados de treino
salarios_simulados_train = modelo.predict(X_train)
acuracia_train = r2_score(y_train, salarios_simulados_train)

# Simulação nos dados de teste
salarios_simulados_test = modelo.predict(X_test)
if y_test is not None:
    acuracia_test = r2_score(y_test, salarios_simulados_test)
    rmse_test = np.sqrt(mean_squared_error(y_test, salarios_simulados_test))
    mae_test = mean_absolute_error(y_test, salarios_simulados_test)
else:
    acuracia_test = None
    rmse_test = None
    mae_test = None

print(f"\n  Dados de Treino:")
print(f"    • Acuracia (R2): {acuracia_train:.4f} ({acuracia_train*100:.2f}%)")

if acuracia_test is not None:
    print(f"\n  Dados de Teste:")
    print(f"    • Acuracia (R2): {acuracia_test:.4f} ({acuracia_test*100:.2f}%)")
    print(f"    • RMSE: ${rmse_test:,.2f}")
    print(f"    • MAE: ${mae_test:,.2f}")


# ========== ETAPA 6: ANALISE DE IMPORTANCIA DAS VARIAVEIS ==========
print(f"\n[6] Importancia das variaveis para predicao:")

importancia = pd.DataFrame({
    'variavel': X_train.columns,
    'importancia': modelo.feature_importances_
}).sort_values('importancia', ascending=False)

for idx, row in importancia.iterrows():
    print(f"    • {row['variavel']}: {row['importancia']:.4f}")


# ========== ETAPA 7: RELATORIO FINAL DE ACURACIA ==========
print("\n" + "=" * 70)
print("RESULTADO FINAL DA SIMULACAO")
print("=" * 70)

if acuracia_test is not None:
    acuracia_final = acuracia_test
    dados_eval = "Teste"
else:
    acuracia_final = acuracia_train
    dados_eval = "Treino"

acuracia_percentual = acuracia_final * 100

print(f"\n[METRICA] ACURACIA DA SIMULACAO SALARIAL ({dados_eval}): {acuracia_percentual:.2f}%")

if acuracia_percentual >= 75:
    print(f"\n[APROVADO] RESULTADO: APROVADO! Acuracia >= 75%")
    print(f"   O modelo esta qualificado para simulacao de salarios.")
else:
    print(f"\n[NAO APROVADO] RESULTADO: NAO ATENDEU! Acuracia < 75%")
    print(f"   Recomenda-se melhorar o modelo ou adicionar mais features.")

print("\n" + "=" * 70)


# ========== ETAPA 8: VISUALIZACOES ==========
print("\n[7] Gerando visualizacoes...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Gráfico 1: Valores Reais vs Simulados (Treino)
if y_test is not None:
    axes[0, 0].scatter(y_test, salarios_simulados_test, alpha=0.6, color='blue', edgecolor='black')
    axes[0, 0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    axes[0, 0].set_xlabel('Salarios Reais (USD)', fontsize=11)
    axes[0, 0].set_ylabel('Salarios Simulados (USD)', fontsize=11)
    axes[0, 0].set_title(f'Valores Reais vs Simulados (Teste)\nR2 = {acuracia_test:.4f}', fontsize=12, fontweight='bold')
    axes[0, 0].grid(True, alpha=0.3)

# Grafico 2: Importancia das Variaveis
axes[0, 1].barh(importancia['variavel'], importancia['importancia'], color='steelblue')
axes[0, 1].set_xlabel('Importancia', fontsize=11)
axes[0, 1].set_title('Importancia das Variaveis', fontsize=12, fontweight='bold')
axes[0, 1].grid(True, alpha=0.3, axis='x')

# Grafico 3: Distribuicao dos Salarios
axes[1, 0].hist(y_train, bins=30, alpha=0.7, color='green', label='Reais', edgecolor='black')
if y_test is not None:
    axes[1, 0].hist(salarios_simulados_test, bins=30, alpha=0.7, color='orange', label='Simulados', edgecolor='black')
axes[1, 0].set_xlabel('Salario (USD)', fontsize=11)
axes[1, 0].set_ylabel('Frequencia', fontsize=11)
axes[1, 0].set_title('Distribuicao de Salarios', fontsize=12, fontweight='bold')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# Grafico 4: Acuracia
categorias = ['Treino', 'Teste'] if acuracia_test is not None else ['Treino']
acuracias = [acuracia_train*100] if acuracia_test is None else [acuracia_train*100, acuracia_test*100]
cores = ['green' if acc >= 75 else 'red' for acc in acuracias]

axes[1, 1].bar(categorias, acuracias, color=cores, edgecolor='black', linewidth=2)
axes[1, 1].axhline(y=75, color='red', linestyle='--', linewidth=2, label='Limite Minimo (75%)') 
axes[1, 1].set_ylabel('Acurácia (%)', fontsize=11)
axes[1, 1].set_title('Acurácia do Modelo', fontsize=12, fontweight='bold')
axes[1, 1].set_ylim(0, 100)
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3, axis='y')

for i, v in enumerate(acuracias):
    axes[1, 1].text(i, v + 2, f'{v:.2f}%', ha='center', fontweight='bold', fontsize=11)

plt.tight_layout()
plt.savefig('Simulacao_Salarios_Analise.png', dpi=300, bbox_inches='tight')
print("  [OK] Graficos salvos em: Simulacao_Salarios_Analise.png")
plt.close()


# ========== ETAPA 9: RESULTADOS FINAIS NO TERMINAL ==========
print("\n[8] Resultados finais da simulacao:")
print("=" * 70)
print(f"Tamanho do dataset de treino: {df_train.shape[0]} registros, {df_train.shape[1]} colunas")
print(f"Tamanho do dataset de teste: {df_test.shape[0]} registros, {df_test.shape[1]} colunas")
print(f"Variaveis categoricas codificadas: {list(categorical_columns)}")
print("=" * 70)
print(f"R2 Treino: {acuracia_train:.4f} ({acuracia_train*100:.2f}%)")
if acuracia_test is not None:
    print(f"R2 Teste: {acuracia_test:.4f} ({acuracia_test*100:.2f}%)")
    print(f"RMSE Teste: ${rmse_test:,.2f}")
    print(f"MAE Teste: ${mae_test:,.2f}")
print("=" * 70)
print("Top 5 variaveis por importancia:")
for rank, (_, row) in enumerate(importancia.head(5).iterrows(), start=1):
    print(f"  {rank}. {row['variavel']}: {row['importancia']:.4f}")
print("=" * 70)
if acuracia_percentual >= 75:
    print("[APROVADO] O modelo atingiu a acuracia minima de 75%.")
else:
    print("[NAO APROVADO] O modelo nao atingiu a acuracia minima de 75%.")
print("\n[SUCESSO] Simulacao concluida com sucesso!")
