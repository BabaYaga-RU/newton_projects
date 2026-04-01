/*
 * Lista Duplamente Encadeada
 * 
 * Imagine uma corrente onde cada elo tem DUAS conexões:
 * - Uma seta apontando para o elo SEGUINTE (próximo)
 * - Uma seta apontando para o elo ANTERIOR
 * 
 * Isso permite navegar nos DOIS SENTIDOS: da início para o fim, 
 * ou do fim para a início.
 * 
 * Cada nó (elo) guarda:
 * - VALOR: o dado
 * - PRÓXIMO: aponta para quem vem DEPOIS
 * - ANTERIOR: aponta para quem vem ANTES
 * 
 * A lista tem:
 * - INÍCIO (cabeça): primeiro nó (não tem anterior)
 * - FIM (cauda): último nó (não tem próximo)
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
 * 9. Exibir lista (frente e verso)
 * 10. Pesquisar elemento
 * 11. Retornar tamanho
 */
public class Nao_foi_feito_por_ia_confia {

    // Classe que representa um NÓ da lista duplamente encadeada
    // Cada nó tem valor, seta para o próximo E seta para o anterior
    class No {
        int valor;       // o número guardado
        No proximo;      // aponta para quem vem DEPOIS (ou null se for o fim)
        No anterior;     // aponta para quem vem ANTES (ou null se for o início)

        No(int valor) {
            this.valor = valor;
            this.proximo = null;
            this.anterior = null;
        }
    }

    // Atributos da lista:
    No inicio;       // aponta para o PRIMEIRO nó (início/cabeça)
    No fim;          // aponta para o ÚLTIMO nó (fim/cauda)
    int tamanho;     // quantos elementos têm

    // 1. Construtor: cria lista vazia
    public Nao_foi_feito_por_ia_confia() {
        inicio = null;
        fim = null;
        tamanho = 0;
    }

    // 2. Inserir no INÍCIO
    // Novo nó vira o primeiro. Se lista vazia, também vira o fim.
    public void inserirNoInicio(int valor) {
        No novoNo = new No(valor);
        if (inicio == null) {
            // lista vazia: novo nó é início E fim
            inicio = novoNo;
            fim = novoNo;
        } else {
            // lista tem elementos: novo nó aponta para antigo início
            novoNo.proximo = inicio;
            inicio.anterior = novoNo;  // antigo início aponta para trás
            inicio = novoNo;           // novo nó vira o início
        }
        tamanho++;
    }

    // 3. Inserir no FIM
    // Novo nó vira o último. Se lista vazia, também vira o início.
    public void inserirNoFim(int valor) {
        No novoNo = new No(valor);
        if (inicio == null) {
            // lista vazia: novo nó é início E fim
            inicio = novoNo;
            fim = novoNo;
        } else {
            // lista tem elementos: fim atual aponta para novo nó
            fim.proximo = novoNo;
            novoNo.anterior = fim;  // novo nó aponta para trás (fim atual)
            fim = novoNo;           // novo nó vira o fim
        }
        tamanho++;
    }

    // 4. Inserir em POSIÇÃO específica
    // Encaixa novo nó entre dois nós existentes
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

        // Inserção no meio: encontra o nó que está NA posição
        No novoNo = new No(valor);
        No atual = inicio;
        for (int i = 0; i < posicao; i++) {
            atual = atual.proximo;
        }
        // atual é o nó que estava na posição desejada
        // Encaixa novo nó ENTRE atual.anterior e atual
        novoNo.anterior = atual.anterior;
        novoNo.proximo = atual;
        atual.anterior.proximo = novoNo;
        atual.anterior = novoNo;
        tamanho++;
    }

    // 5. Remover do INÍCIO
    // Início avança para o próximo. Novo início não tem anterior.
    public int removerDoInicio() {
        if (inicio == null) throw new IllegalStateException("Lista vazia");
        int valor = inicio.valor;

        if (inicio == fim) {
            // só tinha um elemento
            inicio = null;
            fim = null;
        } else {
            // tem mais elementos: início avança
            inicio = inicio.proximo;
            inicio.anterior = null;  // novo início não tem anterior
        }
        tamanho--;
        return valor;
    }

    // 6. Remover do FIM
    // Fim recua para o anterior. Novo fim não tem próximo.
    public int removerDoFim() {
        if (inicio == null) throw new IllegalStateException("Lista vazia");
        int valor = fim.valor;

        if (inicio == fim) {
            // só tinha um elemento
            inicio = null;
            fim = null;
        } else {
            // tem mais elementos: fim recua
            fim = fim.anterior;
            fim.proximo = null;  // novo fim não tem próximo
        }
        tamanho--;
        return valor;
    }

    // 7. Remover de POSIÇÃO específica
    // Conecta o nó anterior ao posterior, pulando o removido
    public int removerEmPosicao(int posicao) {
        if (posicao < 0 || posicao >= tamanho)
            throw new IndexOutOfBoundsException("Posição inválida: " + posicao);

        if (posicao == 0) return removerDoInicio();
        if (posicao == tamanho - 1) return removerDoFim();

        // Remove do meio: encontra o nó na posição
        No atual = inicio;
        for (int i = 0; i < posicao; i++) {
            atual = atual.proximo;
        }
        int valor = atual.valor;
        // Conecta anterior com próximo, pulando o atual
        atual.anterior.proximo = atual.proximo;
        atual.proximo.anterior = atual.anterior;
        tamanho--;
        return valor;
    }

    // 8. Remover ELEMENTO específico (pelo valor)
    public boolean removerElemento(int valor) {
        if (inicio == null) return false;

        if (inicio.valor == valor) {
            removerDoInicio();
            return true;
        }
        if (fim.valor == valor) {
            removerDoFim();
            return true;
        }

        // Procura no meio
        No atual = inicio;
        while (atual != null && atual.valor != valor) {
            atual = atual.proximo;
        }
        if (atual != null) {
            atual.anterior.proximo = atual.proximo;
            atual.proximo.anterior = atual.anterior;
            tamanho--;
            return true;
        }
        return false;
    }

    // 9. Exibir lista (do início para o fim)
    // Mostra: Lista (início -> fim): 1 <-> 2 <-> 3 -> null
    public void exibirLista() {
        if (inicio == null) {
            System.out.println("Lista vazia!");
            return;
        }
        System.out.print("Lista (início -> fim): ");
        No atual = inicio;
        while (atual != null) {
            System.out.print(atual.valor);
            if (atual.proximo != null) System.out.print(" <-> ");
            atual = atual.proximo;
        }
        System.out.println(" -> null");
    }

    // 9b. Exibir lista INVERSA (do fim para o início)
    // Mostra: Lista (fim -> início): null <- 3 <-> 2 <-> 1
    public void exibirListaInversa() {
        if (fim == null) {
            System.out.println("Lista vazia!");
            return;
        }
        System.out.print("Lista (fim -> início): null <- ");
        No atual = fim;
        while (atual != null) {
            System.out.print(atual.valor);
            if (atual.anterior != null) System.out.print(" <-> ");
            atual = atual.anterior;
        }
        System.out.println();
    }

    // 10. Pesquisar elemento
    // Percorre do início até achar, retorna posição ou -1
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