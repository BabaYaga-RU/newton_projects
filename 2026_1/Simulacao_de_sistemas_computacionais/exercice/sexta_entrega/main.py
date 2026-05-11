# pip install pandas seaborn matplotlib scikit-learn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score
)

# ============================================================
# CARREGAMENTO DO DATASET
# ============================================================

iris = load_iris()

dados_iris = pd.DataFrame(
    data=iris.data,
    columns=[
        'comp_sepala',
        'larg_sepala',
        'comp_petala',
        'larg_petala'
    ]
)

dados_iris['especie'] = iris.target

print("\n========== PRIMEIRAS LINHAS ==========\n")
print(dados_iris.head())

print("\n========== INFORMAÇÕES ==========\n")
print(dados_iris.info())

print("\n========== ESTATÍSTICAS ==========\n")
print(dados_iris.describe())

# ============================================================
# ANÁLISE EXPLORATÓRIA
# ============================================================

sns.pairplot(dados_iris, hue='especie')
plt.show()

# ============================================================
# SEPARAÇÃO ENTRE CARACTERÍSTICAS E ALVO
# ============================================================

caracteristicas = dados_iris.drop('especie', axis=1)
alvo = dados_iris['especie']

# ============================================================
# DIVISÃO DOS DADOS
# ============================================================

treino_x, teste_x, treino_y, teste_y = train_test_split(
    caracteristicas,
    alvo,
    test_size=0.2,
    random_state=42,
    stratify=alvo
)

# ============================================================
# CRIAÇÃO DO MODELO RANDOM FOREST
# ============================================================

modelo_floresta = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# ============================================================
# TREINAMENTO DO MODELO
# ============================================================

modelo_floresta.fit(treino_x, treino_y)

# ============================================================
# PREVISÕES
# ============================================================

previsoes = modelo_floresta.predict(teste_x)

# ============================================================
# AVALIAÇÃO DO MODELO
# ============================================================

acuracia = accuracy_score(teste_y, previsoes)

print("\n========== ACURÁCIA ==========\n")
print(f"Acurácia Global: {acuracia:.2f}")

print("\n========== RELATÓRIO DE CLASSIFICAÇÃO ==========\n")
print(classification_report(teste_y, previsoes))

# ============================================================
# MATRIZ DE CONFUSÃO
# ============================================================

matriz_confusao = confusion_matrix(teste_y, previsoes)

plt.figure(figsize=(8, 5))

sns.heatmap(
    matriz_confusao,
    annot=True,
    cmap='Blues',
    fmt='d'
)

plt.xlabel('Previsão do Modelo')
plt.ylabel('Valor Real')
plt.title('Matriz de Confusão - Iris')

plt.show()

# ============================================================
# FEATURE IMPORTANCE
# ============================================================

importancias = modelo_floresta.feature_importances_

nomes_colunas = caracteristicas.columns

dados_importancia = pd.DataFrame({
    'Atributo': nomes_colunas,
    'Importancia': importancias
})

dados_importancia = dados_importancia.sort_values(
    by='Importancia',
    ascending=False
)

print("\n========== IMPORTÂNCIA DAS FEATURES ==========\n")
print(dados_importancia)

"""

1)B

2) C

3) B

4) A

5) C

6) C

7) C

8) C

9) C

10) C

1)

A divisão entre treino e teste é importante para validar a
capacidade de generalização do modelo.

Se utilizarmos os mesmos dados para treino e teste, o modelo
pode decorar os padrões, gerando overfitting e resultados irreais.


2)

O aumento do parâmetro n_estimators melhora a estabilidade e
precisão do modelo, pois múltiplas árvores reduzem variância.

Porém, isso também aumenta o custo computacional e o tempo
de processamento.


3)

O stratify=alvo mantém a proporção original das classes
nos conjuntos de treino e teste.

Isso evita desbalanceamento entre as classes.


4)

A matriz de confusão permite identificar onde o modelo
está errando.

Ela ajuda especialmente a observar confusões entre
Versicolor e Virginica, pois possuem características parecidas.


5)

Feature Importance representa o nível de importância de cada
atributo para a tomada de decisão do modelo.

O Random Forest calcula isso analisando o impacto de cada
feature nas árvores da floresta.


6)

Precisão mede quantas previsões positivas estavam corretas.

Recall mede quantos casos positivos reais foram encontrados
pelo modelo.


7)

Esse cenário representa overfitting.

O modelo aprende muito bem os dados de treino, mas não consegue
generalizar corretamente para novos dados.

Isso pode ser reduzido ajustando hiperparâmetros,
reduzindo complexidade ou utilizando validação cruzada.


8)

O Random Forest não depende fortemente da escala dos dados,
pois árvores de decisão trabalham por divisões e não distância.

Por isso, normalização geralmente não é necessária.


9)

O F1-Score é importante em datasets desbalanceados porque
combina Precisão e Recall em uma única métrica equilibrada.


10)

Para comparar o Random Forest com outro algoritmo como
SVM ou KNN seria necessário:

1. Importar o novo algoritmo.
2. Treinar ambos usando o mesmo conjunto de treino.
3. Utilizar o mesmo conjunto de teste.
4. Comparar métricas como acurácia, precisão, recall e F1-score.
5. Comparar as matrizes de confusão.
"""
