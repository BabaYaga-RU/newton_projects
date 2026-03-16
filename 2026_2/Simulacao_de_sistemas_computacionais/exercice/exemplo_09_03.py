# pip install pandas numpy tensorflow scikit-learn matplotlib seaborn seaborn

'''
Silenciar avisos
'''

import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
warnings.filterwarnings('ignore')

'''
Importar as bibliotecas e configurar o norebook
'''

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

# Plotar figuras bonitas (opcional)
try:
    import matplotlib.pyplot as plt
    plt.rc('axes', labelsize=14)
    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)
    import seaborn as sns
    plotting_available = True
    print("Bibliotecas de visualização carregadas com sucesso!")
except ImportError:
    plotting_available = False
    # print("Avisos: Bibliotecas de visualização (matplotlib/seaborn) não encontradas. Instale com: pip install matplotlib seaborn")

print("Versão do TensorFlow:", tf.__version__)
print('Setup completo!')

'''
Carregamento dos dados
'''

try:
    # Caminho local para os datasets (ajustado para funcionar fora do Colab)
    caminho_do_arquivo = 'datasets'
    train = pd.read_csv('datasets/train.csv')
    test = pd.read_csv('datasets/test.csv')
    print("Dados carregados com sucesso!")
    print("Dataset de treino:")
    print(train.head())
    print("\nDataset de teste:")
    print(test.head())
    
    # Tratamento de valores faltantes na coluna Age
    media_idade = train['Age'].mean()
    train['Age'] = train['Age'].fillna(media_idade)

    def classificar_faixa_etaria(idade):
        if idade <= 12:
            return 'Crianca' # Usar sem cedilha evita problemas de codificação
        else:
            return 'Adulto'

    # Aplicação da Feature
    train['FaixaEtaria'] = train['Age'].apply(classificar_faixa_etaria)

    # Aplicamos também no teste para garantir consistência futura
    test['Age'] = test['Age'].fillna(test['Age'].mean())
    test['FaixaEtaria'] = test['Age'].apply(classificar_faixa_etaria)

    print("Feature 'FaixaEtaria' criada: Criança (<=12) ou Adulto (>12).")

except FileNotFoundError:
    print("Arquivos não encontrados. Verifique o caminho")

''' 
Separar Features (x) e Target (y)
'''
X = train.drop(['Survived', 'PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
y = train['Survived']

'''
Análise Exploratória de Dados (EDA)
'''

# Informações básicas sobre o dataset
print("\nInformações básicas do dataset de treino:")
print(train.info())
print("\nEstatísticas descritivas:")
print(train.describe())

# Verificando valores nulos
print("\nValores nulos no dataset de treino:")
print(train.isnull().sum())

# Distribuição da variável alvo
print("\nDistribuição da variável alvo (Survived):")
print(train['Survived'].value_counts())

# Visualizações básicas (se matplotlib estiver disponível)
if plotting_available:
    plt.figure(figsize=(12, 8))

    # Distribuição da idade
    plt.subplot(2, 2, 1)
    sns.histplot(train['Age'].dropna(), kde=True)
    plt.title('Distribuição da Idade')

    # Distribuição por sexo
    plt.subplot(2, 2, 2)
    sns.countplot(data=train, x='Sex', hue='Survived')
    plt.title('Sobrevivência por Sexo')

    # Distribuição por classe
    plt.subplot(2, 2, 3)
    sns.countplot(data=train, x='Pclass', hue='Survived')
    plt.title('Sobrevivência por Classe')

    # Distribuição por faixa etária
    plt.subplot(2, 2, 4)
    sns.countplot(data=train, x='FaixaEtaria', hue='Survived')
    plt.title('Sobrevivência por Faixa Etária')

    plt.tight_layout()
    plt.show()
else:
    print("Visualizações puladas - bibliotecas de plotagem não disponíveis")

'''
Pré-processamento dos Dados
'''

# Identificar colunas categóricas e numéricas
categorical_features = ['Sex', 'Embarked', 'FaixaEtaria']
numerical_features = ['Age', 'SibSp', 'Parch', 'Fare']

# Criar preprocessador
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

# Aplicar pré-processamento
X_processed = preprocessor.fit_transform(X)

'''
Divisão dos Dados
'''

X_train, X_val, y_train, y_val = train_test_split(X_processed, y, test_size=0.2, random_state=42, stratify=y)

print(f"\nTamanho do conjunto de treino: {X_train.shape[0]}")
print(f"Tamanho do conjunto de validação: {X_val.shape[0]}")

'''
Modelo de Regressão Logística (Baseline)
'''

# Treinar modelo baseline
baseline_model = LogisticRegression(random_state=42, max_iter=1000)
baseline_model.fit(X_train, y_train)

# Avaliar modelo baseline
baseline_score = baseline_model.score(X_val, y_val)
print(f"\nAcurácia do modelo baseline (Regressão Logística): {baseline_score:.4f}")

# Validação cruzada
cv_scores = cross_val_score(baseline_model, X_processed, y, cv=5)
print(f"Validação cruzada (5 folds): {cv_scores}")
print(f"Média da validação cruzada: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")

# Matriz de confusão
y_pred = baseline_model.predict(X_val)
cm = confusion_matrix(y_val, y_pred)
print(f"\nMatriz de confusão:\n{cm}")

'''
Modelo de Rede Neural (Deep Learning)
'''

# Criar modelo neural
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dropout(0.3),
    layers.Dense(32, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(16, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# Compilar modelo
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Treinar modelo
history = model.fit(X_train, y_train,
                    epochs=100,
                    batch_size=32,
                    validation_data=(X_val, y_val),
                    verbose=0)

# Avaliar modelo neural
neural_score = model.evaluate(X_val, y_val, verbose=0)[1]
print(f"\nAcurácia do modelo neural: {neural_score:.4f}")

# Plotar histórico de treinamento (se matplotlib estiver disponível)
if plotting_available:
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.plot(history.history['loss'], label='Treino')
    plt.plot(history.history['val_loss'], label='Validação')
    plt.title('Loss ao longo das épocas')
    plt.xlabel('Épocas')
    plt.ylabel('Loss')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(history.history['accuracy'], label='Treino')
    plt.plot(history.history['val_accuracy'], label='Validação')
    plt.title('Acurácia ao longo das épocas')
    plt.xlabel('Épocas')
    plt.ylabel('Acurácia')
    plt.legend()

    plt.tight_layout()
    plt.show()
else:
    print("Gráficos de treinamento pulados - bibliotecas de plotagem não disponíveis")

'''
Preparação para Submissão
'''

# Preparar dados de teste
X_test = test.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
X_test_processed = preprocessor.transform(X_test)

# Fazer previsões no conjunto de teste
test_predictions = model.predict(X_test_processed)
test_predictions_binary = (test_predictions > 0.5).astype(int).flatten()

# Criar arquivo de submissão
submission = pd.DataFrame({
    'PassengerId': test['PassengerId'],
    'Survived': test_predictions_binary
})

# Salvar submissão
submission.to_csv('envios/submission_deep_v2.csv', index=False)
print(f"\nArquivo de submissão criado: submission_deep_v2.csv")
print("Primeiras linhas da submissão:")
print(submission.head())

print("\nProcesso concluído com sucesso!")