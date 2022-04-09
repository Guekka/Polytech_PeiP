import PaD.*;

public class Carte implements Comparable<Carte> {
    private Couleur couleur;
    private Valeur valeur;
    private Image img;
    private Image dos = new Image("Cartes/dos.gif");
    private Image current;

    public static final double kCarteLargeur;
    public static final double kCarteHauteur;

    static {
        var default_img = new Image("Cartes/dos.gif");
        kCarteLargeur = default_img.getLargeur();
        kCarteHauteur = default_img.getHauteur();
    }

    public Carte(Valeur v, Couleur c) {
        this.valeur = v;
        this.couleur = c;
        var nom = String.format("%s-%s", this.valeur, this.couleur);
        this.img = new Image("Cartes/" + nom + ".gif");
        this.current = this.img;
    }

    public String toString() {
        return String.format("[%s(%d),%s]", this.valeur, this.valeur.ordinal(), this.couleur);
    }

    public int compareTo(Carte other) {
        if (this.couleur.equals(other.couleur))
            return this.valeur.compareTo(other.valeur);
        return this.couleur.compareTo(other.couleur);
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
        pad.supprimer(this.current);
        this.img.setOrig(x, y);
        this.dos.setOrig(x, y);
        pad.ajouter(this.current);
    }

    public void dessiner(PlancheADessin pad) {
        dessiner(pad, this.img.getX(), this.img.getY());
    }

    public void retournerCarte() {
        if (this.current == this.img)
            this.current = this.dos;
        else
            this.current = this.img;
    }

    public boolean estRetournee() {
        return this.current == this.dos;
    }

    public Valeur getValeur() {
        return this.valeur;
    }
}
