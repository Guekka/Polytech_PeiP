import PaD.*;

public class Carte {
    private Couleur couleur;
    private Valeur valeur;
    private Image img;

    public Carte(Valeur v, Couleur c) {
        this.valeur = v;
        this.couleur = c;
        var nom = String.format("%s-%s", this.valeur, this.couleur);
        this.img = new Image("Cartes/" + nom + ".gif");
    }

    public String toString() {
        return String.format("[%s(%d),%s]", this.valeur, this.valeur.ordinal(), this.couleur);
    }

    public int compareTo(Carte other) {
        return this.valeur.compareTo(other.valeur);
    }

    /**
     * Role : dessine la carte `a jouer courante this en position (x,y) sur la
     * planche `a dessiner graphique pad
     *
     * @param x   un <code>int</code >
     * @param y   un <code>int</code >.
     * @param pad un <code>PlancheADessin</code>.
     */
    public void dessiner(PlancheADessin pad, double x, double y) {
        this.img.setOrig(x, y);
        pad.ajouter(this.img);
    }

}
