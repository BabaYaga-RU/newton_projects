"""
Explicação dos Comentários do Sistema de Filas

Este arquivo contém a explicação detalhada dos comentários que estavam no arquivo original Sistema_de_Filas.py.

O sistema modela um caixa de atendimento onde clientes chegam em intervalos
aleatórios e são atendidos com tempos de serviço também aleatórios.
"""

# pip install simpy
"""
Comando para instalar a biblioteca SimPy, que é necessária para a simulação.
SimPy é uma biblioteca de simulação de eventos discretos para Python.
"""

import simpy
import random

"""
Configurações da Simulação

Constantes que definem os parâmetros do sistema de filas sendo simulado.
"""
TEMPO_SIMULACAO = 60  # minutos - Duração total da simulação
INTERVALO_CHEGADA = 5  # minutos entre chegadas - Média do intervalo entre chegadas de clientes
TEMPO_ATENDIMENTO = [3, 7]  # tempo de atendimento entre 3 e 7 minutos - Intervalo de tempo de serviço

def atender_cliente(env, nome, caixa):
    """
    Função que simula o atendimento de um cliente.
    
    Parâmetros:
    - env: Ambiente de simulação do SimPy
    - nome: Identificador do cliente
    - caixa: Recurso (caixa) que será utilizado para o atendimento
    
    Esta função:
    1. Gera um tempo de atendimento aleatório dentro do intervalo definido
    2. Imprime o início do atendimento com o tempo atual da simulação
    3. Ocupa o recurso (caixa) pelo tempo de atendimento
    4. Imprime o término do atendimento
    """
    pass

def chegada_clientes(env, caixa):
    """
    Função que simula a chegada de clientes ao sistema.
    
    Parâmetros:
    - env: Ambiente de simulação do SimPy
    - caixa: Recurso (caixa) disponível para atendimento
    
    Esta função:
    1. Cria um contador de clientes
    2. Enquanto a simulação estiver em execução:
       - Incrementa o contador de clientes
       - Aguarda um intervalo aleatório baseado na distribuição exponencial
       - Inicia o processo de atendimento para o novo cliente
    """
    pass

# Configuração e execução da simulação
"""
Criação do ambiente de simulação, definição dos recursos e início da simulação.
"""

# ================ 1. Gráfico: Tempo de Atendimento por Cliente ================

"""
Matplotlib é uma biblioteca de visualização de dados em Python.
plt é o alias padrão para matplotlib.pyplot, que contém funções para criar gráficos.

Principais componentes usados:
- plt.figure(): Cria uma nova figura (janela) para o gráfico
- plt.plot(): Cria um gráfico de linhas
- plt.title(): Define o título do gráfico
- plt.xlabel()/plt.ylabel(): Define os rótulos dos eixos X e Y
- plt.grid(): Adiciona linhas de grade ao gráfico
- plt.show(): Exibe o gráfico na tela
"""

import matplotlib.pyplot as plt

"""
range() é uma função que gera uma sequência de números.
range(1, len(tempos_atendimento)+1) cria: [1, 2, 3, 4, 5, 6, 7]
Isso representa os números dos clientes no eixo X.

marker='o' define que cada ponto será marcado com um círculo
linestyle='-' define que as linhas entre os pontos serão sólidas
"""

# =================== 2. Gráfico: Tempo de Espera por Cliente ==================

"""
Gráfico de barras (bar chart) - Ideal para comparar categorias diferentes.
Cada barra representa o tempo de espera de um cliente específico.
"""

# ========= 3. Gráfico: Número de Clientes Atendidos ao Longo do Tempo =========

"""
Gráfico de degraus (step plot) - Ideal para mostrar mudanças discretas ao longo do tempo.
Cada "degrau" representa um novo cliente atendido.
"""

# =============================== Próximos Passos ==============================

# Painel Interativo
"""
Transformar os gráficos em um painel interativo com Plotly
Plotly permite criar gráficos interativos com zoom, pan, tooltips e mais
"""

# Exportação de Dados
"""
Exportar os dados para análise em Excel
Permite análise mais detalhada e relatórios em planilhas
"""

# Análise Avançada
"""
Integrar com Power BI para análises mais complexas
Power BI oferece dashboards profissionais e conectividade com diversas fontes de dados
"""