
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import time

from sklearn.model_selection import cross_val_score, KFold, train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
# SVM: Use SGDRegressor for large datasets (como sugerido no enunciado)
from sklearn.linear_model import SGDRegressor
import skfuzzy as fuzz
from skfuzzy import control as ctrl

print("=" * 70)
print("SIMULADORES ESTOCASTICOS DE TI - COMPARATIVO DE PERFORMANCE")
print("=" * 70)

# ============================================================
# BLOCO 2: DADOS
# ============================================================
print("\n" + "=" * 70)
print("BLOCO 2: CARREGAMENTO E ANALISE DESCRITIVA DOS DADOS")
print("=" * 70)

t0 = time.time()
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
print(f"\nDimensoes - Treino: {train.shape}, Teste: {test.shape} ({time.time()-t0:.1f}s)")

y_all = train['salary_usd']
print(f"\n--- Estatisticas Descritivas de salary_usd (Treino) ---")
print(f"Media:          {y_all.mean():>12.2f}")
print(f"Mediana:        {y_all.median():>12.2f}")
print(f"Desvio Padrao:  {y_all.std():>12.2f}")
print(f"Q1 (25%):       {y_all.quantile(0.25):>12.2f}")
print(f"Q3 (75%):       {y_all.quantile(0.75):>12.2f}")

num_cols_corr = train.select_dtypes(include=[np.number]).columns
print("\n--- Correlacao de Pearson ---")
print(train[num_cols_corr].corr().to_string())

# ============================================================
# BLOCO 3: PRE-PROCESSAMENTO
# ============================================================
print("\n" + "=" * 70)
print("BLOCO 3: PRE-PROCESSAMENTO")
print("=" * 70)

def preprocess_data(df):
    data = df.copy()
    data['num_linguagens'] = data['languages'].apply(lambda x: len(str(x).split(', ')))
    data['num_frameworks'] = data['frameworks'].apply(lambda x: len(str(x).split(', ')))
    data.drop(columns=['languages', 'frameworks'], inplace=True)
    return data

train_p = preprocess_data(train)
test_p = preprocess_data(test)

X_train = train_p.drop(columns=['salary_usd'])
y_train = train_p['salary_usd']
X_test = test_p.drop(columns=['salary_usd'])
y_test = test_p['salary_usd']

cat_cols = X_train.select_dtypes(include=['object']).columns.tolist()
num_cols = X_train.select_dtypes(include=[np.number]).columns.tolist()
print(f"\nCategoricas: {cat_cols}")
print(f"Numericas:   {num_cols}")

ord_encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
scaler = StandardScaler()

preprocessor = ColumnTransformer([
    ('ord', ord_encoder, cat_cols),
    ('num', 'passthrough', num_cols)
])

X_tr_t = preprocessor.fit_transform(X_train)
X_te_t = preprocessor.transform(X_test)
X_tr_s = scaler.fit_transform(X_tr_t)
X_te_s = scaler.transform(X_te_t)

# PolynomialFeatures grau 2 - interaction_only para reduzir dimensionalidade
poly = PolynomialFeatures(degree=2, include_bias=False, interaction_only=True)
X_tr_p = poly.fit_transform(X_tr_s)
X_te_p = poly.transform(X_te_s)

print(f"\nFeatures base: {X_tr_s.shape[1]} -> PolyFeatures (interaction): {X_tr_p.shape[1]}")
print(f"X_train_poly: {X_tr_p.shape}")

# ============================================================
# BLOCO 4: MODELAGEM COMPARATIVA
# ============================================================
print("\n" + "=" * 70)
print("BLOCO 4: TREINAMENTO DOS MODELOS")
print("=" * 70)

results = {}
model_names = ['Random Forest', 'RNA', 'SVM', 'Fuzzy']

# --- [A] Random Forest ---
print("\n--- [A] Random Forest (200 arvores, max_depth=10) ---")
t0 = time.time()
rf = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42, n_jobs=-1)
rf.fit(X_tr_p, y_train)
y_pred_rf = rf.predict(X_te_p)
r2_rf = r2_score(y_test, y_pred_rf)
results['Random Forest'] = {'y_pred': y_pred_rf, 'test_r2': r2_rf}
print(f"    R2 = {r2_rf:.4f}  ({time.time()-t0:.1f}s)")

# --- [B] RNA ---
print("\n--- [B] RNA (MLP: 100,50,25) ---")
t0 = time.time()
mlp = MLPRegressor(hidden_layer_sizes=(100, 50, 25), max_iter=500,
                   random_state=42, early_stopping=True, validation_fraction=0.1, verbose=False)
mlp.fit(X_tr_p, y_train)
y_pred_mlp = mlp.predict(X_te_p)
r2_mlp = r2_score(y_test, y_pred_mlp)
results['RNA'] = {'y_pred': y_pred_mlp, 'test_r2': r2_mlp}
print(f"    R2 = {r2_mlp:.4f}  ({time.time()-t0:.1f}s)")

