// Prazo: 29/03/2026
/*
1. Implemente a classe ListaEncadeada utilizando um arranjo de inteiros para
armazenar os elementos da lista.
2. Crie um método para criar uma lista vazia.
3. Crie um método responsável por inserir um elemento no início da lista.
4. Crie um método responsável por inserir um elemento no fim da lista.
5. Crie um método responsável por inserir um elemento em uma posição específica
da lista.
6. Crie um método responsável por remover um elemento no início da lista.
7. Crie um método responsável por remover um elemento no fim da lista.
8. Crie um método responsável por remover um elemento em uma posição
específica da lista.
9. Crie um método responsável por remover um elemento específico da lista.
10. Crie um método para exibir o conteúdo de uma lista.
11. Crie um método para pesquisar por um elemento específico em uma lista e
informar, caso o elemento exista, a posição na qual ele está armazenado.
12. Crie um método que retorne o número de elementos existentes na lista.
*/
public class Nao_foi_feito_por_ia_confia {
    private int[] elementos;  // Arranjo que armazena os elementos da lista
    private int tamanho;      // Número atual de elementos na lista
    private int capacidade;   // Capacidade máxima do arranjo

    // Construtor que cria uma lista vazia com capacidade inicial
    // Inicializa o arranjo com 10 posições e define tamanho como 0
    public Nao_foi_feito_por_ia_confia() {
        this.capacidade = 10; // Capacidade inicial do arranjo
        this.elementos = new int[capacidade]; // Cria arranjo com capacidade inicial
        this.tamanho = 0;     // Lista começa vazia
    }

    // Método para criar uma lista vazia (mesmo que o construtor)
    // Reseta o tamanho para 0, mantendo o arranjo existente
    public void criarListaVazia() {
        this.tamanho = 0; // Define que não há elementos na lista
    }

    // Método para inserir um elemento no início da lista
    // Complexidade: O(n) - precisa mover todos os elementos existentes
    public void inserirNoInicio(int elemento) {
        // Verifica se precisa redimensionar o arranjo
        if (tamanho == capacidade) {
            redimensionar();
        }
        // Move todos os elementos existentes uma posição para a direita
        // para abrir espaço na posição 0
        for (int i = tamanho; i > 0; i--) {
            elementos[i] = elementos[i - 1];
        }
        // Insere o novo elemento na posição 0 (início)
        elementos[0] = elemento;
        tamanho++; // Incrementa o contador de elementos
    }

    // Método para inserir um elemento no fim da lista
    // Complexidade: O(1) - insere diretamente na próxima posição disponível
    public void inserirNoFim(int elemento) {
        // Verifica se precisa redimensionar o arranjo
        if (tamanho == capacidade) {
            redimensionar();
        }
        // Insere o elemento na próxima posição disponível (tamanho atual)
        elementos[tamanho] = elemento;
        tamanho++; // Incrementa o contador de elementos
    }

    // Método para inserir um elemento em uma posição específica da lista
    // Complexidade: O(n) - pode precisar mover vários elementos
    public void inserirEmPosicao(int posicao, int elemento) {
        // Valida se a posição está dentro dos limites válidos
        // Posição deve ser >= 0 e <= tamanho (permite inserir no final)
        if (posicao < 0 || posicao > tamanho) {
            throw new IndexOutOfBoundsException("Posição inválida: " + posicao);
        }
        // Verifica se precisa redimensionar o arranjo
        if (tamanho == capacidade) {
            redimensionar();
        }
        // Move os elementos existentes para a direita a partir da posição desejada
        // para abrir espaço para o novo elemento
        for (int i = tamanho; i > posicao; i--) {
            elementos[i] = elementos[i - 1];
        }
        // Insere o novo elemento na posição especificada
        elementos[posicao] = elemento;
        tamanho++; // Incrementa o contador de elementos
    }

