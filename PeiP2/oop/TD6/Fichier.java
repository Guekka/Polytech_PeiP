public class Fichier extends Item {
    public Fichier(String nom) {
        super(nom);
    }

    @Override
    public void lister() {
        System.out.println("Fichier:" + this.getNom());
    }
}
