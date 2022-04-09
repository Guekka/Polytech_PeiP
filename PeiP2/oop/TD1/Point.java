/**
 * Cette classe représente les points du plan cartésien.
 *
 * @author V. Granet vg@unice.fr
 */
public class Point {
    private double abs, ord;

    /*
     * Rôle : initialise le point (0,0)
     */
    public Point() {
        this(0.0, 0.0);
    }

    /*
     * Rôle : initialise le point (x,y)
     */
    public Point(double x, double y) {
        this.setX(x);
        this.setY(y);
    }

    /**
     * Rôle : renvoie l'abscisse du Point courant
     */
    public double getX() {
        return this.abs;
    }

    /**
     * Rôle : renvoie l'ordonnée du Point courant
     */
    public double getY() {
        return this.ord;
    }

    /**
     * Rôle : change l'abscisse du Point courant
     */
    public void setX(double x) {
        this.abs = x;
    }

    /**
     * Rôle : change l'ordonnée du Point courant
     */
    public void setY(double y) {
        this.ord = y;
    }

    /**
     * Rôle : teste si le Point courant est egal à au Point p
     */
    public boolean egal(Point p) {
        return this.getY() == p.getY() && this.getX() == p.getX();
    }

    /**
     * Rôle : envoie la distance entre le Point courant et le Point p Rappel :
     * distance(a,b) = rac2((b_x-a-x)^2+(b_y-a-y)^2)
     */
    public double distance(Point p) {
        var x = Math.pow(p.getX() - this.getX(), 2);
        var y = Math.pow(p.getY() - this.getY(), 2);
        return Math.sqrt(x + y);
    }

    /**
     * Rôle : renvoie la représentation du Point courant sous forme d'une chaîne de
     * caratères
     */
    public String toString() {
        return String.format("[%f ; %f]", this.getX(), this.getY());
    }

}
