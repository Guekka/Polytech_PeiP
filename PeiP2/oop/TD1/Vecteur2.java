/**
 * Cette classe représente les vecteurs dans un espace à 2 dimensions
 *
 * @author V. Granet vg@unice.fr
 */
public class Vecteur2 {
    private double x, y;

    /*
     * Rôle : initialise un Vecteur2 à partir des coordonnées a et b
     */
    private Vecteur2(double a, double b) {
        this.x = a;
        this.y = b;
    }

    /**
     * Rôle : initialise le vecteur OA
     */
    public Vecteur2(Point A) {
        this.x = A.getX();
        this.y = A.getY();
    }

    /**
     * Rôle : initialise le vecteur AB
     */
    public Vecteur2(Point A, Point B) {
        this.x = B.getX() - A.getX();
        this.y = B.getY() - A.getY();
    }

    /**
     * Rôle : renvoie le Point P(this.x, this.y) correspondant au Vecteur OP
     */
    public Point getPoint() {
        return new Point(this.x, this.y);
    }

    /**
     * Rôle : renvoie la coordonnée x du Vecteur2 courant
     */
    public double getX() {
        return this.x;
    }

    /**
     * Rôle : renvoie la coordonnée y du Vecteur2 courant
     */
    public double getY() {
        return this.y;
    }

    /**
     * Rôle : renvoie le Vecteur2 somme du Vecteur2 courant et du Vecteur2 v.
     */
    public Vecteur2 somme(Vecteur2 v) {
        return new Vecteur2(this.getX() + v.getX(), this.getY() + v.getY());
    }

    /**
     * Rôle : renvoie le Vecteur2 produit du Vecteur2 courant et k
     */
    public Vecteur2 produit(double k) {
        return new Vecteur2(this.getX() * k, this.getY() * k);
    }

    /**
     * Rôle : teste si le Vecteur2 courant et le Vecteur2 v sont égaux
     */
    public boolean egal(Vecteur2 v) {
        return this.getX() == v.getX() && this.getY() == v.getY();
    }

    /**
     * Rôle : teste si le Vecteur2 courant et le Vecteur2 v sont colineaires
     */
    public boolean colineaire(Vecteur2 v) {
        // Float precision issue
        return Math.abs(this.getX() * v.getY() - this.getY() * v.getX()) <= 1E-10;
    }

    /**
     * Rôle : renvoie la représentation du Vecteur2 courant sous forme d'une chaîne
     * de caratères
     */
    public String toString() {
        return String.format("[%f ; %f]", this.getX(), this.getY());
    }
}
