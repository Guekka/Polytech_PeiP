public class Arbre<T> {
    ChainonArbre<T> root = null;

    public Arbre() {
    }

    public Arbre(T elem) {
        root = new ChainonArbre<T>(elem);
    }

    @Override
    public String toString() {
        return root.toString();
    }

}
