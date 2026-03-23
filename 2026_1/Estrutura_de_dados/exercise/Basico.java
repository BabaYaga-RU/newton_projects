import java.util.*; // Importa List, Map, ArrayList, HashMap e Scanner

// Exemplo de POO: Classe para representar uma Matéria
class Materia {
    String nome;
    boolean concluida;

    public Materia(String nome, boolean concluida) {
        this.nome = nome;
        this.concluida = concluida;
    }

    @Override
    public String toString() {
        return (concluida ? "[✓] " : "[ ] ") + nome;
    }
}

public class Basico {
    public static void main(String[] args) {
        // 1. Iniciar Scanner para entrada de dados
        Scanner teclado = new Scanner(System.in);

        // 2. Vetor (Array fixo) - Exemplo de Semestres
        int[] semestres = {1, 2, 3, 4};

        // 3. Lista (ArrayList) - Dinâmica
        List<Materia> listaMaterias = new ArrayList<>();
        listaMaterias.add(new Materia("Algoritmos", true));
        listaMaterias.add(new Materia("Estrutura de Dados", false));

        // 4. Map (Chave-Valor) - Exemplo de Notas por Matéria
        Map<String, Double> notas = new HashMap<>();
        notas.put("Algoritmos", 9.5);

        // Exibindo dados
        System.out.println("--- Status do Aluno ---");
        for (Materia m : listaMaterias) {
            System.out.println(m);
        }

        // Entrada de dados simples
        System.out.print("\nDigite uma nova nota para Algoritmos: ");
        double novaNota = teclado.nextDouble();
        notas.replace("Algoritmos", novaNota);

        System.out.println("Nota atualizada: " + notas.get("Algoritmos"));

        // Fechar o scanner (boa prática)
        teclado.close();
    }
}