import PaD.*;

public class Jeu {
    public static void main(String[] args) {
        var dame_pique = new Carte(Valeur.dame, Couleur.pique);
        var six_trefle = new Carte(Valeur.six, Couleur.trefle);

        System.out.println(dame_pique);
        System.out.println(six_trefle);

        System.out.println(dame_pique.compareTo(six_trefle));

        var pad = new PlancheADessin();
        dame_pique.dessiner(pad, 200, 200);
        six_trefle.dessiner(pad, 400, 200);
    }
}