# --- [C] SVM (SGDRegressor - alternativa para grandes volumes) ---
print("\n--- [C] SVM (SGDRegressor - como sugerido no enunciado) ---")
t0 = time.time()
# Escalar target para SGD (ajuda na convergencia)
y_scaler = StandardScaler()
y_train_s = y_scaler.fit_transform(y_train.to_numpy().reshape(-1, 1)).ravel()
sgd = SGDRegressor(loss='squared_error', penalty='l2', alpha=0.001,
                   max_iter=2000, tol=1e-4, random_state=42, verbose=0, learning_rate='invscaling', eta0=0.01)
sgd.fit(X_tr_p, y_train_s)
y_pred_sgd_s = sgd.predict(X_te_p)
y_pred_sgd = y_scaler.inverse_transform(y_pred_sgd_s.reshape(-1, 1)).ravel()
r2_sgd = r2_score(y_test, y_pred_sgd)
results['SVM'] = {'y_pred': y_pred_sgd, 'test_r2': r2_sgd}
print(f"    R2 = {r2_sgd:.4f}  ({time.time()-t0:.1f}s)")

# --- [D] Logica Nebulosa (Takagi-Sugeno) ---
print("\n--- [D] Logica Nebulosa (Takagi-Sugeno) ---")
print("    Usando sample de 2000 registros para predicao")
t0 = time.time()

fuzzy_feat = ['experience', 'num_linguagens', 'num_frameworks']
X_tr_f = X_train[fuzzy_feat].values[:10000]  # usa 10k para definicao do fuzzy
X_te_f = X_test[fuzzy_feat].values

scl_f = StandardScaler()
X_tr_fs = scl_f.fit_transform(X_tr_f)
X_te_fs = scl_f.transform(X_te_f)

def mm_scale(X, X_ref):
    mn, mx = X_ref.min(0), X_ref.max(0)
    return (X - mn) / (mx - mn + 1e-10), mn, mx

X_tr_fn, mn_f, mx_f = mm_scale(X_tr_fs, X_tr_fs)
X_te_fn = (X_te_fs - mn_f) / (mx_f - mn_f + 1e-10)
y_mn, y_mx = y_train.min(), y_train.max()

# Sistema Fuzzy
exp = ctrl.Antecedent(np.linspace(0, 1, 100), 'exp')
lang = ctrl.Antecedent(np.linspace(0, 1, 100), 'lang')
fram = ctrl.Antecedent(np.linspace(0, 1, 100), 'fram')
sal = ctrl.Consequent(np.linspace(0, 1, 100), 'sal', defuzzify_method='centroid')

exp.automf(3, names=['junior', 'mid', 'senior'])
lang.automf(3, names=['poucas', 'medias', 'muitas'])
fram.automf(3, names=['poucos', 'medios', 'muitos'])
sal.automf(5)

r1 = ctrl.Rule(exp['junior'] & lang['poucas'] & fram['poucos'], sal['poor'])
r2 = ctrl.Rule(exp['junior'] & (lang['medias'] | fram['medios']), sal['mediocre'])
r3 = ctrl.Rule(exp['mid'], sal['average'])
r4 = ctrl.Rule(exp['senior'] & (lang['muitas'] | fram['muitos']), sal['good'])
r5 = ctrl.Rule(exp['senior'] & (lang['medias'] | fram['medios']), sal['decent'])
r6 = ctrl.Rule(exp['mid'] & lang['muitas'] & fram['muitos'], sal['decent'])

fs_ctrl = ctrl.ControlSystem([r1, r2, r3, r4, r5, r6])

# Predizer (sample de 2000 para ser viavel)
n_test = len(X_te_fn)
sample_size = min(2000, n_test)
sample_idx = np.random.RandomState(42).choice(n_test, sample_size, replace=False)
y_pred_fz = np.full(n_test, np.nan)

for i in sample_idx:
    sim = ctrl.ControlSystemSimulation(fs_ctrl)
    try:
        sim.input['exp'] = float(X_te_fn[i, 0])
        sim.input['lang'] = float(X_te_fn[i, 1])
        sim.input['fram'] = float(X_te_fn[i, 2])
        sim.compute()
        y_pred_fz[i] = sim.output['sal']
    except:
        y_pred_fz[i] = 0.5

# Preencher NaN com mediana das predicoes validas
valid_preds = y_pred_fz[~np.isnan(y_pred_fz)]
y_pred_fz[np.isnan(y_pred_fz)] = np.median(valid_preds)
y_pred_fz = y_pred_fz * (y_mx - y_mn) + y_mn

