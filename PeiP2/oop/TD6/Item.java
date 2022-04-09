public abstract class Item {
    private String nom;

    public Item(String nom) {
        this.nom = nom;
    }

    public String getNom() {
        return this.nom;
    }

    public abstract void lister();
}
