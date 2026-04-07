public class Main {
    public static void main(String[] args) {
        // Criar uma nova lista encadeada
        ListaEncadeada lista = new ListaEncadeada();

        System.out.println("=== Demonstracao da Lista Encadeada ===\n");

        // 1. Inserir elementos no inicio
        System.out.println("Inserindo 10, 20, 30 no inicio:");
        lista.inserir_inicio(10);
        lista.inserir_inicio(20);
        lista.inserir_inicio(30);
        lista.imprimir();
        System.out.println("Quantidade: " + lista.qnt_atual() + "\n");

        // 2. Inserir elementos no fim
        System.out.println("Inserindo 40, 50 no fim:");
        lista.remover_fim(40);  // metodo remover_fim na verdade insere no fim
        lista.remover_fim(50);
        lista.imprimir();
        System.out.println("Quantidade: " + lista.qnt_atual() + "\n");

        // 3. Inserir em posicao especifica
        System.out.println("Inserindo 99 na posicao 2:");
        lista.inserir_posicao(99, 2);
        lista.imprimir();
        System.out.println("Quantidade: " + lista.qnt_atual() + "\n");

        // 4. Pesquisar elemento
        System.out.println("Pesquisando elemento 99:");
        lista.pesquisar(99);
        System.out.println();

        // 5. Remover do inicio
        System.out.println("Removendo do inicio:");
        lista.remover_inicio();
        lista.imprimir();
        System.out.println("Quantidade: " + lista.qnt_atual() + "\n");

        // 6. Remover do fim
        System.out.println("Removendo do fim:");
        lista.remover_fim();
        lista.imprimir();
        System.out.println("Quantidade: " + lista.qnt_atual() + "\n");

        // 7. Remover elemento especifico
        System.out.println("Removendo elemento 99:");
        lista.remover_elemento(99);
        lista.imprimir();
        System.out.println("Quantidade: " + lista.qnt_atual() + "\n");

        // 8. Esvaziar lista
        System.out.println("Esvaziando a lista:");
        lista.lista_vazia();
        System.out.println("Quantidade apos esvaziar: " + lista.qnt_atual());
    }
}