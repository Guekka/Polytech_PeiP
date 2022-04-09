import java.io.*;
import java.util.Random;
import java.util.ArrayList;

class Fichier {
    private String nomFich;
    private static final int kMaxNum = 100;

    public Fichier(String nomFich) {
        this.nomFich = nomFich;
    }

    public void aleatoire(int n) {
        var rand = new Random();
        try (var os = new DataOutputStream(new FileOutputStream(nomFich))) {
            for (int i = 0; i < n; i++) {
                os.writeInt(rand.nextInt(kMaxNum));
            }
        } catch (IOException e) {
            System.out.println("Erreur: " + e.getMessage());
        }
    }

    private ArrayList<Integer> read() throws IOException {
        var ret = new ArrayList<Integer>();
        try (var is = new DataInputStream(new FileInputStream(nomFich))) {
            while (is.available() > 0) {
                ret.add(is.readInt());
            }
        } catch (EOFException e) {
            /* do nothing */ }
        return ret;
    }

    public String toString() {
        try {
            return read().toString();
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("Erreur: " + e.getMessage());
        }
        return "";
    }

    public int min() throws IOException {
        return read().stream().min(Integer::compare).get();
    }
}
