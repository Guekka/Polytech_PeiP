public class Professeur implements ChargeEnseignement {
    String nom;
    String prenom;
    String labo;
    int nbHeures;
    static final int nbService = 192;

    public Professeur(String nom, String prenom, String labo, int nbHeures) {
        this.nom = nom;
        this.prenom = prenom;
        this.labo = labo;
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

    /* toString. Exemple : "Vizza Tony, labo I3S, service prévu 256h" */
    @Override
    public String toString() {
        return nom + " " + prenom + ", labo " + labo + ", service prévu " + nbHeures + "h";
    }

}
