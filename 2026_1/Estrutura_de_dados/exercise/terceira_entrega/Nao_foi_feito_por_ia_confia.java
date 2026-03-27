/**
 * Lista Encadeada - Implementação completa com explicações detalhadas
 * 
 * Esta classe implementa uma lista encadeada simples para armazenar valores inteiros.
 * Cada elemento da lista é representado por um nó que contém um valor e uma referência
 * para o próximo nó na lista.
 * 
 * @author Desenvolvido manualmente - NÃO foi feito por IA
 */
public class Nao_foi_feito_por_ia_confia {
    
    /**
     * Classe interna que representa um nó da lista encadeada.
     * Cada nó contém um valor inteiro e uma referência para o próximo nó.
     */
    private class No {
        private int valor;  // Valor armazenado no nó
        private No proximo; // Referência para o próximo nó na lista
        
        /**
         * Construtor do nó
         * @param valor Valor a ser armazenado no nó
         */
        public No(int valor) {
            this.valor = valor;
            this.proximo = null; // Inicialmente, não aponta para nenhum próximo nó
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
    }
    
    private No cabeca; // Referência para o primeiro nó da lista
    private int tamanho; // Número de elementos na lista
    
    /**
     * 2. Cria uma lista vazia
     * Inicializa a lista com a cabeça nula e tamanho zero
     */
    public Nao_foi_feito_por_ia_confia() {
        this.cabeca = null;
        this.tamanho = 0;
        System.out.println("Lista vazia criada com sucesso!");
    }
    
    /**
     * 3. Insere um elemento no início da lista
     * Este método tem complexidade O(1) pois não depende do tamanho da lista
     * @param valor Valor a ser inserido no início
     */
    public void inserirNoInicio(int valor) {
        // Passo 1: Cria um novo nó com o valor fornecido
        No novoNo = new No(valor);
        
        // Passo 2: O novo nó aponta para a antiga cabeça
        novoNo.setProximo(cabeca);
        
        // Passo 3: Atualiza a cabeça para apontar para o novo nó
        cabeca = novoNo;
        
        // Passo 4: Incrementa o tamanho da lista
        tamanho++;
        
        System.out.println("Elemento " + valor + " inserido no início da lista.");
    }
    
    /**
     * 4. Insere um elemento no fim da lista
     * Este método tem complexidade O(n) pois precisa percorrer toda a lista
     * @param valor Valor a ser inserido no fim
     */
    public void inserirNoFim(int valor) {
        // Passo 1: Cria um novo nó com o valor fornecido
        No novoNo = new No(valor);
        
        // Passo 2: Se a lista estiver vazia, o novo nó se torna a cabeça
        if (cabeca == null) {
            cabeca = novoNo;
        } else {
            // Passo 3: Percorre a lista até encontrar o último nó
            No atual = cabeca;
            while (atual.getProximo() != null) {
                atual = atual.getProximo();
            }
            
            // Passo 4: O último nó aponta para o novo nó
            atual.setProximo(novoNo);
        }
        
        // Passo 5: Incrementa o tamanho da lista
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
        
        // Passo 5: Percorre a lista até a posição anterior à desejada
        No atual = cabeca;
        for (int i = 0; i < posicao - 1; i++) {
            atual = atual.getProximo();
        }
        
        // Passo 6: O novo nó aponta para o próximo do nó atual
        novoNo.setProximo(atual.getProximo());
        
        // Passo 7: O nó atual aponta para o novo nó
        atual.setProximo(novoNo);
        
        // Passo 8: Incrementa o tamanho da lista
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
        
        // Passo 3: Move a cabeça para o próximo nó
        cabeca = cabeca.getProximo();
        
        // Passo 4: Decrementa o tamanho da lista
        tamanho--;
        
        System.out.println("Elemento " + valor + " removido do início da lista.");
        return valor;
    }
    
