// Prazo: 22/03/2026

import java.util.Random;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static boolean ehPar(int dado) {
        return dado % 2 == 0;
    }
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
        int Exercicio = 1;
        System.out.println("====================== Exercicio " + Exercicio + " ======================");
        /*
        1. Escreva um programa que leia dois vetores inteiros com dez posições cada. 
        A partir desses vetores, carregue um terceiro vetor onde o valor de cada elemento 
        será a média dos elementos de mesmo índice nos dois vetores anteriores.
        */
        try{
            double[] vetor_um = {6, 19, 184, 310, 12, 13, 28, 333, 666, 17};
            double[] vetor_dois = {21, 16, 1, 15, 27, 5, 11, 33, 22, 4};
            double[] vetor_tres = new double[10];
            for (int i = 0; i < vetor_um.length; i ++){
                vetor_tres[i] = (vetor_um[i] + vetor_dois[i]) / 2;
            }
            System.out.println(Arrays.toString(vetor_tres));
        }catch(Exception e){}
        Exercicio ++;
        System.out.println("====================== Exercicio " + Exercicio + " ======================");
        /*
        2. Escreva um programa que carregue um vetor inteiro de cem posições com números 
        aleatórios entre 0 e 100. Percorrendo o vetor criado apenas uma vez, imprima a 
        posição onde ocorre o menor o valor, a soma dos números armazenados e preencha 
        os valores de um novo vetor com metade do tamanho do vetor original onde a primeira 
        posição do novo vetor é igual à soma da primeira e da última posição do vetor original. 
        A segunda posição do novo vetor é a soma da segunda e da penúltima posição do 
        vetor original e assim em diante.
        */
        try{
            Random random = new Random();
            int[] vetor = new int[100];
            for (int i = 0; i < 100; i ++){
                vetor[i] = random.nextInt(100);
            }
            int menor_valor = 101;
            int menor_indice = 0;
            int numeros_armazenados = 0;
            int[] segundo_vetor = new int[50];
            int indice = 99;
            for (int i = 0; i < 100; i ++){
                if (vetor[i] < menor_valor){
                    menor_valor = vetor[i];
                    menor_indice = i;
                }
                numeros_armazenados += vetor[i];
                if (i < 50){
                    segundo_vetor[i] = vetor[i] + vetor[indice];
                }
            }
            System.out.println("Vetor gerado: " + Arrays.toString(vetor));
            System.out.println("Menor valor no indice: " + menor_indice + " (Valor: " + menor_valor + ")");
            System.out.println("Somatoria dos numeros armazenados: " + numeros_armazenados);
            System.out.println("Novo Vetor: " + Arrays.toString(segundo_vetor));
        }catch(Exception e){}
        Exercicio ++;
        System.out.println("====================== Exercicio " + Exercicio + " ======================");
        /*
        3. Escreva um programa que carregue dois vetores inteiros com 5 posições, sendo 
        um com números pares e o outro com números ímpares. O usuário pode digitar os 
        números em qualquer sequência e o programa deverá armazená-los no vetor correto 
        na ordem em que foram informados pelo usuário.
        */
        try{
            Scanner scn = new Scanner(System.in);
            int[] impar = new int[5];
            int[] par = new int[5];
            int entrada = 0;
            int indicePar = 0;
            int indiceImpar = 0;
            while(true){
                if (indicePar == 5 & indiceImpar == 5){
                    break;
                }
                System.out.print("Insira um numero inteiro: ");
                entrada = scn.nextInt();
                if (ehPar(entrada) == true){
                    if (indicePar == 5){
                        System.out.println("Vetor Par completo");
                    }else {
                        par[indicePar] = entrada;
                        indicePar ++;
                    }
                }else{
                    if (indiceImpar == 5){
                        System.out.println("Vetor Impar completo");
                    }else {
                        impar[indiceImpar] = entrada;
                        indiceImpar ++;
                    }
                }
            }
            System.out.println("Vetor impar: " + Arrays.toString(impar));
            System.out.println("Vetor par: " + Arrays.toString(par));
            scn.close();
        }catch(Exception e){}
        Exercicio ++;
        System.out.println("====================== Exercicio " + Exercicio + " ======================");
        /*
        4. Escreva um programa que ordene um vetor de tamanho arbitrário preenchido com 
        números aleatórios e execute a pesquisa por um valor passado como parâmetro 
        utilizando o algoritmo da busca binária.
        */
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
            Arrays.sort(vetor);
            int inicio = 0;
            int fim = tamanho_vetor - 1;
            while (inicio <= fim) {
                int meio = (inicio + fim) / 2;
                if (vetor[meio] == numero_desejado) {
                    System.out.println("Vetor gerado: " + Arrays.toString(vetor));
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
        Exercicio ++;
        System.out.println("====================== Exercicio " + Exercicio + " ======================");
        /*
        5. Implemente dois algoritmos que ordenem os elementos de um vetor em ordem 
        crescente e compare o número de trocas que eles efetuam durante a ordenação de:

        a) um vetor criado com os números de 1 até 100 aleatoriamente distribuídos.
        b) um vetor criado com os números de 1 até 100 ordenados em ordem decrescente
        */
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
            System.out.println("a) um vetor criado com os números de 1 até 100 aleatoriamente distribuídos.");
            ordenar(vetor_um);
            System.out.println("b) um vetor criado com os números de 1 até 100 ordenados em ordem decrescente");
            ordenar(vetor_dois);
            
        }catch(Exception e){}
    }
}