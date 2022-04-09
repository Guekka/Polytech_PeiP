import java.util.ArrayList;

public class Repertoire extends Item {
    private ArrayList<Item> items;

    public Repertoire(String nom) {
        super(nom);
        this.items = new ArrayList<Item>();
    }

    public void ajouter(Item i) {
        this.items.add(i);
    }

    @Override
    public void lister() {
        System.out.println("Repertoire: " + this.getNom());
        System.out.println("DEBUT");
        this.items.forEach(Item::lister);
        System.out.println("FIN");
    }

}
