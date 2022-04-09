import PaD.*;
import java.awt.Color;

/**
 * Cette classe représente le plan cartésien et permet de visualiser à l'aide de
 * la planche à dessin (PaD) des segments de droite et des points du plan
 *
 * @author V. Granet vg@unice.fr
 */

public class Plan2D {
    private final double unité = 20;
    private PlancheADessin pad;
    private final double milieuL;
    private final double milieuH;
    private final int max_coord = 25;

    /**
     * Rôle crée un Plan2D avec les axes gradués des abscisses et des ordonnées
     *
     */
    public Plan2D() {
        this.pad = new PlancheADessin(true);
        this.milieuL = pad.getLargeur() / 2;
        this.milieuH = pad.getHauteur() / 2;
        this.tracerAxes();
        this.tracerGraduations();
    }

    /*
     * Rôle : convertit une coordonnée x du PaD en abscisse du Plan2D courant
     */
    private double coordX(double x) {
        return (unité * x) + milieuL;
    }

    /*
     * Rôle : convertit une coordonnée y du PaD en ordonnée du Plan2D courant
     */
    private double coordY(double y) {
        return -(unité * y) + milieuH;
    }

    /*
     * Rôle : trace les axes des abscisses et des ordonnées du Plan2D courant
     */
    private void tracerAxes() {
        var x = new Ligne(coordX(-max_coord), coordY(0), coordX(max_coord), coordY(0));
        var y = new Ligne(coordX(0), coordY(-max_coord), coordX(0), coordY(max_coord));
        this.pad.ajouter(x, y);
    }

    /*
     * Rôle : gradue les axes des abscisses et des ordonnées du Plan2D courant
     */
    private void tracerGraduations() {
        for (int i = -max_coord; i < max_coord; i++) {
            var x = new Ligne(coordX(-0.25), coordY(i), coordX(0.25), coordY(i));
            var y = new Ligne(coordX(i), coordY(-0.25), coordX(i), coordY(0.25));
            this.pad.ajouter(x, y);
        }
    }

    /**
     * Rôle : trace le Point p dans la couleur c sur le Plan2D courant
     */
    public void tracerPoint(Point p, Color c) {
        var point = new CerclePlein(coordX(p.getX()), coordY(p.getY()), 10, c);
        this.pad.ajouter(point);
    }

    /**
     * Rôle : trace le Point s sur le Plan2D courant
     */
    public void tracerSegment(Segment s) {
        var A = s.getOrig();
        var B = s.getFin();
        var ligne = new Ligne(coordX(A.getX()), coordY(A.getY()), coordX(B.getX()), coordY(B.getY()),
                PlancheADessin.ROUGE);
        this.pad.ajouter(ligne);

    }

}
