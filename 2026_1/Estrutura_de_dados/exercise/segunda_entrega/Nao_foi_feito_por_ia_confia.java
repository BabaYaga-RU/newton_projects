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
    int[] elementos;
    int tamanho;
    int capacidade;

    public Nao_foi_feito_por_ia_confia() {
        capacidade = 10;
        elementos = new int[capacidade];
        tamanho = 0;
    }

    public void criarListaVazia() {
        tamanho = 0;
    }

    public void inserirNoInicio(int elemento) {
        if (tamanho == capacidade) redimensionar();
        for (int i = tamanho; i > 0; i--) elementos[i] = elementos[i - 1];
        elementos[0] = elemento;
        tamanho++;
    }

    public void inserirNoFim(int elemento) {
        if (tamanho == capacidade) redimensionar();
        elementos[tamanho++] = elemento;
    }

    public void inserirEmPosicao(int posicao, int elemento) {
        if (posicao < 0 || posicao > tamanho) throw new IndexOutOfBoundsException("Posição inválida: " + posicao);
        if (tamanho == capacidade) redimensionar();
        for (int i = tamanho; i > posicao; i--) elementos[i] = elementos[i - 1];
        elementos[posicao] = elemento;
        tamanho++;
    }

    public int removerDoInicio() {
        if (tamanho == 0) throw new IllegalStateException("Lista vazia");
        int elemento = elementos[0];
        for (int i = 0; i < tamanho - 1; i++) elementos[i] = elementos[i + 1];
        tamanho--;
        return elemento;
    }

    public int removerDoFim() {
        if (tamanho == 0) throw new IllegalStateException("Lista vazia");
        return elementos[--tamanho];
    }

    public int removerEmPosicao(int posicao) {
        if (posicao < 0 || posicao >= tamanho) throw new IndexOutOfBoundsException("Posição inválida: " + posicao);
        int elemento = elementos[posicao];
        for (int i = posicao; i < tamanho - 1; i++) elementos[i] = elementos[i + 1];
        tamanho--;
        return elemento;
    }

    public boolean removerElemento(int elemento) {
        for (int i = 0; i < tamanho; i++) {
            if (elementos[i] == elemento) {
                removerEmPosicao(i);
                return true;
            }
        }
        return false;
    }

    public void exibirLista() {
        System.out.print("[");
        for (int i = 0; i < tamanho; i++) {
            System.out.print(elementos[i]);
            if (i < tamanho - 1) System.out.print(", ");
        }
        System.out.println("]");
    }

    public int pesquisarElemento(int elemento) {
        for (int i = 0; i < tamanho; i++) {
            if (elementos[i] == elemento) return i;
        }
        return -1;
    }

    public int tamanho() {
        return tamanho;
    }

    void redimensionar() {
        capacidade *= 2;
        int[] novoArranjo = new int[capacidade];
        for (int i = 0; i < tamanho; i++) novoArranjo[i] = elementos[i];
        elementos = novoArranjo;
    }
}