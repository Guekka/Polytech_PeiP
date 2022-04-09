import java.util.Random;

import PaD.PlancheADessin;
import PaD.Texte;

public class Joueur {
    private String nom;
    private Carte[] mesCartes;
    private int score;
    public Texte displayName = null;

    public Joueur(String nom) {
        this.nom = nom;
    }

    public void prendreMesCartes(Jeu52 jeu, int de, int a) {
        this.mesCartes = new Carte[a - de];
        for (int i = de; i < a; i++) {
            this.mesCartes[i - de] = jeu.getCarte(i);
        }
    }

    public void cacherCartes() {
        for (var c : this.mesCartes)
            if (!c.estRetournee())
                c.retournerCarte();
    }

    public void montrerCartes(PlancheADessin pad, double h) {
        int x = 10; // A 0, l'image dépasse à gauche

        // Affiche le nom et le score
        if (this.displayName != null)
            pad.supprimer(this.displayName);
        this.displayName = new Texte(this.nom + " : " + this.score);
        this.displayName.setOrig(x, h);
        pad.ajouter(this.displayName);
        h += 25; // Valeur arbitraire

        for (var carte : this.mesCartes) {
            carte.dessiner(pad, x, h);
            x += Carte.kCarteLargeur;
        }
    }

    public Carte choisirCarteCacheeAuHasard() {
        var rand = new Random();
        final int limit = 100; // Avoid deadlock
        for (int i = 0; i < limit; i++) {
            int idx = rand.nextInt(this.mesCartes.length);
            if (this.mesCartes[idx].estRetournee())
                return this.mesCartes[idx];
        }
        return null;
    }

    public int getScore() {
        return this.score;
    }

    public void retournerCarteCacheeAuHasard() {
        var c = choisirCarteCacheeAuHasard();
        c.retournerCarte();
        this.score += c.getValeur().valeur();
    }

    public boolean peutJouer() {
        return this.score < 15;
    }

    public String toString() {
        return this.nom;
    }
}
