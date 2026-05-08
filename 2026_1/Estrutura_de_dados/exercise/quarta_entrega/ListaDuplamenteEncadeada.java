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

    public void inserirPosicao(int valor, int posicao) {
        if (posicao < 0 || posicao > tamanho) {
            return;
        }
        if (posicao == 0) {
            inserirInicio(valor);
            return;
        }
        if (posicao == tamanho) {
            inserirFim(valor);
            return;
        }
        Node novo = new Node(valor);
        Node atual = inicio;
        for (int i = 0; i < posicao; i++) {
            atual = atual.proximo;
        }
        novo.anterior = atual.anterior;
        novo.proximo = atual;
        atual.anterior.proximo = novo;
        atual.anterior = novo;
        tamanho++;
    }

    public void removerPosicao(int posicao) {
        if (posicao < 0 || posicao >= tamanho) {
            return;
        }
        if (posicao == 0) {
            removerInicio();
            return;
        }
        if (posicao == tamanho - 1) {
            removerFim();
            return;
        }
        Node atual = inicio;
        for (int i = 0; i < posicao; i++) {
            atual = atual.proximo;
        }
        atual.anterior.proximo = atual.proximo;
        atual.proximo.anterior = atual.anterior;
        tamanho--;
    }

    public void removerElemento(int valor) {
        Node atual = inicio;
        while (atual != null) {
            if (atual.valor == valor) {
                if (atual == inicio) {
                    removerInicio();
                } else if (atual == fim) {
                    removerFim();
                } else {
                    atual.anterior.proximo = atual.proximo;
                    atual.proximo.anterior = atual.anterior;
                    tamanho--;
                }
                return;
            }
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
