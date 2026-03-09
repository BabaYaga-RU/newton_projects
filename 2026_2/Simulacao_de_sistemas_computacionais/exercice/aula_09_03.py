'''
Desafio
A prefeitura quer otimizar o atendimento em uma
Unidade Básica de Saúde (UBS), onde há filas longas e
tempo de espera elevado. Você deve modelar e simular
o fluxo de pacientes para propor melhorias.
Dados Necessários
• Número médio de pacientes por hora
• Tempo médio de atendimento por profissional
• Número de profissionais disponíveis
• Horário de funcionamento
'''
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
# Validação Cruzada
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
try:
    caminho_do_arquivo = 'datasets'
    train = pd.read_csv('datasets/train.csv')
    test = pd.read_csv('datasets/test.csv')
    print("Dados carregados com sucesso!")

except FileNotFoundError:
  print("Arquivos não encontrados. Verifique o caminho")