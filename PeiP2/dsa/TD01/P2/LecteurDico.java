import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * classe pour lire un dictionnaire dans un fichier de texte et le stocker dans
 * un tableau
 */
public class LecteurDico {
    // le chemin vers le fichier
    private String fileName;

    // la liste des mots du dico
    ArrayList<String> lesMots;

    public LecteurDico(String fileName) {
        this.fileName = fileName;
        initDico();
    }

    private int getSize() {
        return lesMots.size();
    }

    // stocke les éléments du fichier dans lesMots
    private void initDico() {
        lesMots = new ArrayList<String>();
        Scanner sc = null;
        try {
            // ouvrir le fichier
            sc = new Scanner(new File(fileName));
        } catch (IOException e) {
            // violent mais, ne sert à rien de poursuivre
            e.printStackTrace();
            System.err.println("erreur d'ouverture fichier dictionnaire, BYE BYE ...");
            System.exit(-1);
        }
        // tant qu'il y a des lignes dans le dictionnaire
        while (sc.hasNextLine()) { // renvoie true ou false selon qy'y a encore à lire
            String ligne = sc.nextLine();
            lesMots.add(ligne);
        }
    }

    // renvoie un String[]
    public String[] getDico() {
        String[] t = new String[lesMots.size()];
        int i = 0;
        for (String s : lesMots) {
            t[i++] = s;
        }
        return t;
    }

    ////////////////////////////////////////////////
    // un exemple d'utilisation
    public static void main(String[] s) {
        LecteurDico ld = new LecteurDico("wordsAlpha.txt");
        // ld.getDico() renvoie un String[] dont le 5ème élément est aaru
        System.out.println(ld.getDico()[25]);
    }
}
