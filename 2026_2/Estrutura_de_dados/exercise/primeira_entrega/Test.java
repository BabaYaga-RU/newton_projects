import java.util.Random;
import java.util.Arrays;
import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        try{
            Random random = new Random();
            int tamanho_vetor = 0;
            while(true){
                tamanho_vetor = random.nextInt(100);
                if (tamanho_vetor != 0){
                    break;
                }
            }
            int[] vetor = new int[tamanho_vetor];
            for (int i = 0; i < tamanho_vetor; i++){
                vetor[i] = random.nextInt(100);
            }
            // Numero escolhido para procura
            int numero_desejado = vetor[random.nextInt(tamanho_vetor)];
            System.out.println("Vetor gerado: " + Arrays.toString(vetor));
            Arrays.sort(vetor);
            int inicio = 0;
            int fim = tamanho_vetor - 1;
            while (inicio <= fim) {
                int meio = (inicio + fim) / 2;
                if (vetor[meio] == numero_desejado) {
                    System.out.println("Numero desejado: " + numero_desejado + " Numero encontrado: " + vetor[meio]);
                    break; 
                }
                if (vetor[meio] < numero_desejado) {
                    inicio = meio + 1;
                } 
                else {
                    fim = meio - 1;
                }
            }
        }catch(Exception e){}
    }
}