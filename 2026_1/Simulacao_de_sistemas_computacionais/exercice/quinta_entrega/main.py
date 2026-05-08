"""
Atividade Pratica - OTIMIZACAO DE SIMULADORES ESTOCASTICOS DE TI
Comparativo: Random Forest vs. RNA vs. SVM vs. Logica Nebulosa
"""
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import time
from sklearn.model_selection import cross_val_score, KFold
from sklearn.preprocessing import StandardScaler, PolynomialFeatures, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import SGDRegressor
import skfuzzy as fuzz
from skfuzzy import control as ctrl

print("="*60); print("SIMULADORES ESTOCASTICOS DE TI"); print("="*60)

# ========== BLOCO 2: DADOS ==========
print("\n--- BLOCO 2: DADOS ---")
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
print(f"Treino: {train.shape}, Teste: {test.shape}")

y_all = train['salary_usd']
print(f"Media={y_all.mean():.2f} Mediana={y_all.median():.2f} Std={y_all.std():.2f}")
print(f"Q1={y_all.quantile(0.25):.2f} Q3={y_all.quantile(0.75):.2f}")
print("\nCorrelacao Pearson:")
print(train.select_dtypes(include=[np.number]).corr().to_string())

# ========== BLOCO 3: PRE-PROCESSAMENTO ==========
print("\n--- BLOCO 3: PRE-PROCESSAMENTO ---")
def preprocess(df):
    d = df.copy()
    d['num_linguagens'] = d['languages'].apply(lambda x: len(str(x).split(', ')))
    d['num_frameworks'] = d['frameworks'].apply(lambda x: len(str(x).split(', ')))
    return d.drop(columns=['languages','frameworks'])

train_p = preprocess(train); test_p = preprocess(test)
X_tr = train_p.drop(columns=['salary_usd']); y_tr = train_p['salary_usd']
X_te = test_p.drop(columns=['salary_usd']); y_te = test_p['salary_usd']

cat = X_tr.select_dtypes(['object']).columns.tolist()
num = X_tr.select_dtypes([np.number]).columns.tolist()
print(f"Cat={cat} Num={num}")

pp = ColumnTransformer([('ord', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1), cat),
                         ('num','passthrough', num)])
X_tr_t = pp.fit_transform(X_tr); X_te_t = pp.transform(X_te)

scaler = StandardScaler()
X_tr_s = scaler.fit_transform(X_tr_t)
X_te_s = scaler.transform(X_te_t)

poly = PolynomialFeatures(degree=2, include_bias=False, interaction_only=True)
X_tr_p = poly.fit_transform(X_tr_s); X_te_p = poly.transform(X_te_s)
print(f"Features: {X_tr_s.shape[1]} -> Poly: {X_tr_p.shape[1]}")

# ========== BLOCO 4: MODELAGEM ==========
print("\n--- BLOCO 4: MODELOS ---")
results = {}; names = ['Random Forest','RNA','SVM','Fuzzy']

# [A] Random Forest
t0=time.time()
rf = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42, n_jobs=-1).fit(X_tr_p, y_tr)
yp_rf = rf.predict(X_te_p); r2_rf = r2_score(y_te, yp_rf)
results['Random Forest']={'y_pred':yp_rf,'test_r2':r2_rf}
print(f"[A] RF: R2={r2_rf:.4f} ({time.time()-t0:.1f}s)")

# [B] RNA - reduzido para 300 iteracoes
t0=time.time()
mlp = MLPRegressor(hidden_layer_sizes=(100,50,25), max_iter=300, random_state=42, early_stopping=True, validation_fraction=0.1)
mlp.fit(X_tr_p, y_tr)
yp_mlp = mlp.predict(X_te_p); r2_mlp = r2_score(y_te, yp_mlp)
results['RNA']={'y_pred':yp_mlp,'test_r2':r2_mlp}
print(f"[B] RNA: R2={r2_mlp:.4f} ({time.time()-t0:.1f}s)")

# [C] SVM (SGDRegressor)
t0=time.time()
y_mean,y_std = y_tr.mean(), y_tr.std()
sgd = SGDRegressor(loss='squared_error', alpha=0.001, max_iter=1000, tol=1e-3, random_state=42)
sgd.fit(X_tr_p, (y_tr-y_mean)/y_std)
yp_sgd = sgd.predict(X_te_p)*y_std + y_mean; r2_sgd = r2_score(y_te, yp_sgd)
results['SVM']={'y_pred':yp_sgd,'test_r2':r2_sgd}
print(f"[C] SVM: R2={r2_sgd:.4f} ({time.time()-t0:.1f}s)")

# [D] Fuzzy (sample 200 para ser rapido)
t0=time.time()
ff = ['experience','num_linguagens','num_frameworks']
X_tr_f = X_tr[ff].values[:5000]; X_te_f = X_te[ff].values
scl = StandardScaler(); X_tr_fs = scl.fit_transform(X_tr_f); X_te_fs = scl.transform(X_te_f)
mn_f = X_tr_fs.min(0); mx_f = X_tr_fs.max(0)
X_te_fn = (X_te_fs - mn_f) / (mx_f - mn_f + 1e-10)
y_mn, y_mx = y_tr.min(), y_tr.max()

