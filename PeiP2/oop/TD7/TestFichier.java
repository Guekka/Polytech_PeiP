import java.util.Scanner;
import java.io.*;

public class TestFichier {
    public static void main(String[] args) {
        // 4
        var fichier1 = "Test.bin";
        if (args.length == 2)
            fichier1 = args[1];

        // 3
        var f = new Fichier(fichier1);
        f.aleatoire(10);

        // Pour vérifier que le programme fonctionne, on compare la taille du
        // fichier à n. On doit avoir taille = 4n

        // 5
        // On utilise "throws IOException" et non pas "FileNotFoundException"
        // Pour pouvoir renvoyer des exceptions de type différents

        // 6
        System.out.println(f.toString());

        // 7
        try {
            System.out.println(f.min());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        // 9
        final var nomFichierIn = "LesNotes.txt";

        String out = "";
        try (var scanner = new Scanner(new FileInputStream(nomFichierIn))) {
            float glob_average = 0;
            int glob_count = 0;
            while (scanner.hasNextLine()) {
                out += scanner.next(); // Nom
                out += " " + scanner.next(); // Prenom
                out += " : "; // Delimiteur
                float sum = 0;
                int count = 0;
                while (scanner.hasNextDouble()) {
                    sum += scanner.nextDouble();
                    count += 1;
                }

                if (sum == 0) {
                    out += "abs";
                } else {
                    out += sum / count;
                    glob_average += sum / count;
                    glob_count += 1;
                }
                out += "\n";
            }
            out += "Moyenne générale : " + glob_average / glob_count;
        } catch (IOException e) {
            System.out.println("Erreur: " + e.getMessage());
            System.exit(-1);
        }
        final var nomFichierOut = "LesMoyennes.txt";
        try (var os = new PrintWriter(new FileWriter(nomFichierOut))) {
            os.write(out);
        } catch (IOException e) {
            System.out.println("Erreur: " + e.getMessage());
            System.exit(-1);
        }
    }
}
