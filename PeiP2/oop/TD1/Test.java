/**
 * Classe de Test pour tester les différentes classes du td1 et 2
 *
 * @author V. Granet vg@unice.fr
 */

public class Test {
    public static void main(String[] args) throws Exception {
        // Ex 1
        System.out.println("EX 1");

        // 1.2
        var O = new Point(0, 0);
        var A = new Point(14, -5);
        var B = new Point(2, 7);

        // 1.3
        System.out.println(O + " " + A + " " + B);
        // 1.4
        System.out.println(O.distance(A) + " " + O.distance(B) + " " + B.distance(A));
        // 1.5
        System.out.println(A.egal(B)); // false

        // Ex 2
        System.out.println("EX 2");

        // 2.7
        var AO = new Vecteur2(A, O);
        var OB = new Vecteur2(O, B);
        var AB = new Vecteur2(A, B);

        // 2.8
        System.out.println(AO.somme(OB).egal(AB)); // true

        // 2.9
        var C = new Point(5, 4);
        var AC = new Vecteur2(A, C);

        System.out.println(AC.colineaire(AB)); // true

        // 2.10
        var D = new Point(1, 2);
        var E = new Point(2, 0);
        var F = new Point(3, 2);

        var OD = new Vecteur2(O, D);
        var EF = new Vecteur2(E, F);

        System.out.println(OD.egal(EF)); // true, donc ODFE parallèlogramme

        // Ex 3
        System.out.println("EX 3");

        // 3.12
        var sAB = new Segment(A, B);

        // 3.13
        System.out.println(sAB.appartient(C)); // true
        System.out.println(sAB.appartient(D)); // false

        // 3.14
        var G = new Point(-2, -3);
        var H = new Point(9, 5);
        var sGH = new Segment(G, H);

        var I = sGH.intersection(sAB);
        System.out.println(I);

        // 3.15
        System.out.println(sGH.appartient(I) && sAB.appartient(I)); // true

        // 3.16
        var sEF = new Segment(E, F);
        System.out.println(sAB.intersection(sEF)); // null

        // Ex 4
        // 4.20
        var plan = new Plan2D();
        plan.tracerSegment(sAB);
        plan.tracerSegment(sGH);
        // 4.21
        plan.tracerPoint(I, null);
    }
}
