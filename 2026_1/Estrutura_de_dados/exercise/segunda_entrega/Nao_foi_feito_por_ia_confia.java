/*
 * Lista baseada em array (Array)
 * 
 * Em vez de usar nós encadeados, esta lista usa um array (array) de inteiros.
 * É como uma fila numerada: cada elemento tem uma POSIÇÃO fixa (0, 1, 2, ...).
 * 
 * Quando o array enche, criamos um NOVO array maior e copiamos os elementos.
 * 
 * Vantagem: acesso rápido por posição (elementos[i] pega o elemento na posição i)
 * Desvantagem: inserir/remover no início é lento (precisa mover todos os elementos)
 * 
 * Exercícios:
1. Implemente a classe ListaEncadeada utilizando um array de inteiros para
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

    // =========================== ATRIBUTOS ===========================
    int[] elementos;   // o array que guarda os números
    int tamanho;       // quantos elementos têm (próxima posição vazia)
    int capacidade;    // tamanho máximo do array atual

    // =========================== CONSTRUTOR ===========================
    // 1. Construtor: cria array com capacidade inicial de 10
    public Nao_foi_feito_por_ia_confia() {
        capacidade = 10;
        elementos = new int[capacidade];
        tamanho = 0;
    }

    // =========================== MÉTODOS AUXILIARES ===========================
    // Redimensionar: quando array enche, dobra a capacidade
    // Cria novo array maior e copia os elementos
    void redimensionar() {
        capacidade *= 2;  // dobra capacidade
        int[] novoarray = new int[capacidade];
        // Copia elementos do array antigo para o novo
        for (int i = 0; i < tamanho; i++) {
            novoarray[i] = elementos[i];
        }
        elementos = novoarray;  // troca referência
    }

    // Cria lista vazia (reseta o tamanho para 0)
    public void criarListaVazia() {
        tamanho = 0;
    }

    // =========================== MÉTODOS DE INSERÇÃO ===========================
    // 2. Inserir no INÍCIO
    // Abre espaço na posição 0 movendo todos os elementos para a direita
    public void inserirNoInicio(int elemento) {
        if (tamanho == capacidade) {  // se cheio, aumenta array
            redimensionar();
        }
        // Move todos os elementos uma posição para a direita
        for (int i = tamanho; i > 0; i--) {
            elementos[i] = elementos[i - 1];
        }
        elementos[0] = elemento;  // coloca novo elemento na posição 0
        tamanho++;
    }

    // 3. Inserir no FIM
    // Coloca elemento na próxima posição disponível (tamanho)
    public void inserirNoFim(int elemento) {
        if (tamanho == capacidade) {  // se cheio, aumenta array
            redimensionar();
        }
        elementos[tamanho] = elemento;  // coloca na posição 'tamanho'
        tamanho++;
    }

    // 4. Inserir em POSIÇÃO específica
    // Move elementos da posição em diante para a direita, abre espaço
    public void inserirEmPosicao(int posicao, int elemento) {
        if (posicao < 0 || posicao > tamanho) {
            throw new IndexOutOfBoundsException("Posição inválida: " + posicao);
        }
        if (tamanho == capacidade) {
            redimensionar();
        }

        // Move elementos da posição em diante para a direita
        for (int i = tamanho; i > posicao; i--) {
            elementos[i] = elementos[i - 1];
        }
        elementos[posicao] = elemento;
        tamanho++;
    }

    // =========================== MÉTODOS DE REMOÇÃO ===========================
    // 5. Remover do INÍCIO
    // Pega elemento da posição 0, move todos para a esquerda
    public int removerDoInicio() {
        if (tamanho == 0) {
            throw new IllegalStateException("Lista vazia");
        }
        int elemento = elementos[0];  // guarda valor que será removido
        // Move todos os elementos uma posição para a esquerda
        for (int i = 0; i < tamanho - 1; i++) {
            elementos[i] = elementos[i + 1];
        }
        tamanho--;
        return elemento;
    }

    // 6. Remover do FIM
    // Simplesmente diminui o tamanho (última posição vira "vazia")
    public int removerDoFim() {
        if (tamanho == 0) {
            throw new IllegalStateException("Lista vazia");
        }
        tamanho--;  // diminui tamanho
        return elementos[tamanho];  // retorna o último elemento
    }

    // 7. Remover de POSIÇÃO específica
    // Move elementos da posição em diante para a esquerda, fechando o buraco
    public int removerEmPosicao(int posicao) {
        if (posicao < 0 || posicao >= tamanho) {
            throw new IndexOutOfBoundsException("Posição inválida: " + posicao);
        }
        int elemento = elementos[posicao];  // guarda valor que será removido
        // Move elementos da posição em diante para a esquerda
        for (int i = posicao; i < tamanho - 1; i++) {
            elementos[i] = elementos[i + 1];
        }
        tamanho--;
        return elemento;
    }

    // 8. Remover ELEMENTO específico (pelo valor)
    // Procura o valor no array e remove pela posição
    public boolean removerElemento(int elemento) {
        for (int i = 0; i < tamanho; i++) {
            if (elementos[i] == elemento) {
                removerEmPosicao(i);  // remove pela posição encontrada
                return true;
            }
        }
        return false;  // não achou
    }

    // =========================== MÉTODOS DE CONSULTA ===========================
    // 11. Retornar tamanho
    public int tamanho() {
        return tamanho;
    }

    // 10. Pesquisar elemento
    // Procura no array, retorna a POSIÇÃO ou -1 se não achou
    public int pesquisarElemento(int elemento) {
        for (int i = 0; i < tamanho; i++) {
            if (elementos[i] == elemento) {  // achou, retorna posição
                return i;
            }
        }
        return -1;  // não achou
    }

    // 9. Exibir lista
    // Mostra: [1, 2, 3]
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

    // =========================== MÉTODO PRINCIPAL ===========================
    public static void main(String[] args) {
        System.out.println("=== Testando Lista Baseada em Array ===\n");
        
        // Criar lista vazia
        Nao_foi_feito_por_ia_confia lista = new Nao_foi_feito_por_ia_confia();
        System.out.println("1. Lista criada (vazia):");
        lista.exibirLista();
        System.out.println("Tamanho: " + lista.tamanho());
        
        // Inserir no fim
        System.out.println("\n2. Inserindo elementos no fim: 10, 20, 30");
        lista.inserirNoFim(10);
        lista.inserirNoFim(20);
        lista.inserirNoFim(30);
        lista.exibirLista();
        System.out.println("Tamanho: " + lista.tamanho());
        
        // Inserir no início
        System.out.println("\n3. Inserindo elemento no início: 5");
        lista.inserirNoInicio(5);
        lista.exibirLista();
        
        // Inserir em posição específica
        System.out.println("\n4. Inserindo elemento 15 na posição 2");
        lista.inserirEmPosicao(2, 15);
        lista.exibirLista();
        
        // Pesquisar elemento
        System.out.println("\n5. Pesquisando elemento 15:");
        int posicao = lista.pesquisarElemento(15);
        System.out.println("Elemento 15 está na posição: " + posicao);
        
        // Remover do início
        System.out.println("\n6. Removendo elemento do início:");
        int removido = lista.removerDoInicio();
        System.out.println("Elemento removido: " + removido);
        lista.exibirLista();
        
        // Remover do fim
        System.out.println("\n7. Removendo elemento do fim:");
        removido = lista.removerDoFim();
        System.out.println("Elemento removido: " + removido);
        lista.exibirLista();
        
        // Remover elemento específico (pelo valor)
        System.out.println("\n8. Removendo elemento 15 (pelo valor):");
        boolean removidoB = lista.removerElemento(15);
        System.out.println("Elemento removido com sucesso: " + removidoB);
        lista.exibirLista();
        
        // Remover em posição específica
        System.out.println("\n9. Removendo elemento da posição 1:");
        removido = lista.removerEmPosicao(1);
        System.out.println("Elemento removido: " + removido);
        lista.exibirLista();
        
        // Criar lista vazia (resetar)
        System.out.println("\n10. Criando lista vazia (reset):");
        lista.criarListaVazia();
        lista.exibirLista();
        System.out.println("Tamanho: " + lista.tamanho());
        
        // Testar redimensionamento (adicionar mais de 10 elementos)
        System.out.println("\n11. Testando redimensionamento (adicionando 12 elementos):");
        for (int i = 1; i <= 12; i++) {
            lista.inserirNoFim(i * 10);
        }
        lista.exibirLista();
        System.out.println("Tamanho: " + lista.tamanho());
        
        System.out.println("\n=== Todos os testes concluídos! ===");
    }
}