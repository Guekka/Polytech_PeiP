import java.util.ArrayList;

public class GestionServices {
    String etablissement;
    ArrayList<ChargeEnseignement> personnel = new ArrayList<ChargeEnseignement>();

    public GestionServices(String etablissement) {
        this.etablissement = etablissement;
    }

    public void add(ChargeEnseignement p) {
        personnel.add(p);
    }

    /*
     * toString. Exemple
     * "Services à Polytech
     * Total d'heures à payer 380h
     * Vizza Tony, labo I3S, service prévu 256h, dépasse son service de 64h
     * Courtois Pierre, promo MAM3, rang 12, moniteur, service prévu 56h, en sous
     * service de 8h
     * France Marie, promo SI3, rang 1, moniteur, service prévu 68h, dépasse son
     * service de 4h"
     */
    @Override
    public String toString() {
        String s = "Services à " + etablissement + "\n";
        int total = 0;
        for (ChargeEnseignement p : personnel) {
            total += p.getNbHeures();
        }
        s += "Total d'heures à payer " + total + "h\n";
        for (ChargeEnseignement p : personnel) {
            if (p.getNbHeures() > p.getService()) {
                s += p + ", dépasse son service de " + (p.getNbHeures() - p.getService()) + "h\n";
            } else {
                s += p + ", en sous service de " + (p.getService() - p.getNbHeures()) + "h\n";
            }
        }
        return s;
    }
}
