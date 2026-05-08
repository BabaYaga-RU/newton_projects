(inicio + i) % n

inicio: É a posição atual ou o ponto de partida no vetor.
i: É o deslocamento (quantas posições você quer andar para frente).
n: É o tamanho total do vetor (a capacidade dele).
% (Operador Modulo): É o resto da divisão inteira. É ele quem faz o "salto" de volta para o começo.

Exemplo
vetor de tamanho n = 5 (índices de 0 a 4)
(4 + 1) % 5
(4 + 1) (mod 5) = 0

Outros Exemplos
(4 + 2) % 5 = 1 e sobra 1. (Resultado: 1)
(4 + 3) % 5 = 1 e sobra 2. (Resultado: 2)
(1 + 1) % 5 = 0 e sobra 2. (Resultado: 2)

Python
# Para inserir um elemento na próxima posição livre
posicao_inserir = (fim + 1) % n

# Para ler o próximo elemento
posicao_ler = (inicio + 1) % n