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
    public void inicio(int dado){
        if (gasto == limite) AumentarTamanho();
        for (int i = gasto; i > 0; i--){
            lista[i + 1] = lista[i];
        }
        lista[0] = dado;
        gasto ++;
    }
//4. Crie um método responsável por inserir um elemento no fim da lista.
    public void fim(int dado){
        if (gasto == limite) AumentarTamanho();
        lista[gasto + 1] = dado;
        gasto ++;
    }
//5. Crie um método responsável por inserir um elemento em uma posição específica da lista.

//6. Crie um método responsável por remover um elemento no início da lista.

//7. Crie um método responsável por remover um elemento no fim da lista.

//8. Crie um método responsável por remover um elemento em uma posição específica da lista.

//9. Crie um método responsável por remover um elemento específico da lista.

//10. Crie um método para exibir o conteúdo de uma lista.

/*
11. Crie um método para pesquisar por um elemento específico em uma lista e
informar, caso o elemento exista, a posição na qual ele está armazenado.
*/

//12. Crie um método que retorne o número de elementos existentes na lista.
}