/**
 * Lista Duplamente Encadeada - Implementação completa com explicações detalhadas
 * 
 * Esta classe implementa uma lista duplamente encadeada para armazenar valores inteiros.
 * Cada elemento da lista é representado por um nó que contém um valor e duas referências:
 * uma para o próximo nó e outra para o nó anterior na lista.
 * 
 * @author Desenvolvido manualmente - NÃO foi feito por IA
 */
public class Nao_foi_feito_por_ia_confia {
    
    /**
     * Classe interna que representa um nó da lista duplamente encadeada.
     * Cada nó contém um valor inteiro e duas referências: uma para o próximo nó
     * e outra para o nó anterior.
     */
    private class No {
        private int valor;     // Valor armazenado no nó
        private No proximo;    // Referência para o próximo nó na lista
        private No anterior;   // Referência para o nó anterior na lista
        
        /**
         * Construtor do nó
         * @param valor Valor a ser armazenado no nó
         */
        public No(int valor) {
            this.valor = valor;
            this.proximo = null;  // Inicialmente, não aponta para nenhum próximo nó
            this.anterior = null; // Inicialmente, não aponta para nenhum nó anterior
        }
        
        /**
         * Obtém o valor armazenado no nó
         * @return Valor do nó
         */
        public int getValor() {
            return valor;
        }
        
        /**
         * Obtém a referência para o próximo nó
         * @return Referência para o próximo nó
         */
        public No getProximo() {
            return proximo;
        }
        
        /**
         * Define a referência para o próximo nó
         * @param proximo Referência para o próximo nó
         */
        public void setProximo(No proximo) {
            this.proximo = proximo;
        }
        
        /**
         * Obtém a referência para o nó anterior
         * @return Referência para o nó anterior
         */
        public No getAnterior() {
            return anterior;
        }
        
        /**
         * Define a referência para o nó anterior
         * @param anterior Referência para o nó anterior
         */
        public void setAnterior(No anterior) {
            this.anterior = anterior;
        }
    }
    
    private No cabeca;   // Referência para o primeiro nó da lista
    private No cauda;    // Referência para o último nó da lista
    private int tamanho; // Número de elementos na lista
    
    /**
     * 2. Cria uma lista vazia
     * Inicializa a lista com a cabeça e cauda nulas e tamanho zero
     */
    public Nao_foi_feito_por_ia_confia() {
        this.cabeca = null;
        this.cauda = null;
        this.tamanho = 0;
        System.out.println("Lista duplamente encadeada vazia criada com sucesso!");
    }
    
    /**
     * 3. Insere um elemento no início da lista
     * Este método tem complexidade O(1) pois não depende do tamanho da lista
     * @param valor Valor a ser inserido no início
     */
    public void inserirNoInicio(int valor) {
        // Passo 1: Cria um novo nó com o valor fornecido
        No novoNo = new No(valor);
        
        // Passo 2: Se a lista estiver vazia
        if (cabeca == null) {
            // O novo nó se torna tanto a cabeça quanto a cauda
            cabeca = novoNo;
            cauda = novoNo;
        } else {
            // Passo 3: O novo nó aponta para a antiga cabeça
            novoNo.setProximo(cabeca);
            
            // Passo 4: A antiga cabeça aponta para o novo nó como anterior
            cabeca.setAnterior(novoNo);
            
            // Passo 5: Atualiza a cabeça para apontar para o novo nó
            cabeca = novoNo;
        }
        
        // Passo 6: Incrementa o tamanho da lista
        tamanho++;
        
        System.out.println("Elemento " + valor + " inserido no início da lista.");
    }
    
    /**
     * 4. Insere um elemento no fim da lista
     * Este método tem complexidade O(1) pois não depende do tamanho da lista
     * @param valor Valor a ser inserido no fim
     */
    public void inserirNoFim(int valor) {
        // Passo 1: Cria um novo nó com o valor fornecido
        No novoNo = new No(valor);
        
        // Passo 2: Se a lista estiver vazia
        if (cabeca == null) {
            // O novo nó se torna tanto a cabeça quanto a cauda
            cabeca = novoNo;
            cauda = novoNo;
        } else {
            // Passo 3: A cauda atual aponta para o novo nó como próximo
            cauda.setProximo(novoNo);
            
            // Passo 4: O novo nó aponta para a cauda atual como anterior
            novoNo.setAnterior(cauda);
            
            // Passo 5: Atualiza a cauda para apontar para o novo nó
            cauda = novoNo;
        }
        
        // Passo 6: Incrementa o tamanho da lista
        tamanho++;
        
        System.out.println("Elemento " + valor + " inserido no fim da lista.");
    }
    
