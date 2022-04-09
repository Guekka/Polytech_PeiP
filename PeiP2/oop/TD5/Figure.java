import PaD.PlancheADessin;

/**
 * Cette classe représente des figures
 *
 * @author V. Granet vg@unice.fr
 */

public abstract class Figure {
    /**
     * point d'origine de la figure
     */
    protected Point origine;

    /**
     * Rôle : crée une figure dont l'origine est (0, 0)
     */
    public Figure() {
        this(new Point(0, 0));
    }

    /**
     * Rôle : crée une figure dont l'origine est le Point p
     *
     * @param p Point d'origine
     */
    public Figure(Point p) {
        this.origine = p;
    }

    /**
     * Rôle : @return origine de la figure
     */
    public Point getOrigine() {
        return this.origine;
    }

    /**
     * Rôle : @return origine de la figure
     */
    public void setOrigine(Point p) {
        this.origine = p;
    }

    public abstract double perimetre();

    public abstract double surface();

    public abstract void dessiner(PlancheADessin pad);
}