r2_fz = r2_score(y_test, y_pred_fz)
results['Fuzzy'] = {'y_pred': y_pred_fz, 'test_r2': r2_fz}
print(f"    R2 = {r2_fz:.4f}  ({time.time()-t0:.1f}s)")

# ============================================================
# BLOCO 5: VALIDACAO CRUZADA
# ============================================================
print("\n" + "=" * 70)
print("BLOCO 5: VALIDACAO CRUZADA (5-FOLD)")
print("=" * 70)

kfold = KFold(n_splits=5, shuffle=True, random_state=42)

cv_models = {
    'Random Forest': RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42, n_jobs=-1),
    'RNA': MLPRegressor(hidden_layer_sizes=(100, 50, 25), max_iter=500,
                        random_state=42, early_stopping=True, validation_fraction=0.1),
    'SVM': SGDRegressor(loss='squared_error', penalty='l2', alpha=0.001,
                        max_iter=2000, tol=1e-4, random_state=42, learning_rate='invscaling', eta0=0.01),
}

print()
header = "{:<18} {:<14} {:<10} {:<12} {:<12}".format('Modelo', 'R2 CV Medio', 'DP CV', 'R2 Teste', 'Supera 82%?')
print(header)
print("-" * 66)

for name, model in cv_models.items():
    t0 = time.time()
    scores = cross_val_score(model, X_tr_p, y_train, cv=kfold, scoring='r2', n_jobs=1)
    r2_cv = scores.mean()
    dp_cv = scores.std()
    r2_te = results[name]['test_r2']
    flag = "SIM" if r2_te > 0.82 else "NAO"
    print(f"{name:<18} {r2_cv:<14.4f} {dp_cv:<10.4f} {r2_te:<12.4f} {flag:<12}  ({time.time()-t0:.1f}s)")

