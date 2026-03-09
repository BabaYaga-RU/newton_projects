# pip install pandas numpy tensorflow scikit-learn

import os
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
print("Versão do TensorFlow:", tf.__version__)
# Validação Cruzada
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
print('Setup completo!')
try:
    caminho_do_arquivo = 'datasets'
    train = pd.read_csv('datasets/train.csv')
    test = pd.read_csv('datasets/test.csv')
    print("Dados carregados com sucesso!")
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