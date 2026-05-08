// Prazo: 06/04/2026
/*
1. Implemente a classe ListaDuplamenteEncadeada para armazenar valores inteiros 
usando referências para ligar os elementos da lista.
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


public class Main {
    public static void main(String[] args) {
        ListaDuplamenteEncadeada lista = new ListaDuplamenteEncadeada();

        lista.inserirInicio(10);
        lista.inserirInicio(20);
        lista.inserirInicio(30);
        lista.imprimir();
        System.out.println("Quantidade: " + lista.qntAtual());

        lista.inserirFim(40);
        lista.inserirFim(50);
        lista.imprimir();
        System.out.println("Quantidade: " + lista.qntAtual());

        lista.inserirPosicao(99, 2);
        lista.imprimir();
        System.out.println("Quantidade: " + lista.qntAtual());

        System.out.println("Pesquisar 99: " + lista.pesquisar(99));

        lista.removerInicio();
        lista.imprimir();
        System.out.println("Quantidade: " + lista.qntAtual());

        lista.removerFim();
        lista.imprimir();
        System.out.println("Quantidade: " + lista.qntAtual());

        lista.removerElemento(99);
        lista.imprimir();
        System.out.println("Quantidade: " + lista.qntAtual());

        lista.removerPosicao(1);
        lista.imprimir();
        System.out.println("Quantidade: " + lista.qntAtual());

        lista.listaVazia();
        System.out.println("Quantidade apos esvaziar: " + lista.qntAtual());
    }
}