    /**
     * 5. Insere um elemento em uma posição específica da lista
     * Este método tem complexidade O(n) no pior caso
     * @param posicao Posição onde o elemento será inserido (0-indexado)
     * @param valor Valor a ser inserido
     * @throws IndexOutOfBoundsException Se a posição for inválida
     */
    public void inserirEmPosicao(int posicao, int valor) {
        // Passo 1: Valida a posição
        if (posicao < 0 || posicao > tamanho) {
            throw new IndexOutOfBoundsException("Posição inválida: " + posicao);
        }
        
        // Passo 2: Se a posição for 0, insere no início
        if (posicao == 0) {
            inserirNoInicio(valor);
            return;
        }
        
        // Passo 3: Se a posição for igual ao tamanho, insere no fim
        if (posicao == tamanho) {
            inserirNoFim(valor);
            return;
        }
        
        // Passo 4: Cria o novo nó
        No novoNo = new No(valor);
        
        // Passo 5: Percorre a lista até a posição desejada
        No atual = cabeca;
        for (int i = 0; i < posicao; i++) {
            atual = atual.getProximo();
        }
        
        // Passo 6: O nó anterior ao atual aponta para o novo nó como próximo
        atual.getAnterior().setProximo(novoNo);
        
        // Passo 7: O novo nó aponta para o nó anterior ao atual como anterior
        novoNo.setAnterior(atual.getAnterior());
        
        // Passo 8: O novo nó aponta para o nó atual como próximo
        novoNo.setProximo(atual);
        
        // Passo 9: O nó atual aponta para o novo nó como anterior
        atual.setAnterior(novoNo);
        
        // Passo 10: Incrementa o tamanho da lista
        tamanho++;
        
        System.out.println("Elemento " + valor + " inserido na posição " + posicao + ".");
    }
    
    /**
     * 6. Remove um elemento no início da lista
     * Este método tem complexidade O(1)
     * @return Valor do elemento removido
     * @throws IllegalStateException Se a lista estiver vazia
     */
    public int removerDoInicio() {
        // Passo 1: Verifica se a lista está vazia
        if (cabeca == null) {
            throw new IllegalStateException("Lista está vazia!");
        }
        
        // Passo 2: Obtém o valor da cabeça
        int valor = cabeca.getValor();
        
        // Passo 3: Se houver apenas um elemento
        if (cabeca == cauda) {
            // Ambos cabeça e cauda apontam para null
            cabeca = null;
            cauda = null;
        } else {
            // Passo 4: Move a cabeça para o próximo nó
            cabeca = cabeca.getProximo();
            
            // Passo 5: A nova cabeça não tem nó anterior
            cabeca.setAnterior(null);
        }
        
        // Passo 6: Decrementa o tamanho da lista
        tamanho--;
        
        System.out.println("Elemento " + valor + " removido do início da lista.");
        return valor;
    }
    
    /**
     * 7. Remove um elemento no fim da lista
     * Este método tem complexidade O(1)
     * @return Valor do elemento removido
     * @throws IllegalStateException Se a lista estiver vazia
     */
    public int removerDoFim() {
        // Passo 1: Verifica se a lista está vazia
        if (cabeca == null) {
            throw new IllegalStateException("Lista está vazia!");
        }
        
        // Passo 2: Obtém o valor da cauda
        int valor = cauda.getValor();
        
        // Passo 3: Se houver apenas um elemento
        if (cabeca == cauda) {
            // Ambos cabeça e cauda apontam para null
            cabeca = null;
            cauda = null;
        } else {
            // Passo 4: Move a cauda para o nó anterior
            cauda = cauda.getAnterior();
            
            // Passo 5: A nova cauda não tem próximo nó
            cauda.setProximo(null);
        }
        
        // Passo 6: Decrementa o tamanho da lista
        tamanho--;
        
        System.out.println("Elemento " + valor + " removido do fim da lista.");
        return valor;
    }
    