    /**
     * 7. Remove um elemento no fim da lista
     * Este método tem complexidade O(n) pois precisa percorrer até o penúltimo nó
     * @return Valor do elemento removido
     * @throws IllegalStateException Se a lista estiver vazia
     */
    public int removerDoFim() {
        // Passo 1: Verifica se a lista está vazia
        if (cabeca == null) {
            throw new IllegalStateException("Lista está vazia!");
        }
        
        // Passo 2: Se houver apenas um elemento, remove do início
        if (cabeca.getProximo() == null) {
            return removerDoInicio();
        }
        
        // Passo 3: Percorre a lista até o penúltimo nó
        No atual = cabeca;
        while (atual.getProximo().getProximo() != null) {
            atual = atual.getProximo();
        }
        
        // Passo 4: Obtém o valor do último nó
        int valor = atual.getProximo().getValor();
        
        // Passo 5: O penúltimo nó aponta para null (remove a referência ao último)
        atual.setProximo(null);
        
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
        
        // Passo 3: Percorre a lista até a posição anterior à desejada
        No atual = cabeca;
        for (int i = 0; i < posicao - 1; i++) {
            atual = atual.getProximo();
        }
        
        // Passo 4: Obtém o valor do nó a ser removido
        int valor = atual.getProximo().getValor();
        
        // Passo 5: O nó atual aponta para o nó após o que será removido
        atual.setProximo(atual.getProximo().getProximo());
        
        // Passo 6: Decrementa o tamanho da lista
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
        
        // Passo 3: Percorre a lista procurando o elemento
        No atual = cabeca;
        while (atual.getProximo() != null && atual.getProximo().getValor() != valor) {
            atual = atual.getProximo();
        }
        
        // Passo 4: Se encontrou o elemento
        if (atual.getProximo() != null) {
            // Passo 5: O nó atual aponta para o nó após o que será removido
            atual.setProximo(atual.getProximo().getProximo());
            
            // Passo 6: Decrementa o tamanho da lista
            tamanho--;
            
            System.out.println("Elemento " + valor + " removido da lista.");
            return true;
        }
        
        // Passo 7: Elemento não encontrado
        System.out.println("Elemento " + valor + " não encontrado na lista.");
        return false;
    }
    
    /**
     * 10. Exibe o conteúdo da lista
     * Este método tem complexidade O(n)
     */
    public void exibirLista() {
        // Passo 1: Verifica se a lista está vazia
        if (cabeca == null) {
            System.out.println("Lista vazia!");
            return;
        }
        
        // Passo 2: Percorre a lista exibindo cada elemento
        System.out.print("Lista: ");
        No atual = cabeca;
        while (atual != null) {
            System.out.print(atual.getValor());
            if (atual.getProximo() != null) {
                System.out.print(" -> ");
            }
            atual = atual.getProximo();
        }
        System.out.println(" -> null");
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
     * Exemplo de uso da lista encadeada
     */
    public static void main(String[] args) {
        System.out.println("=== Testando Lista Encadeada ===\n");
        
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
        
        // Testando remoção do início
        System.out.println("6. Testando remoção do início:");
        lista.removerDoInicio();
        lista.exibirLista();
        System.out.println();
        
        // Testando remoção do fim
        System.out.println("7. Testando remoção do fim:");
        lista.removerDoFim();
        lista.exibirLista();
        System.out.println();
        
        // Testando remoção em posição específica
        System.out.println("8. Testando remoção em posição específica:");
        lista.removerEmPosicao(1);
        lista.exibirLista();
        System.out.println();
        
        // Testando remoção de elemento específico
        System.out.println("9. Testando remoção de elemento específico:");
        lista.removerElemento(4);
        lista.exibirLista();
        System.out.println();
        
        // Testando tamanho final
        System.out.println("10. Tamanho final da lista:");
        lista.getTamanho();
        
        System.out.println("\n=== Testes concluídos com sucesso! ===");
    }
}