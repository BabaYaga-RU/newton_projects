Atividade Prática – OTIMIZAÇÃO DE SIMULADORES ESTOCÁSTICOS DE TI
Comparativo de Performance: Random Forest vs. RNA vs. SVM vs. Lógica Nebulosa
Disciplina: Simulação de Sistemas Computacionais
Professor: Ruy Barbosa Figueiredo Junior
1. BLOCO 1: INFRAESTRUTURA
A primeira etapa consiste na preparação do ambiente computacional de alto desempenho no Google Colab.
O discente deverá realizar a montagem do Google Drive para garantir a persistência dos dados e a
exportação dos resultados. A carga de bibliotecas deve contemplar o ecossistema completo de Ciência de
Dados, incluindo pandas e numpy para manipulação matricial, matplotlib e seaborn para visualização
analítica, e o scikit-learn para a base de modelagem. Adicionalmente, devem ser importadas as bibliotecas
skfuzzy para a lógica nebulosa e tensorflow/keras para a construção das arquiteturas de redes neurais
profundas.
2. BLOCO 2: DADOS
O carregamento dos conjuntos de dados deve ser realizado a partir do diretório datasets/salario/, acessando
os arquivos train.csv (treinamento) e test.csv (teste). Após a carga, é mandatória a execução de uma análise
estatística descritiva completa. Esta análise deve identificar a média, mediana, desvio padrão e quartis da
variável alvo salary_usd, além de verificar a correlação de Pearson entre as variáveis numéricas. O objetivo
é detectar anomalias ou outliers que possam enviesar a simulação estocástica.
3. BLOCO 3: PRÉ-PROCESSAMENTO
Nesta fase, aplica-se a engenharia de atributos para transformar dados brutos em sinais preditivos. O
discente deve criar as variáveis num_linguagens e num_frameworks através do processamento de strings.
O nível de experiência deve ser convertido em uma escala ordinal numérica. A normalização será executada
via ColumnTransformer, aplicando o StandardScaler para garantir que todas as variáveis possuam média
zero e variância unitária, conforme a fórmula:
Para capturar interações não-lineares complexas, deve-se aplicar o PolynomialFeatures de grau 2 em todas
as variáveis numéricas antes da entrada nos modelos.
4. BLOCO 4: MODELAGEM COMPARATIVA
A atividade exige a implementação e o ajuste fino de quatro arquiteturas distintas de regressores para a
simulação salarial:
1. Modelo A: Random Forest (Baseline): Configurado com 200 árvores de decisão e profundidade
máxima limitada a 10 níveis para evitar o sobreajuste.
2. Modelo B: RNA (Rede Neural Artificial): Implementação de um MLPRegressor com no mínimo 3
camadas ocultas (ex: 100, 50, 25 neurônios) e 1000 iterações para convergência do gradiente.
3. Modelo C: SVM (Support Vector Machine): Utilização do SVR com kernel RBF (Radial Basis
Function) ou SGDRegressor para otimização de performance em grandes volumes de dados.
4. Modelo D: Lógica Nebulosa (Fuzzy): Desenvolvimento de um sistema de inferência do tipo TakagiSugeno ou Neuro-Fuzzy, capaz de mapear variáveis linguísticas em saídas numéricas precisas.
5. BLOCO 5: VALIDAÇÃO E MÉTRICAS
A validação da eficácia dos simuladores será pautada pelo coeficiente de determinação
R²
. O desafio técnico imposto é que os modelos B, C e D superem o benchmark do Modelo A, atingindo um
R² > 82%
. A métrica deve ser calculada através de Validação Cruzada (5-fold) para garantir a estabilidade estatística,
utilizando a fórmula:
6. BLOCO 6: ANÁLISE GRÁFICA
A etapa final exige a geração de evidências visuais do desempenho. Devem ser plotados gráficos de
dispersão comparando os valores reais versus os preditos para cada um dos quatro modelos.
Adicionalmente, o discente deve gerar um histograma do erro residual (diferença entre o valor real e a
predição), permitindo analisar se a distribuição dos erros segue uma curva normal, o que valida a qualidade
da simulação estocástica.
QUESTIONÁRIO DE ANÁLISE CRÍTICA
1. Explique por que a Rede Neural conseguiu capturar padrões que o Random Forest ignorou.
2. Analise o custo computacional (tempo de treinamento) do SVM em relação ao Random Forest
para 40k registros.
3. Como a Lógica Fuzzy permite lidar com a incerteza na definição de cargos e senioridade?
4. Qual modelo apresentou a melhor generalização no conjunto de teste? Justifique com base no
Overfitting.
5. Proponha uma arquitetura Ensemble que combine os 4 modelos (Stacking) para atingir R² > 90%.