    /**
     * 8. Remove um elemento em uma posição específica da lista
     * Este método tem complexidade O(n) no pior caso
     * @param posicao Posição do elemento a ser removido (0-indexado)
     * @return Valor do elemento removido
     * @throws IndexOutOfBoundsException Se a posição for inválida
     * @throws IllegalStateException Se a lista estiver vazia
     */
    public int removerEmPosicao(int posicao) {
        // Passo 1: Valida a posição
        if (posicao < 0 || posicao >= tamanho) {
            throw new IndexOutOfBoundsException("Posição inválida: " + posicao);
        }
        
        // Passo 2: Se a posição for 0, remove do início
        if (posicao == 0) {
            return removerDoInicio();
        }
        
        // Passo 3: Se a posição for igual ao tamanho - 1, remove do fim
        if (posicao == tamanho - 1) {
            return removerDoFim();
        }
        
        // Passo 4: Percorre a lista até a posição desejada
        No atual = cabeca;
        for (int i = 0; i < posicao; i++) {
            atual = atual.getProximo();
        }
        
        // Passo 5: Obtém o valor do nó a ser removido
        int valor = atual.getValor();
        
        // Passo 6: O nó anterior ao atual aponta para o próximo do atual
        atual.getAnterior().setProximo(atual.getProximo());
        
        // Passo 7: O nó próximo ao atual aponta para o anterior do atual
        atual.getProximo().setAnterior(atual.getAnterior());
        
        // Passo 8: Decrementa o tamanho da lista
        tamanho--;
        
        System.out.println("Elemento " + valor + " removido da posição " + posicao + ".");
        return valor;
    }
    
    /**
     * 9. Remove um elemento específico da lista
     * Este método tem complexidade O(n) no pior caso
     * @param valor Valor do elemento a ser removido
     * @return true se o elemento foi encontrado e removido, false caso contrário
     */
    public boolean removerElemento(int valor) {
        // Passo 1: Verifica se a lista está vazia
        if (cabeca == null) {
            System.out.println("Lista está vazia, nada a remover.");
            return false;
        }
        
        // Passo 2: Se o elemento a ser removido for a cabeça
        if (cabeca.getValor() == valor) {
            removerDoInicio();
            return true;
        }
        
        // Passo 3: Se o elemento a ser removido for a cauda
        if (cauda.getValor() == valor) {
            removerDoFim();
            return true;
        }
        
        // Passo 4: Percorre a lista procurando o elemento
        No atual = cabeca;
        while (atual != null && atual.getValor() != valor) {
            atual = atual.getProximo();
        }
        
        // Passo 5: Se encontrou o elemento
        if (atual != null) {
            // Passo 6: O nó anterior ao atual aponta para o próximo do atual
            atual.getAnterior().setProximo(atual.getProximo());
            
            // Passo 7: O nó próximo ao atual aponta para o anterior do atual
            atual.getProximo().setAnterior(atual.getAnterior());
            
            // Passo 8: Decrementa o tamanho da lista
            tamanho--;
            
            System.out.println("Elemento " + valor + " removido da lista.");
            return true;
        }
        
        // Passo 9: Elemento não encontrado
        System.out.println("Elemento " + valor + " não encontrado na lista.");
        return false;
    }
    
    /**
     * 10. Exibe o conteúdo da lista (da cabeça para a cauda)
     * Este método tem complexidade O(n)
     */
    public void exibirLista() {
        // Passo 1: Verifica se a lista está vazia
        if (cabeca == null) {
            System.out.println("Lista vazia!");
            return;
        }
        
        // Passo 2: Percorre a lista exibindo cada elemento
        System.out.print("Lista (cabeça -> cauda): ");
        No atual = cabeca;
        while (atual != null) {
            System.out.print(atual.getValor());
            if (atual.getProximo() != null) {
                System.out.print(" <-> ");
            }
            atual = atual.getProximo();
        }
        System.out.println(" -> null");
    }
    
