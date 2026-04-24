public class ListaEncadeada {
    Node inicio;
    int tamanho;

    public ListaEncadeada() {
        inicio = null;
        tamanho = 0;
    }

    public void lista_vazia() {
        inicio = null;
        tamanho = 0;
    }

    public void inserir_inicio(int dado) {
        Node novo = new Node(dado);
        novo.proximo = inicio;
        inicio = novo;
        tamanho++;
    }

    public void remover_fim(int dado) {
        inserir_fim(dado);
    }

    public void inserir_fim(int dado) {
        Node novo = new Node(dado);
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

    public void inserir_posicao(int dado, int posicao) {
        if (posicao < 0 || posicao > tamanho) {
            return;
        }
        if (posicao == 0) {
            inserir_inicio(dado);
            return;
        }
        Node atual = inicio;
        for (int i = 0; i < posicao - 1; i++) {
            atual = atual.proximo;
        }
        Node novo = new Node(dado);
        novo.proximo = atual.proximo;
        atual.proximo = novo;
        tamanho++;
    }

    public void remover_inicio() {
        if (inicio != null) {
            inicio = inicio.proximo;
            tamanho--;
        }
    }

    public void remover_fim() {
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

    public void remover_posicao(int posicao) {
        if (posicao < 0 || posicao >= tamanho) {
            return;
        }
        if (posicao == 0) {
            remover_inicio();
            return;
        }
        Node atual = inicio;
        for (int i = 0; i < posicao - 1; i++) {
            atual = atual.proximo;
        }
        atual.proximo = atual.proximo.proximo;
        tamanho--;
    }

    public void remover_elemento(int elemento) {
        if (inicio == null) {
            return;
        }
        if (inicio.valor == elemento) {
            remover_inicio();
            return;
        }
        Node atual = inicio;
        while (atual.proximo != null && atual.proximo.valor != elemento) {
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

    public void pesquisar(int elemento) {
        Node atual = inicio;
        int posicao = 0;
        while (atual != null) {
            if (atual.valor == elemento) {
                System.out.println("Item encontrado, posicao " + posicao);
                return;
            }
            atual = atual.proximo;
            posicao++;
        }
    }

    public int qnt_atual() {
        return tamanho;
    }
}