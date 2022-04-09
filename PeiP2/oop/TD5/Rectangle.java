import PaD.*;

/**
 * Cette classe représente des figures qui sont des rectangles
 *
 * @author V. Granet vg@unice.fr
 */

public class Rectangle extends Figure {
    /* Invariant de classe : largeur et longueur >=0 */

    /**
     * longueur du rectangle
     */
    protected double longueur;
    /**
     * largeur du rectangle
     */
    protected double largeur;

    /**
     * Rôle : crée un rectangle d'origine p avec les dimensions voulues
     *
     * @param L longueur
     * @param l largeur
     * @param p point d'origine
     */
    public Rectangle(double L, double l, Point p) {
        super(p);
        this.longueur = L;
        this.largeur = l;
    }

    /**
     * Rôle : crée un rectangle d'origine (0,0) avec les dimensions voulues
     *
     * @param L longueur
     * @param l largeur
     */
    public Rectangle(double L, double l) {
        this(L, l, new Point(0, 0));
    }

    /**
     * Rôle : @return surface du rectangle
     */
    public double surface() {
        return this.longueur * this.largeur;
    }

    /**
     * @return périmètre du rectangle
     */
    public double perimetre() {
        return (this.longueur + this.largeur) * 2;
    }

    /**
     * Rôle : change la longueur du rectangle
     *
     * @param L nouvelle longueur
     */
    public void setLongueur(double L) {
        this.longueur = L;
    }

    /**
     * Rôle : change la largeur du rectangle
     *
     * @param l nouvelle largeur
     */
    public void setLargeur(double l) {
        this.largeur = l;
    }

    public String toString() {
        var s = "+";
        for (int i = 0; i < this.longueur; i++)
            s += "-";
        s += "+\n";

        for (int h = 0; h < this.largeur; h++) {
            s += "|";
            for (int i = 0; i < this.longueur; i++) {
                s += " ";
            }
            s += "|\n";
        }
        s += "+";
        for (int i = 0; i < this.longueur; i++)
            s += "-";
        s += "+\n";
        return s;
    }

    public void dessiner(PlancheADessin pad) {
        var rec = new RectanglePlein(this.origine.abscisse(), this.origine.ordonnee(), this.longueur * 10,
                this.largeur * 10);
        pad.ajouter(rec);
    }
}
