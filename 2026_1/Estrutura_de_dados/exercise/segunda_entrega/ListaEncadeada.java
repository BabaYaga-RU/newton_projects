public class ListaEncadeada {
    int[] lista;
    int gasto;
    int limite;

    public ListaEncadeada(){
/*
1. Implemente a classe ListaEncadeada utilizando um arranjo de inteiros para
armazenar os elementos da lista.
*/
        gasto = 0;
        limite = 10;
        lista = new int[limite];
    }
    public void AumentarTamanho(){
        limite *= 2;
        int[] _lista = new int[limite];
        for (int i = 0; i > gasto; i++){
            _lista[i] = lista[i];
        }
        lista = _lista;
    }
    public void lista_vazia(){
//2. Crie um método para criar uma lista vazia.
        gasto = 0;
    }
// 3. Crie um método responsável por inserir um elemento no início da lista.
    public void inserir_inicio(int dado){
        if (gasto == limite) AumentarTamanho();
        for (int i = gasto; i > 0; i--){
            lista[i] = lista[i - 1];
        }
        lista[0] = dado;
        gasto ++;
    }
//4. Crie um método responsável por inserir um elemento no fim da lista.
    public void remover_fim(int dado){
        if (gasto == limite) AumentarTamanho();
        lista[gasto] = dado;
        gasto ++;
    }
//5. Crie um método responsável por inserir um elemento em uma posição específica da lista.
    public void inserir_posicao (int dado, int posicao){
        if (gasto == limite) AumentarTamanho();
        for (int i = gasto - 1; i > posicao; i--) lista[i + 1] = lista[i];
        lista[posicao] = dado;
        gasto ++;
    }
//6. Crie um método responsável por remover um elemento no início da lista.
    public void remover_inicio(){
        for (int i = 0; i < gasto; i++) lista[i] = lista[i + 1];
        gasto --;
    }
//7. Crie um método responsável por remover um elemento no fim da lista.
    public void remover_fim(){
        gasto --;
    }
//8. Crie um método responsável por remover um elemento em uma posição específica da lista.
    public void remover_posicao (int posicao){
        for (int i = gasto - 1; i > posicao; i--) lista[i - 1] = lista[i];
        gasto --;
    }
//9. Crie um método responsável por remover um elemento específico da lista.
    public void remover_elemento(int elemento){
       for(int i = 0; i < gasto; i++){
        if (lista[i] == elemento) remover_posicao(i);
       }
       gasto --;
    }
//10. Crie um método para exibir o conteúdo de uma lista.
    public void imprimir(){for(int i = 0; i < gasto; i++) System.out.println(lista[i]);}
/*
11. Crie um método para pesquisar por um elemento específico em uma lista e
informar, caso o elemento exista, a posição na qual ele está armazenado.
*/
    public void pesquisar(int elemento){

        for(int i = 0; i < gasto; i++){
            if (lista[i] == elemento) {
                System.out.println("Item encontrado, posicao " + i);
            }
        }
    }

//12. Crie um método que retorne o número de elementos existentes na lista.
}