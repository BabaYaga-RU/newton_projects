public class ListaEncadeada {
    Node inicio;
    int tamanho;

    public ListaEncadeada() {
        inicio = null;
        tamanho = 0;
    }

    public void listaVazia() {
        inicio = null;
        tamanho = 0;
    }

    public void inserirInicio(int valor) {
        Node novo = new Node(valor);
        novo.proximo = inicio;
        inicio = novo;
        tamanho++;
    }

    public void inserirFim(int valor) {
        Node novo = new Node(valor);
        if (inicio == null) {
            inicio = novo;
        } else {
            Node atual = inicio;
            while (atual.proximo != null) {
                atual = atual.proximo;
            }
            atual.proximo = novo;
        }
        tamanho++;
    }

    public void inserirPosicao(int valor, int posicao) {
        if (posicao < 0 || posicao > tamanho) {
            return;
        }
        if (posicao == 0) {
            inserirInicio(valor);
            return;
        }
        Node atual = inicio;
        for (int i = 0; i < posicao - 1; i++) {
            atual = atual.proximo;
        }
        Node novo = new Node(valor);
        novo.proximo = atual.proximo;
        atual.proximo = novo;
        tamanho++;
    }

    public void removerInicio() {
        if (inicio != null) {
            inicio = inicio.proximo;
            tamanho--;
        }
    }

    public void removerFim() {
        if (inicio == null) {
            return;
        }
        if (inicio.proximo == null) {
            inicio = null;
            tamanho--;
            return;
        }
        Node atual = inicio;
        while (atual.proximo.proximo != null) {
            atual = atual.proximo;
        }
        atual.proximo = null;
        tamanho--;
    }

    public void removerPosicao(int posicao) {
        if (posicao < 0 || posicao >= tamanho) {
            return;
        }
        if (posicao == 0) {
            removerInicio();
            return;
        }
        Node atual = inicio;
        for (int i = 0; i < posicao - 1; i++) {
            atual = atual.proximo;
        }
        atual.proximo = atual.proximo.proximo;
        tamanho--;
    }

    public void removerElemento(int valor) {
        if (inicio == null) {
            return;
        }
        if (inicio.valor == valor) {
            removerInicio();
            return;
        }
        Node atual = inicio;
        while (atual.proximo != null && atual.proximo.valor != valor) {
            atual = atual.proximo;
        }
        if (atual.proximo != null) {
            atual.proximo = atual.proximo.proximo;
            tamanho--;
        }
    }

    public void imprimir() {
        Node atual = inicio;
        while (atual != null) {
            System.out.println(atual.valor);
            atual = atual.proximo;
        }
    }

    public int pesquisar(int valor) {
        Node atual = inicio;
        int posicao = 0;
        while (atual != null) {
            if (atual.valor == valor) {
                return posicao;
            }
            atual = atual.proximo;
            posicao++;
        }
        return -1;
    }

    public int qntAtual() {
        return tamanho;
    }