    /**
     * Exibe o conteúdo da lista (da cauda para a cabeça)
     * Este método tem complexidade O(n)
     */
    public void exibirListaInversa() {
        // Passo 1: Verifica se a lista está vazia
        if (cauda == null) {
            System.out.println("Lista vazia!");
            return;
        }
        
        // Passo 2: Percorre a lista exibindo cada elemento
        System.out.print("Lista (cauda -> cabeça): null <- ");
        No atual = cauda;
        while (atual != null) {
            System.out.print(atual.getValor());
            if (atual.getAnterior() != null) {
                System.out.print(" <-> ");
            }
            atual = atual.getAnterior();
        }
        System.out.println();
    }
    
    /**
     * 11. Pesquisa por um elemento específico na lista
     * Este método tem complexidade O(n) no pior caso
     * @param valor Valor a ser pesquisado
     * @return Posição do elemento se encontrado, -1 se não encontrado
     */
    public int pesquisarElemento(int valor) {
        // Passo 1: Verifica se a lista está vazia
        if (cabeca == null) {
            System.out.println("Lista está vazia!");
            return -1;
        }
        
        // Passo 2: Percorre a lista procurando o elemento
        No atual = cabeca;
        int posicao = 0;
        
        while (atual != null) {
            // Passo 3: Se encontrou o elemento, retorna a posição
            if (atual.getValor() == valor) {
                System.out.println("Elemento " + valor + " encontrado na posição " + posicao + ".");
                return posicao;
            }
            atual = atual.getProximo();
            posicao++;
        }
        
        // Passo 4: Elemento não encontrado
        System.out.println("Elemento " + valor + " não encontrado na lista.");
        return -1;
    }
    
    /**
     * 12. Retorna o número de elementos existentes na lista
     * Este método tem complexidade O(1)
     * @return Número de elementos na lista
     */
    public int getTamanho() {
        System.out.println("Número de elementos na lista: " + tamanho);
        return tamanho;
    }
    
    /**
     * Verifica se a lista está vazia
     * @return true se a lista estiver vazia, false caso contrário
     */
    public boolean estaVazia() {
        return cabeca == null;
    }
    
    /**
     * Exemplo de uso da lista duplamente encadeada
     */
    public static void main(String[] args) {
        System.out.println("=== Testando Lista Duplamente Encadeada ===\n");
        
        // Criando uma nova lista
        Nao_foi_feito_por_ia_confia lista = new Nao_foi_feito_por_ia_confia();
        
        // Testando inserção no início
        System.out.println("1. Testando inserção no início:");
        lista.inserirNoInicio(3);
        lista.inserirNoInicio(2);
        lista.inserirNoInicio(1);
        lista.exibirLista();
        System.out.println();
        
        // Testando inserção no fim
        System.out.println("2. Testando inserção no fim:");
        lista.inserirNoFim(5);
        lista.inserirNoFim(6);
        lista.exibirLista();
        System.out.println();
        
        // Testando inserção em posição específica
        System.out.println("3. Testando inserção em posição específica:");
        lista.inserirEmPosicao(3, 4); // Inserindo 4 na posição 3
        lista.exibirLista();
        System.out.println();
        
        // Testando tamanho da lista
        System.out.println("4. Testando tamanho da lista:");
        lista.getTamanho();
        System.out.println();
        
        // Testando pesquisa de elemento
        System.out.println("5. Testando pesquisa de elemento:");
        lista.pesquisarElemento(4);
        lista.pesquisarElemento(10);
        System.out.println();
        
        // Testando exibição inversa
        System.out.println("6. Testando exibição inversa:");
        lista.exibirListaInversa();
        System.out.println();
        
        // Testando remoção do início
        System.out.println("7. Testando remoção do início:");
        lista.removerDoInicio();
        lista.exibirLista();
        System.out.println();
        
        // Testando remoção do fim
        System.out.println("8. Testando remoção do fim:");
        lista.removerDoFim();
        lista.exibirLista();
        System.out.println();
        
        // Testando remoção em posição específica
        System.out.println("9. Testando remoção em posição específica:");
        lista.removerEmPosicao(1);
        lista.exibirLista();
        System.out.println();
        
        // Testando remoção de elemento específico
        System.out.println("10. Testando remoção de elemento específico:");
        lista.removerElemento(4);
        lista.exibirLista();
        System.out.println();
        
        // Testando tamanho final
        System.out.println("11. Tamanho final da lista:");
        lista.getTamanho();
        
        System.out.println("\n=== Testes concluídos com sucesso! ===");
    }
}