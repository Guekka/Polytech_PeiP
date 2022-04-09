/**
 * Cette classe représente les segments de droite entre 2 points du plan. Ces
 * deux points doivent être différents.
 *
 * @author V. Granet vg@unice.fr
 */

public class Segment {
    private Point orig, fin;

    /**
     * Rôle : initialise le Segment de droite d'orgine O et de fin a Antécédent : a
     * != 0
     */
    public Segment(Point a) {
        this(new Point(0, 0), a);
    }

    /**
     * Rôle : initialise le Segment de droite d'orgine a et de fin b Antécédent : a
     * != b
     */
    public Segment(Point a, Point b) {
        this.orig = a;
        this.fin = b;
        assert_invariants();
    }

    /**
     * Rôle : renvoie le point d'origne du Segment courant
     */
    public Point getOrig() {
        return this.orig;
    }

    /**
     * Rôle : renvoie le point de fin du Segment courant
     */
    public Point getFin() {
        return this.fin;
    }

    /**
     * Rôle : modifie le point d'orgine du Semgent courant
     */
    public void setOrig(Point orig) {
        this.orig = orig;
    }

    /**
     * Rôle : modifie le point de fin du Semgent courant
     */
    public void setFin(Point fin) {
        this.fin = fin;
    }

    /**
     * Rôle : renvoie la représentation du Segment courant sous forme d'une chaîne
     * de caratères
     */
    public String toString() {
        return "[" + this.getOrig() + "-" + this.getFin() + "]";
    }

    public double longueur() {
        var x = Math.pow(this.fin.getX() - this.orig.getX(), 2);
        var y = Math.pow(this.fin.getY() - this.orig.getY(), 2);
        return Math.sqrt(x + y);
    }

    /**
     * rôle : teste si le Point p appartient au Segment courant
     */
    public boolean appartient(Point p) {
        var AB = new Vecteur2(this.getOrig(), this.getFin());
        var AC = new Vecteur2(this.getOrig(), p);

        var k = AC.getX() / AB.getX();
        return AB.colineaire(AC) && k >= 0 && k <= 1;
    }

    /**
     * rôle : renvoie le Point d'intersection entre le Segment courant et le Segment
     * s. Si pas de point d'intersaction, la fonction renvoie null
     */
    public Point intersection(Segment s) {
        var S1 = new Vecteur2(this.getOrig(), this.getFin());
        var S2 = new Vecteur2(s.getOrig(), s.getFin());

        if (S1.colineaire(S2)) {
            return null;
        }

        var A = this.getOrig();
        var B = this.getFin();
        var C = s.getOrig();
        var D = s.getFin();

        var kAB = ((A.getY() - C.getY()) * (D.getX() - C.getX()) - (A.getX() - C.getX()) * (D.getY() - C.getY()))
                / ((B.getX() - A.getX()) * (D.getY() - C.getY()) - (B.getY() - A.getY()) * (D.getX() - C.getX()));

        var kCD = ((C.getX() - A.getX()) * (B.getY() - A.getY()) - (A.getY() - C.getY()) * (B.getX() - A.getX()))
                / ((D.getY() - C.getY()) * (B.getX() - A.getX()) - (D.getX() - C.getX()) * (B.getY() - A.getY()));

        if (kAB + kCD <= 0 || kAB + kCD >= 2)
            return null;

        var AB = new Vecteur2(A, B);
        var AI = AB.produit(kAB);

        return new Point(AI.getX() + A.getX(), AI.getY() + A.getY());
    }

    private void assert_invariants() {
        assert (!this.orig.egal(this.fin));
    }
}
