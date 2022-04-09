public class ChainonArbre<T> {
    public ChainonArbre(T elem) {
        val = elem;
    }

    public ChainonArbre<T> left;
    public ChainonArbre<T> right;

    T val;

    @Override
    public String toString() {
        return val.toString() + "(" + left.toString() + ")(" + right.toString() + ")";
    }
}