    // Método para remover um elemento no início da lista
    // Complexidade: O(n) - precisa mover todos os elementos restantes
    public int removerDoInicio() {
        // Verifica se a lista não está vazia
        if (tamanho == 0) {
            throw new IllegalStateException("Lista vazia");
        }
        // Salva o elemento que será removido (primeiro elemento)
        int elemento = elementos[0];
        // Move todos os elementos restantes uma posição para a esquerda
        // para "fechar o buraco" deixado pelo elemento removido
        for (int i = 0; i < tamanho - 1; i++) {
            elementos[i] = elementos[i + 1];
        }
        tamanho--; // Decrementa o contador de elementos
        return elemento; // Retorna o elemento removido
    }

    // Método para remover um elemento no fim da lista
    // Complexidade: O(1) - apenas decrementa o tamanho
    public int removerDoFim() {
        // Verifica se a lista não está vazia
        if (tamanho == 0) {
            throw new IllegalStateException("Lista vazia");
        }
        // Salva o último elemento antes de removê-lo
        int elemento = elementos[tamanho - 1];
        tamanho--; // Simplesmente decrementa o tamanho
        return elemento; // Retorna o elemento removido
    }

    // Método para remover um elemento em uma posição específica da lista
    // Complexidade: O(n) - pode precisar mover vários elementos
    public int removerEmPosicao(int posicao) {
        // Valida se a posição está dentro dos limites válidos
        // Posição deve ser >= 0 e < tamanho (não permite além do último elemento)
        if (posicao < 0 || posicao >= tamanho) {
            throw new IndexOutOfBoundsException("Posição inválida: " + posicao);
        }
        // Salva o elemento que será removido
        int elemento = elementos[posicao];
        // Move os elementos restantes para a esquerda a partir da posição removida
        // para "fechar o buraco"
        for (int i = posicao; i < tamanho - 1; i++) {
            elementos[i] = elementos[i + 1];
        }
        tamanho--; // Decrementa o contador de elementos
        return elemento; // Retorna o elemento removido
    }

    // Método para remover um elemento específico da lista
    // Complexidade: O(n) - percorre a lista para encontrar o elemento
    public boolean removerElemento(int elemento) {
        // Percorre a lista procurando o elemento desejado
        for (int i = 0; i < tamanho; i++) {
            if (elementos[i] == elemento) {
                // Quando encontra, remove pela posição e retorna true
                removerEmPosicao(i);
                return true; // Indica que o elemento foi encontrado e removido
            }
        }
        return false; // Indica que o elemento não foi encontrado
    }

    // Método para exibir o conteúdo de uma lista
    // Exibe os elementos entre colchetes, separados por vírgula
    public void exibirLista() {
        System.out.print("[");
        // Percorre apenas os elementos que existem (até tamanho - 1)
        for (int i = 0; i < tamanho; i++) {
            System.out.print(elementos[i]);
            // Adiciona vírgula entre os elementos, mas não após o último
            if (i < tamanho - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }

    // Método para pesquisar por um elemento específico em uma lista
    // Complexidade: O(n) - percorre a lista sequencialmente
    public int pesquisarElemento(int elemento) {
        // Percorre a lista procurando o elemento desejado
        for (int i = 0; i < tamanho; i++) {
            if (elementos[i] == elemento) {
                return i; // Retorna a posição (índice) do elemento encontrado
            }
        }
        return -1; // Retorna -1 se o elemento não for encontrado
    }

    // Método que retorna o número de elementos existentes na lista
    // Complexidade: O(1) - apenas retorna o valor armazenado
    public int tamanho() {
        return tamanho; // Retorna o contador de elementos atuais
    }

    // Método auxiliar para redimensionar o arranjo quando necessário
    // Dobra a capacidade do arranjo para acomodar mais elementos
    private void redimensionar() {
        capacidade *= 2; // Dobra a capacidade atual
        int[] novoArranjo = new int[capacidade]; // Cria novo arranjo com capacidade maior
        
        // Copia todos os elementos existentes para o novo arranjo
        for (int i = 0; i < tamanho; i++) {
            novoArranjo[i] = elementos[i];
        }
        
        elementos = novoArranjo; // Atualiza a referência para o novo arranjo
    }
}