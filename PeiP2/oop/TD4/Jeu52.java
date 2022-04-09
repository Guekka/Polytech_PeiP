import java.util.Random;
import PaD.*;

public class Jeu52 {
    private Carte[] jeu;
    public static final int kNombreCarte = 52;

    public Jeu52() {
        this.jeu = new Carte[kNombreCarte];
        int idx = 0;
        for (var c : Couleur.values()) {
            for (var v : Valeur.values()) {
                this.jeu[idx] = new Carte(v, c);
                idx++;
            }
        }
    }

    public Carte getCarte(int indice) {
        if (indice > this.jeu.length)
            return null;
        return this.jeu[indice];
    }

    private void echange(int l, int r) {
        var tmp = this.jeu[l];
        this.jeu[l] = this.jeu[r];
        this.jeu[r] = tmp;
    }

    public void melanger() {
        Random random = new Random();
        for (int i = 0; i < kNombreCarte; i++) {
            var idx1 = random.nextInt(kNombreCarte);
            var idx2 = random.nextInt(kNombreCarte);

            echange(idx1, idx2);
        }
    }

    public void ordonner() {
        for (int i = 0; i < this.jeu.length; i++) {
            // Element le plus petit
            int min_idx = i;
            for (int j = i + 1; j < this.jeu.length; j++)
                if (this.jeu[j].compareTo(jeu[min_idx]) == -1)
                    min_idx = j;

            echange(i, min_idx);
        }
    }

    public void dessiner(PlancheADessin pad) {
        for (int l = 0; l < 4; l++) {
            for (int c = 0; c < 13; c++) {
                double x = (c + 1) * Carte.kCarteLargeur;
                double y = (l + 1) * Carte.kCarteHauteur;
                System.out.println(l * 13 + c);
                this.jeu[l * 13 + c].dessiner(pad, x, y);
            }
        }
    }

    public String toString() {
        var builder = new StringBuilder();
        for (var carte : this.jeu) {
            builder.append(carte.toString() + '\n');
        }
        return builder.toString();
    }
}
