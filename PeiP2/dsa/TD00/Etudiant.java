public class Etudiant {
    String nom;
    String prenom;
    String promo;
    int rang;

    public Etudiant(String nom, String prenom, String promo, int rang) {
        this.nom = nom;
        this.prenom = prenom;
        this.promo = promo;
        this.rang = rang;
    }

    /* toString selon le format : "Courtois Pierre, promo MAM3, rang 12" */
    @Override
    public String toString() {
        return nom + " " + prenom + ", promo " + promo + ", rang " + rang;
    }
}
