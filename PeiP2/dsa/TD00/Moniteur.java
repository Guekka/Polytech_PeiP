public class Moniteur implements ChargeEnseignement {
    Etudiant etudiant;
    int nbHeures;
    static final int nbService = 64;

    public Moniteur(Etudiant etudiant, int nbHeures) {
        this.etudiant = etudiant;
        this.nbHeures = nbHeures;
    }

    @Override
    public int getNbHeures() {
        return nbHeures;
    }

    @Override
    public int getService() {
        return nbService;
    }

    /*
     * toString. Exemple : "France Marie, promo SI3, rang 1, moniteur, service
     * prévu 68h"
     */
    @Override
    public String toString() {
        return etudiant.toString() + ", moniteur, service prévu " + nbHeures + "h";
    }
}
