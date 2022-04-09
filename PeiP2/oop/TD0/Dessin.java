import PaD.*;

public class Dessin {
  public static void main(String[] args) {
    PlancheADessin pad = new PlancheADessin();
    // sans le import, on aurait pu ecrire (en plus long!) :

    // PaD.PlancheADessin pad= new PaD.PlancheADessin()
    double milieu = pad.getLargeur() / 2;
    Dessinable titre = new Texte(milieu - 60, 10, "Mon Bonhomme");
    Dessinable tete = new CerclePlein(milieu, 80, 60, PlancheADessin.ROUGE);
    Dessinable cou = new Ligne(milieu, 110, milieu, 170);
    Dessinable corps = new RectanglePlein(milieu - 40, 170, 80, 100, PlancheADessin.VERT);
    Dessinable brasg = new RectanglePlein(milieu - 80, 180, 50, 20, PlancheADessin.BLEU);
    Dessinable brasd = new RectanglePlein(milieu + 20, 180, 50, 20, PlancheADessin.BLEU);
    Dessinable jambeg = new RectanglePlein(milieu - 20, 250, 20, 50, PlancheADessin.BLEU);
    Dessinable jambed = new RectanglePlein(milieu + 40, 250, 20, 50, PlancheADessin.BLEU);

    pad.ajouter(titre);
    pad.ajouter(tete);
    pad.ajouter(cou);
    pad.ajouter(corps);
    pad.ajouter(brasg);
    pad.ajouter(brasd);
    pad.ajouter(jambeg);
    pad.ajouter(jambed);
  }
}
