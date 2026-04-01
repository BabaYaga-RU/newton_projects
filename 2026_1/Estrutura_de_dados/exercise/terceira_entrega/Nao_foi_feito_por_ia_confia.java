/*
 * Lista Encadeada Simples
 * 
 * Imagine uma corrente de bicicleta: cada elo está conectado ao próximo.
 * Na programação, chamamos cada elo de "nó". Cada nó tem:
 * - Um VALOR (o dado que queremos guardar)
 * - Uma REFERÊNCIA para o PRÓXIMO nó (como um elo conectado ao seguinte)
 * 
 * A lista tem uma "cabeça" (início) que aponta para o primeiro nó.
 * O último nó aponta para null (fim da linha).
 * 
 * Exercícios:
 * 1. Criar a lista vazia
 * 2. Inserir no início
 * 3. Inserir no fim
 * 4. Inserir em posição específica
 * 5. Remover do início
 * 6. Remover do fim
 * 7. Remover de posição específica
 * 8. Remover elemento específico
 * 9. Exibir lista
 * 10. Pesquisar elemento
 * 11. Retornar tamanho
 */
public class Nao_foi_feito_por_ia_confia {

    // Classe que representa um NÓ da lista (um elo da corrente)
    // Cada nó guarda um número e sabe quem é o próximo nó
    class No {
        int valor;      // o número guardado neste nó
        No proximo;     // referência para o próximo nó (ou null se for o último)

        // Construtor: cria um nó com um valor
        No(int valor) {
            this.valor = valor;
            this.proximo = null;  // inicialmente não tem próximo
        }
    }

    // Atributos da lista:
    No inicio;        // aponta para o PRIMEIRO nó (cabeça/início da lista)
    int tamanho;      // quantos elementos têm na lista

    // 1. Construtor: cria lista vazia
    // Lista vazia = início é null e tamanho é 0
    public Nao_foi_feito_por_ia_confia() {
        inicio = null;
        tamanho = 0;
    }

    // 2. Inserir no INÍCIO da lista
    // Cria novo nó, faz ele apontar para o antigo início, e atualiza o início
    public void inserirNoInicio(int valor) {
        No novoNo = new No(valor);    // cria novo nó com o valor
        novoNo.proximo = inicio;      // novo nó aponta para quem era o início
        inicio = novoNo;              // novo nó vira o novo início
        tamanho++;
    }

    // 3. Inserir no FIM da lista
    // Percorre até achar o último nó (aquele cujo próximo é null) e anexa o novo
    public void inserirNoFim(int valor) {
        No novoNo = new No(valor);
        if (inicio == null) {
            // lista vazia: novo nó vira o início (e também o fim)
            inicio = novoNo;
        } else {
            // lista tem elementos: percorre até o último
            No atual = inicio;
            while (atual.proximo != null) {
                atual = atual.proximo;  // avança para o próximo
            }
            // atual agora é o último nó
            atual.proximo = novoNo;     // último nó aponta para o novo
        }
        tamanho++;
    }

    // 4. Inserir em POSIÇÃO específica
    // Posição 0 = início, posição tamanho = fim, outras = no meio
    public void inserirEmPosicao(int posicao, int valor) {
        if (posicao < 0 || posicao > tamanho)
            throw new IndexOutOfBoundsException("Posição inválida: " + posicao);

        if (posicao == 0) {
            inserirNoInicio(valor);
            return;
        }
        if (posicao == tamanho) {
            inserirNoFim(valor);
            return;
        }

        // Inserção no meio: para na posição ANTES de onde quer inserir
        No novoNo = new No(valor);
        No atual = inicio;
        for (int i = 0; i < posicao - 1; i++) {
            atual = atual.proximo;
        }
        // atual.proximo é o nó que estava na posição desejada
        novoNo.proximo = atual.proximo;  // novo nó aponta para o que estava lá
        atual.proximo = novoNo;          // nó anterior aponta para o novo
        tamanho++;
    }

    // 5. Remover do INÍCIO
    // Retorna o valor removido. Início avança para o próximo nó.
    public int removerDoInicio() {
        if (inicio == null) throw new IllegalStateException("Lista vazia");
        int valor = inicio.valor;    // guarda valor do primeiro nó
        inicio = inicio.proximo;     // início agora é o próximo nó
        tamanho--;
        return valor;
    }

    // 6. Remover do FIM
    // Percorre até o PENÚLTIMO nó e corta a ligação com o último
    public int removerDoFim() {
        if (inicio == null) throw new IllegalStateException("Lista vazia");
        if (inicio.proximo == null) return removerDoInicio();  // só tem um

        No atual = inicio;
        while (atual.proximo.proximo != null) {
            atual = atual.proximo;  // para no penúltimo
        }
        int valor = atual.proximo.valor;  // valor do último
        atual.proximo = null;             // penúltimo agora é o fim
        tamanho--;
        return valor;
    }

    // 7. Remover de POSIÇÃO específica
    public int removerEmPosicao(int posicao) {
        if (posicao < 0 || posicao >= tamanho)
            throw new IndexOutOfBoundsException("Posição inválida: " + posicao);
        if (posicao == 0) return removerDoInicio();

        No atual = inicio;
        for (int i = 0; i < posicao - 1; i++) {
            atual = atual.proximo;  // para no nó ANTES do que quer remover
        }
        int valor = atual.proximo.valor;         // valor do nó a remover
        atual.proximo = atual.proximo.proximo;   // pula o nó removido
        tamanho--;
        return valor;
    }

    // 8. Remover ELEMENTO específico (pelo valor)
    // Retorna true se achou e removeu, false se não achou
    public boolean removerElemento(int valor) {
        if (inicio == null) return false;
        if (inicio.valor == valor) {
            removerDoInicio();
            return true;
        }

        No atual = inicio;
        // procura o nó CUJO PRÓXIMO tem o valor
        while (atual.proximo != null && atual.proximo.valor != valor) {
            atual = atual.proximo;
        }
        if (atual.proximo != null) {
            atual.proximo = atual.proximo.proximo;  // pula o nó removido
            tamanho--;
            return true;
        }
        return false;
    }

    // 9. Exibir lista
    // Mostra: Lista: 1 -> 2 -> 3 -> null
    public void exibirLista() {
        if (inicio == null) {
            System.out.println("Lista vazia!");
            return;
        }
        System.out.print("Lista: ");
        No atual = inicio;
        while (atual != null) {
            System.out.print(atual.valor);
            if (atual.proximo != null) System.out.print(" -> ");
            atual = atual.proximo;
        }
        System.out.println(" -> null");
    }

    // 10. Pesquisar elemento
    // Retorna a POSIÇÃO do elemento ou -1 se não achou
    public int pesquisarElemento(int valor) {
        if (inicio == null) return -1;
        No atual = inicio;
        int posicao = 0;
        while (atual != null) {
            if (atual.valor == valor) return posicao;
            atual = atual.proximo;
            posicao++;
        }
        return -1;
    }

    // 11. Retornar tamanho
    public int getTamanho() { return tamanho; }

    public boolean estaVazia() { return inicio == null; }
}