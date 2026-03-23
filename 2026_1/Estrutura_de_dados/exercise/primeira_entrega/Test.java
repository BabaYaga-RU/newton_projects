import java.util.Random;
import java.util.Arrays;
import java.util.Scanner;

/*
5. Implemente dois algoritmos que ordenem os elementos de um vetor em ordem 
crescente e compare o número de trocas que eles efetuam durante a ordenação de:

a) um vetor criado com os números de 1 até 100 aleatoriamente distribuídos.
b) um vetor criado com os números de 1 até 100 ordenados em ordem decrescente
*/

public class Test {

    public static void ordenar(int[] vetor){
        int contagem = 0;
        while(true){
            boolean pronto = true;
            for (int i = 0; i < 99; i++){
                if (vetor[i] > vetor[i + 1]){
                    int save = vetor[i] ;
                    vetor[i] = vetor[i + 1];
                    vetor[i + 1] = save;
                    pronto = false;
                    contagem ++;
                }
            }
            if (pronto == true){
                break;
            }
        }
        System.out.println("Vetor ordenado: " + Arrays.toString(vetor));
        System.out.println("Quantidade de movimentos: " + contagem);
    }
    public static void main(String[] args) {
        try{
            Random random = new Random();
            int[] vetor_um = new int[100];
            int indice = 0;
            while(true){
                int valor_atual = random.nextInt(100);
                boolean contem = false;
                boolean final_vetor = true;
                for (int i = 0; i < 100; i++){
                    if (vetor_um[i] == valor_atual + 1){
                        contem = true;
                    }
                    if (vetor_um[i] == 0){
                        final_vetor = false;
                    }
                }
                if (final_vetor == true){
                    break;
                }
                if (contem == false){
                    vetor_um[indice] = valor_atual + 1;
                    indice ++;
                }
            }
            System.out.println("Primeiro vetor: " + Arrays.toString(vetor_um));
            int[] vetor_dois = new int[100];
            indice = 0;
            for (int i = 100; i > 0; i--){
                vetor_dois[indice] = i;
                indice ++;
            }
            System.out.println("Segundo vetor: " + Arrays.toString(vetor_dois));
            System.out.println("Segundo vetor: " + Arrays.toString(vetor_dois));
            System.out.println("a) um vetor criado com os números de 1 até 100 aleatoriamente distribuídos.");
            ordenar(vetor_um);
            System.out.println("b) um vetor criado com os números de 1 até 100 ordenados em ordem decrescente");
            ordenar(vetor_dois);
            

        }catch(Exception e){}
    }
}