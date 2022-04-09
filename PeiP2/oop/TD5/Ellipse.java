import PaD.PlancheADessin;
import PaD.EllipsePleine;

public class Ellipse extends Figure {
    protected double grandAxe;
    protected double petitAxe;

    public Ellipse(double petitRayon, double grandRayon, Point p) {
        super(p);
        this.grandAxe = grandRayon;
        this.petitAxe = petitRayon;
    }

    public Ellipse(double petitRayon, double grandRayon) {
        this(petitRayon, grandRayon, new Point(0, 0));
    }

    public double surface() {
        return Math.PI * this.petitAxe * this.grandAxe;
    }

    public double perimetre() {
        return Math.PI * Math.sqrt(2 * (Math.pow(this.petitAxe, 2) + Math.pow(this.grandAxe, 2)));
    }

    public void dessiner(PlancheADessin pad) {
        var el = new EllipsePleine(this.getOrigine().abscisse(), this.getOrigine().ordonnee(), this.grandAxe * 10,
                this.petitAxe * 10);
        pad.ajouter(el);
    }
}
