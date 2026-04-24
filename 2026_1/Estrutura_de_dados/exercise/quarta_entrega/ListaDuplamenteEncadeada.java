public class ListaDuplamenteEncadeada {
    Node inicio;
    Node fim;
    int tamanho;

    public ListaDuplamenteEncadeada() {
        inicio = null;
        fim = null;
        tamanho = 0;
    }

    public void listaVazia() {
        inicio = null;
        fim = null;
        tamanho = 0;
    }

    public void inserirInicio(int valor) {
        Node novo = new Node(valor);
        if (inicio == null) {
            inicio = novo;
            fim = novo;
        } else {
            novo.proximo = inicio;
            inicio.anterior = novo;
            inicio = novo;
        }
        tamanho++;
    }

    public void inserirFim(int valor) {
        Node novo = new Node(valor);
        if (fim == null) {
            inicio = novo;
            fim = novo;
        } else {
            fim.proximo = novo;
            novo.anterior = fim;
            fim = novo;
        }
        tamanho++;
    }

    public void removerInicio() {
        if (inicio == null) {
            return;
        }
        if (inicio == fim) {
            inicio = null;
            fim = null;
        } else {
            inicio = inicio.proximo;
            if (inicio != null) {
                inicio.anterior = null;
            }
        }
        tamanho--;
    }

    public void removerFim() {
        if (fim == null) {
            return;
        }
        if (inicio == fim) {
            inicio = null;
            fim = null;
        } else {
            fim = fim.anterior;
            if (fim != null) {
                fim.proximo = null;
            }
        }
        tamanho--;
    }

    public void imprimir() {
        Node atual = inicio;
        while (atual != null) {
            System.out.println(atual.valor);
            atual = atual.proximo;
        }
    }

    public int qntAtual() {
        return tamanho;
    }
}
