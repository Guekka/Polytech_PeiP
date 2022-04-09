import java.util.ArrayList;

public class Disque {
    private ArrayList<Item> items;

    public Disque() {
        this.items = new ArrayList<Item>();
    }

    public void ajouter(Item i) {
        items.add(i);
    }

    public void lister() {
        this.items.forEach(Item::lister);
    }
}
