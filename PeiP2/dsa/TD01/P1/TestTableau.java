public class TestTableau {

    public static void main(String[] s) {
        Integer[] os = { 33, 5, 8, 16, 41, 8 };
        var t = new TableauGenerique<Integer>(os);
        System.out.println(t);
        System.out.println(t.recherche(8));
        System.out.println(t.rechercheVite(8));

        // Q2
        System.out.println(t.recherche(8, 2));
        System.out.println(t.recherche(8, 5));

        String[] oss = { "il", "fait", "beau", "aujourd'hui" };
        var ts = new TableauGenerique<String>(oss);
        System.out.println(ts);
        System.out.println(ts.recherche("beau"));

        EtudiantComparable e1 = new EtudiantComparable(new Etudiant("Pierre", 1234));
        EtudiantComparable e2 = new EtudiantComparable(new Etudiant("Antoine", 12));
        EtudiantComparable e3 = new EtudiantComparable(new Etudiant("Line", 1));
        EtudiantComparable e4 = new EtudiantComparable(new Etudiant("Sophie", 1));
        EtudiantComparable[] es = { e2, e3, e1 };
        var te = new TableauGenerique<EtudiantComparable>(es);
        System.out.println(te);
        System.out.println(te.recherche(e3));
        System.out.println(te.recherche(e4));
        // System.out.println(te.rechercheViteRecursif(e4));

    }
}