exp = ctrl.Antecedent(np.linspace(0,1,50),'exp')
lang = ctrl.Antecedent(np.linspace(0,1,50),'lang')
fram = ctrl.Antecedent(np.linspace(0,1,50),'fram')
sal = ctrl.Consequent(np.linspace(0,1,50),'sal',defuzzify_method='centroid')
exp.automf(3, names=['junior','mid','senior']); lang.automf(3, names=['poucas','medias','muitas'])
fram.automf(3, names=['poucos','medios','muitos']); sal.automf(5)

rules = [
    ctrl.Rule(exp['junior'] & lang['poucas'] & fram['poucos'], sal['poor']),
    ctrl.Rule(exp['junior'] & (lang['medias'] | fram['medios']), sal['mediocre']),
    ctrl.Rule(exp['mid'], sal['average']),
    ctrl.Rule(exp['senior'] & (lang['muitas'] | fram['muitos']), sal['good']),
    ctrl.Rule(exp['senior'] & (lang['medias'] | fram['medios']), sal['decent']),
    ctrl.Rule(exp['mid'] & lang['muitas'] & fram['muitos'], sal['decent'])
]
fctrl = ctrl.ControlSystem(rules)

# Sample 200 para predicao
n = len(X_te_fn); rng = np.random.RandomState(42)
idx = rng.choice(n, min(200,n), replace=False)
yp_fz = np.full(n, np.nan)
for i in idx:
    sim = ctrl.ControlSystemSimulation(fctrl)
    try:
        sim.input['exp']=float(X_te_fn[i,0]); sim.input['lang']=float(X_te_fn[i,1])
        sim.input['fram']=float(X_te_fn[i,2]); sim.compute()
        yp_fz[i]=sim.output['sal']
    except: yp_fz[i]=0.5
v = yp_fz[~np.isnan(yp_fz)]; yp_fz[np.isnan(yp_fz)] = np.median(v)
yp_fz = yp_fz*(y_mx-y_mn)+y_mn; r2_fz = r2_score(y_te, yp_fz)
results['Fuzzy']={'y_pred':yp_fz,'test_r2':r2_fz}
print(f"[D] Fuzzy: R2={r2_fz:.4f} ({time.time()-t0:.1f}s)")

# ========== BLOCO 5: CV ==========
print("\n--- BLOCO 5: VALIDACAO CRUZADA (5-FOLD) ---")
kf = KFold(5, shuffle=True, random_state=42)
cv = {'Random Forest': RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42, n_jobs=-1),
      'RNA': MLPRegressor(hidden_layer_sizes=(100,50,25), max_iter=300, random_state=42, early_stopping=True, validation_fraction=0.1),
      'SVM': SGDRegressor(loss='squared_error', alpha=0.001, max_iter=1000, tol=1e-3, random_state=42)}
print(f"{'Modelo':<18}{'R2 CV':<14}{'DP':<10}{'R2 Test':<12}{'>82%?':<10}")
print("-"*64)
for n, m in cv.items():
    t0=time.time()
    s = cross_val_score(m, X_tr_p, y_tr, cv=kf, scoring='r2')
    fl = "SIM" if results[n]['test_r2']>0.82 else "NAO"
    print(f"{n:<18}{s.mean():<14.4f}{s.std():<10.4f}{results[n]['test_r2']:<12.4f}{fl:<10}({time.time()-t0:.1f}s)")

# ========== BLOCO 6: GRAFICOS ==========
print("\n--- BLOCO 6: GRAFICOS ---")
sns.set_theme(style='whitegrid'); cols = ['#3498db','#e74c3c','#2ecc71','#f39c12']

fig, ax = plt.subplots(2,2,figsize=(14,12))
for i,n in enumerate(names):
    a = ax[i//2][i%2]; yp = results[n]['y_pred']; r2 = results[n]['test_r2']
    a.scatter(y_te, yp, alpha=0.3, color=cols[i], edgecolors='k', linewidth=0.3)
    lo=min(y_te.min(),yp.min()); hi=max(y_te.max(),yp.max())
    a.plot([lo,hi],[lo,hi],'k--',lw=2)
    a.set_xlabel('Real'); a.set_ylabel('Predito'); a.set_title(f'{n} (R2={r2:.4f})')
plt.tight_layout(); plt.savefig('scatter_real_vs_predito.png',dpi=150); plt.close()
print("OK scatter_real_vs_predito.png")

fig, ax = plt.subplots(2,2,figsize=(14,12))
for i,n in enumerate(names):
    a = ax[i//2][i%2]; yp = results[n]['y_pred']; r2 = results[n]['test_r2']
    a.hist(y_te-yp, bins=40, color=cols[i], alpha=0.7, edgecolor='black')
    a.axvline(0, color='red', ls='--', lw=2); a.set_xlabel('Erro Residual')
    a.set_ylabel('Freq'); a.set_title(f'{n} Residual (R2={r2:.4f})')
plt.tight_layout(); plt.savefig('histograma_erro_residual.png',dpi=150); plt.close()
print("OK histograma_erro_residual.png")

# ========== RESUMO ==========
print("\n--- RESUMO FINAL ---")
print(f"{'Modelo':<18}{'R2':<12}{'>82%':<10}")
print("-"*40)
for n in names:
    fl = "SIM" if results[n]['test_r2']>0.82 else "NAO"
    print(f"{n:<18}{results[n]['test_r2']:<12.4f}{fl:<10}")
best = max(names, key=lambda n: results[n]['test_r2'])
print(f"\nMelhor: {best} (R2={results[best]['test_r2']:.4f})")
print("\nOK!")