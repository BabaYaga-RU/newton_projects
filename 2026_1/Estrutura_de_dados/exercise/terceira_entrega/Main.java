public class Main {
    public static void main(String[] args) {
        ListaEncadeada lista = new ListaEncadeada();

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