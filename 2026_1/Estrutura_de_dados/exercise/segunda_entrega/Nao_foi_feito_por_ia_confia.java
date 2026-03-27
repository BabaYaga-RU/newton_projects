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
    private int[] elementos;
    private int tamanho;
    private int capacidade;

    // Construtor que cria uma lista vazia com capacidade inicial
    public Nao_foi_feito_por_ia_confia() {
        this.capacidade = 10; // Capacidade inicial
        this.elementos = new int[capacidade];
        this.tamanho = 0;
    }

    // Método para criar uma lista vazia (mesmo que o construtor)
    public void criarListaVazia() {
        this.tamanho = 0;
    }

    // Método para inserir um elemento no início da lista
    public void inserirNoInicio(int elemento) {
        if (tamanho == capacidade) {
            redimensionar();
        }
        // Move todos os elementos uma posição para a direita
        for (int i = tamanho; i > 0; i--) {
            elementos[i] = elementos[i - 1];
        }
        elementos[0] = elemento;
        tamanho++;
    }

    // Método para inserir um elemento no fim da lista
    public void inserirNoFim(int elemento) {
        if (tamanho == capacidade) {
            redimensionar();
        }
        elementos[tamanho] = elemento;
        tamanho++;
    }

    // Método para inserir um elemento em uma posição específica da lista
    public void inserirEmPosicao(int posicao, int elemento) {
        if (posicao < 0 || posicao > tamanho) {
            throw new IndexOutOfBoundsException("Posição inválida: " + posicao);
        }
        if (tamanho == capacidade) {
            redimensionar();
        }
        // Move os elementos para a direita a partir da posição desejada
        for (int i = tamanho; i > posicao; i--) {
            elementos[i] = elementos[i - 1];
        }
        elementos[posicao] = elemento;
        tamanho++;
    }

    // Método para remover um elemento no início da lista
    public int removerDoInicio() {
        if (tamanho == 0) {
            throw new IllegalStateException("Lista vazia");
        }
        int elemento = elementos[0];
        // Move todos os elementos uma posição para a esquerda
        for (int i = 0; i < tamanho - 1; i++) {
            elementos[i] = elementos[i + 1];
        }
        tamanho--;
        return elemento;
    }

    // Método para remover um elemento no fim da lista
    public int removerDoFim() {
        if (tamanho == 0) {
            throw new IllegalStateException("Lista vazia");
        }
        int elemento = elementos[tamanho - 1];
        tamanho--;
        return elemento;
    }

    // Método para remover um elemento em uma posição específica da lista
    public int removerEmPosicao(int posicao) {
        if (posicao < 0 || posicao >= tamanho) {
            throw new IndexOutOfBoundsException("Posição inválida: " + posicao);
        }
        int elemento = elementos[posicao];
        // Move os elementos para a esquerda a partir da posição removida
        for (int i = posicao; i < tamanho - 1; i++) {
            elementos[i] = elementos[i + 1];
        }
        tamanho--;
        return elemento;
    }

    // Método para remover um elemento específico da lista
    public boolean removerElemento(int elemento) {
        for (int i = 0; i < tamanho; i++) {
            if (elementos[i] == elemento) {
                removerEmPosicao(i);
                return true;
            }
        }
        return false;
    }

    // Método para exibir o conteúdo de uma lista
    public void exibirLista() {
        System.out.print("[");
        for (int i = 0; i < tamanho; i++) {
            System.out.print(elementos[i]);
            if (i < tamanho - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }

    // Método para pesquisar por um elemento específico em uma lista
    public int pesquisarElemento(int elemento) {
        for (int i = 0; i < tamanho; i++) {
            if (elementos[i] == elemento) {
                return i; // Retorna a posição do elemento
            }
        }
        return -1; // Elemento não encontrado
    }

    // Método que retorna o número de elementos existentes na lista
    public int tamanho() {
        return tamanho;
    }

    // Método auxiliar para redimensionar o arranjo quando necessário
    private void redimensionar() {
        capacidade *= 2;
        int[] novoArranjo = new int[capacidade];
        for (int i = 0; i < tamanho; i++) {
            novoArranjo[i] = elementos[i];
        }
        elementos = novoArranjo;
    }
}