import random
import math
import matplotlib.pyplot as plt
import numpy as numpy_np
import pandas as pandas_pd

def gerar_intervalos(tempo_medio):
    # X = -ln(U) / λ
    if tempo_medio <= 0:
        return 0
    
    u = random.random()
    if u == 0:
        u = 0.0001
    
    _lambda = 1.0 / tempo_medio
    
    return -math.log(u) / _lambda

def calcular_media(lista_numeros):
    if not lista_numeros:
        return 0
    
    # Otimizar com array e calcular media
    return numpy_np.mean(numpy_np.array(lista_numeros))

def calcular_estatistica(lista_numeros):
    if not lista_numeros:
        return {}
    
    array_otimizado =  numpy_np.array(lista_numeros)

    estatistica = {
        'media': numpy_np.mean(array_otimizado),
        'mediana': numpy_np.median(array_otimizado),
        'desvio_padrao': numpy_np.std(array_otimizado),
        'variancia': numpy_np.var(array_otimizado),
        'minimo': numpy_np.min(array_otimizado),
        'maximo': numpy_np.max(array_otimizado),
        'percentil_25': numpy_np.percentile(array_otimizado, 25),
        'percentil_50': numpy_np.percentile(array_otimizado, 50), #Mediana
        'percentil_75': numpy_np.percentile(array_otimizado, 75),
        'quantidade': len(array_otimizado)
    }

    return estatistica





print(gerar_intervalos(10))