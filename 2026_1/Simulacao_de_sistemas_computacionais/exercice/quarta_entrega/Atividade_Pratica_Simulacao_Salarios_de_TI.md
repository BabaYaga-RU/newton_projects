Simulação de Sistemas Digitais
Atividade Prática – Simulação de Salários de Profissionais de TI
Disciplina: Simulação de Sistemas Computacionais
Professor: Ruy Barbosa Figueiredo Junior
Descrição da Atividade Prática
Título: Simulação de salários de Profissionais de TI
Duração: 110 minutos
Objetivo: Desenvolver um algoritmo de simulação computacional capaz de estimar o salário de
profissionais de TI, com base em variáveis presentes no dataset, atingindo acurácia mínima de 75%,
devidamente calculada e exibida no código.
1. Contextualização
A simulação computacional é amplamente utilizada para modelar sistemas reais e apoiar processos de
tomada de decisão. No contexto da área de Tecnologia da Informação (TI), a análise e previsão salarial é
um problema real, relevante e baseado em dados.
Nesta atividade, os alunos irão utilizar datasets reais de salários de profissionais de TI, disponíveis na
plataforma Kaggle, para desenvolver um modelo de simulação salarial, aplicando técnicas de préprocessamento de dados, modelagem, treinamento e validação, com foco na acurácia da simulação.
2. Dataset
Cada aluno deverá:
• Baixar o conjunto de dadtasets sobre salários de profissionais de TI disponível no Kaggle
Identificar as variáveis comuns:
o Cargo (Job Title)
o Nível de experiência (Junior, Pleno, Sênior)
o Anos de experiência
o Localização / país
o Formação
o Tipo de contrato
o Área de atuação (Data, Desenvolvimento, Infraestrutura etc.)
o Salário anual ou mensal
3. Etapas da Atividade
3.1. Pré-processamento dos Dados
• Tratar valores ausentes
• Converter variáveis categóricas (ex: cargo, nível) em variáveis numéricas
• Normalizar ou padronizar os dados, se necessário
• Separar os dados em conjunto de treinamento e teste
3.2. Modelo de Simulação
A simulação poderá utilizar, por exemplo:
• Regressão Linear
• Regressão Polinomial
• Árvores de Decisão
• Random Forest
• Outro modelo supervisionado justificável
O salário será a variável simulada (variável dependente).
4.3. Cálculo da Acurácia
A acurácia do modelo deve ser explicitamente calculada e exibida no algoritmo, sendo obrigatória:
• Acurácia ≥ 75%
• Exibição do valor da acurácia no console ou na saída do programa
A métrica pode ser definida como:
• R² (Coeficiente de determinação), ou
• Outra métrica equivalente, desde que bem justificada
4. Exemplos de Algoritmos (Python)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
# Carregar dataset
dataset = pd.read_csv("it_salary_dataset.csv")
# Seleção de variáveis
X = dataset[['experiencia_anos', 'nivel', 'cargo']]
y = dataset['salario']
# Codificação de variáveis categóricas
encoder = LabelEncoder()
X['nivel'] = encoder.fit_transform(X['nivel'])
X['cargo'] = encoder.fit_transform(X['cargo'])
# Separação treino/teste
X_train, X_test, y_train, y_test = train_test_split(
 X, y, test_size=0.2, random_state=42
)
# Modelo de simulação
modelo = LinearRegression()
modelo.fit(X_train, y_train)
# Simulação (previsão)
salarios_simulados = modelo.predict(X_test)
# Avaliação da acurácia
acuracia = r2_score(y_test, salarios_simulados)
print(f"Acurácia da simulação salarial: {acuracia * 100:.2f}%")
5. Entregas
O aluno deverá entregar:
1. Código-fonte do algoritmo de simulação
2. Relatório técnico contendo:
o Descrição do dataset
o Justificativa do modelo escolhido
o Etapas de pré-processamento
o Resultado da acurácia (gráficos)
o Análise crítica dos resultados