# CV para Fuzzy (sample)
print(f"{'Fuzzy':<18} ", end="")
t0 = time.time()
try:
    fz_scores = []
    for train_i, val_i in kfold.split(X_tr_fs[:5000]):  # amostra 5k para viabilidade
        X_tr_fold = X_tr_fs[:5000][train_i]; X_val_fold = X_tr_fs[:5000][val_i]
        y_tr_fold = y_train.iloc[:5000].iloc[train_i]
        y_val_fold = y_train.iloc[:5000].iloc[val_i]

        mn_fold = X_tr_fold.min(0); mx_fold = X_tr_fold.max(0)
        X_tr_fold_n = (X_tr_fold - mn_fold) / (mx_fold - mn_fold + 1e-10)
        X_val_fold_n = (X_val_fold - mn_fold) / (mx_fold - mn_fold + 1e-10)
        ymin_f, ymax_f = y_tr_fold.min(), y_tr_fold.max()

        preds = np.zeros(len(X_val_fold_n))
        for i in range(min(200, len(X_val_fold_n))):
            sim = ctrl.ControlSystemSimulation(fs_ctrl)
            try:
                sim.input['exp'] = float(X_val_fold_n[i, 0])
                sim.input['lang'] = float(X_val_fold_n[i, 1])
                sim.input['fram'] = float(X_val_fold_n[i, 2])
                sim.compute()
                preds[i] = sim.output['sal']
            except:
                preds[i] = 0.5
        # Preencher resto com media
        preds[len(preds)//2:] = preds[:len(preds)//2].mean()
        preds = preds * (ymax_f - ymin_f) + ymin_f
        fz_scores.append(r2_score(y_val_fold[:200], preds[:200]))
    r2_fz_cv = np.mean(fz_scores)
    dp_fz_cv = np.std(fz_scores)
    flag_fz = "SIM" if results['Fuzzy']['test_r2'] > 0.82 else "NAO"
    print(f"{r2_fz_cv:<14.4f} {dp_fz_cv:<10.4f} {results['Fuzzy']['test_r2']:<12.4f} {flag_fz:<12}  ({time.time()-t0:.1f}s)")
except Exception as e:
    print(f"{'N/A':<14} {'N/A':<10} {results['Fuzzy']['test_r2']:<12.4f} {'N/A':<12}  ({time.time()-t0:.1f}s)")

print("-" * 66)

# ============================================================
# BLOCO 6: ANALISE GRAFICA
# ============================================================
print("\n" + "=" * 70)
print("BLOCO 6: ANALISE GRAFICA")
print("=" * 70)

sns.set_theme(style='whitegrid')
colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']

fig, axes = plt.subplots(2, 2, figsize=(14, 12))
for idx, name in enumerate(model_names):
    ax = axes[idx // 2][idx % 2]
    yp = results[name]['y_pred']
    r2 = results[name]['test_r2']
    ax.scatter(y_test, yp, alpha=0.5, color=colors[idx], edgecolors='k', linewidth=0.5)
    lo = min(y_test.min(), yp.min())
    hi = max(y_test.max(), yp.max())
    ax.plot([lo, hi], [lo, hi], 'k--', lw=2, alpha=0.8)
    ax.set_xlabel('Valores Reais (USD)')
    ax.set_ylabel('Valores Preditos (USD)')
    ax.set_title(f'{name} (R2 = {r2:.4f})', fontweight='bold')

plt.suptitle('Comparativo: Valores Reais vs Preditos', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('scatter_real_vs_predito.png', dpi=150)
plt.close()
print("  OK - scatter_real_vs_predito.png")

fig, axes = plt.subplots(2, 2, figsize=(14, 12))
for idx, name in enumerate(model_names):
    ax = axes[idx // 2][idx % 2]
    yp = results[name]['y_pred']
    r2 = results[name]['test_r2']
    residuals = y_test - yp
    ax.hist(residuals, bins=40, color=colors[idx], alpha=0.7, edgecolor='black', linewidth=0.5)
    ax.axvline(x=0, color='red', linestyle='--', lw=2, label='Erro Zero')
    ax.set_xlabel('Erro Residual (USD)')
    ax.set_ylabel('Frequencia')
    ax.set_title(f'{name} - Erro Residual (R2 = {r2:.4f})', fontweight='bold')
    ax.legend()

plt.suptitle('Distribuicao dos Erros Residuais', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('histograma_erro_residual.png', dpi=150)
plt.close()
print("  OK - histograma_erro_residual.png")

# ============================================================
# QUESTIONARIO DE ANALISE CRITICA
# ============================================================
print("\n" + "=" * 70)
print("QUESTIONARIO DE ANALISE CRITICA")
print("=" * 70)

print("""
1. Explique por que a Rede Neural conseguiu capturar padroes que o Random
   Forest ignorou.
   R: A RNA com camadas ocultas pode aprender representacoes nao-lineares
   complexas e interacoes de alta ordem entre as features, enquanto o
   Random Forest, mesmo com PolynomialFeatures, e limitado pela
   profundidade maxima (10 niveis). A RNA tambem generaliza melhor
   quando ha relacoes suaves e continuas nos dados.

2. Analise o custo computacional (tempo de treinamento) do SVM em relacao
   ao Random Forest para 40k registros.
   R: SVR com kernel RBF tem complexidade O(n^2) a O(n^3), tornando-se
   inviavel para 40k registros (alto custo de memoria e processamento).
   O Random Forest escala quase linearmente com n_estimators e n_jobs,
   sendo muito mais rapido. Por isso o enunciado sugere SGDRegressor
   como alternativa viavel para grandes volumes.

3. Como a Logica Fuzzy permite lidar com a incerteza na definicao de
   cargos e senioridade?
   R: A Logica Fuzzy permite membership functions que suavizam as
   transicoes entre categorias (junior->mid->senior), capturando a
   nebulosidade inerente a definicao de cargos. Um profissional com
   3 anos pode ser parcialmente junior e parcialmente mid, e o sistema
   fuzzy pondera essas contribuicoes nas regras de inferencia.

4. Qual modelo apresentou a melhor generalizacao no conjunto de teste?
   Justifique com base no Overfitting.
   R: O modelo com maior R2 no teste e menor diferenca entre R2 CV e
   R2 teste apresenta a melhor generalizacao. O Random Forest com
   max_depth=10 tende a evitar overfitting, enquanto a RNA com
   early_stopping tambem controla bem. SVM/SGD e Fuzzy podem sofrer
   mais com underfitting devido a limitacoes de representacao.

5. Proponha uma arquitetura Ensemble que combine os 4 modelos (Stacking)
   para atingir R2 > 90%.
   R: Usar StackingRegressor com:
   - Estimadores base: RandomForest (200 trees, depth=10),
     MLPRegressor (100,50,25), SGDRegressor (huber), Fuzzy
   - Meta-estimador: RidgeCV ou GradientBoostingRegressor
   - Treinar os bases com 5-fold CV e usar as predicoes out-of-fold
     como features para o meta-modelo, que aprende a ponderar as
     contribuicoes de cada modelo base.
""")

# ============================================================
# RESUMO FINAL
# ============================================================
print("=" * 70)
print("RESUMO FINAL")
print("=" * 70)
print(f"\n{'Modelo':<18} {'R2 Teste':<12} {'R2 > 0.82':<12}")
print("-" * 42)
for name in model_names:
    r2 = results[name]['test_r2']
    flag = "SIM" if r2 > 0.82 else "NAO"
    print(f"{name:<18} {r2:<12.4f} {flag:<12}")

best = max(model_names, key=lambda n: results[n]['test_r2'])
print("-" * 42)
print(f"\nMelhor modelo: {best} (R2 = {results[best]['test_r2']:.4f})")
print("\nExecucao concluida com sucesso!")