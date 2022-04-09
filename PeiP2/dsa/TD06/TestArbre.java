public class TestArbre {
    public static void main(String[] args) {
        Arbre<Character> arbre = new Arbre<Character>();
        arbre.root = new ChainonArbre<Character>('H');
        arbre.root.left = new ChainonArbre<Character>('P');
        arbre.root.right = new ChainonArbre<Character>('Z');
        arbre.root.left.left = new ChainonArbre<Character>('D');
        arbre.root.left.left.left = new ChainonArbre<Character>('T');
        arbre.root.left.left.right = new ChainonArbre<Character>('Y');
        arbre.root.left.left.left.right = new ChainonArbre<Character>('U');
        System.out.println(arbre);
    }
}
