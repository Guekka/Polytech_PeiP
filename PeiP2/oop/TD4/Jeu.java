import PaD.*;
import javax.swing.JOptionPane;

public class Jeu {

    private static int retourner(String joueur) {
        int ret = JOptionPane.showConfirmDialog(null, "Retourner 1 carte au hasard ?", joueur,
                JOptionPane.OK_CANCEL_OPTION);
        return ret;
    }

    private static void montrer_jeu(Joueur[] joueurs, int i, PlancheADessin pad) {
        // La valeur y est arbitraire, déterminée par différents essais
        joueurs[i].montrerCartes(pad, 100 + i * Carte.kCarteHauteur * 1.2);

    }

    public static void main(String[] args) {
        // Initialisaiton des cartes
        var lesCartes = new Jeu52();
        lesCartes.melanger();

        var pad = new PlancheADessin(1000, 800);

        // Initialisation des joueurs
        var joueurs = new Joueur[4];
        int carte_par_joueur = Jeu52.kNombreCarte / joueurs.length;
        for (int i = 0; i < joueurs.length; i++) {
            var joueur = joueurs[i] = new Joueur("Joueur " + i);
            joueur.prendreMesCartes(lesCartes, i * carte_par_joueur, (i + 1) * carte_par_joueur);
            joueur.cacherCartes();
        }

        for (int i = 0; i < joueurs.length; i++) {
            montrer_jeu(joueurs, i, pad);
        }

        // Boucle principale
        int cannot_play = 0;
        while (cannot_play != joueurs.length) {
            cannot_play = 0;
            for (int i = 0; i < joueurs.length; i++) {
                var joueur = joueurs[i];
                if (!joueur.peutJouer()) {
                    cannot_play += 1;
                    continue;
                }
                if (retourner(joueur.toString()) != JOptionPane.OK_OPTION)
                    continue;

                joueur.retournerCarteCacheeAuHasard();
                montrer_jeu(joueurs, i, pad);
            }
        }

        // Trouver le vainqueur
        Joueur vainqueur = new Joueur("Croupier");
        for (var j : joueurs) {
            var score = j.getScore();
            if (score <= 21 && score > vainqueur.getScore()) {
                vainqueur = j;
            }
        }
        if (vainqueur != null)
            JOptionPane.showMessageDialog(null, "Le joueur victorieux est :" + vainqueur.toString(), "Victoire!",
                    JOptionPane.PLAIN_MESSAGE);
    }
}
