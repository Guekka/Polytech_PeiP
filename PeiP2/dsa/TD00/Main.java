class Main {
    public static void main(String[] args) {
        // test 1
        Etudiant e1 = new Etudiant("Courtois", "Pierre", "MAM3", 12);
        System.out.println(e1);
        // test 2
        Etudiant e2 = new Etudiant("France", "Marie", "SI3", 1);
        ChargeEnseignement m2 = new Moniteur(e2, 68);
        System.out.println(m2);
        // test 3
        ChargeEnseignement p = new Professeur("Vizza", "Tony", "I3S", 256);
        System.out.println(p);
        // test 4
        ChargeEnseignement m1 = new Moniteur(e1, 56);
        GestionServices g = new GestionServices("Polytech");
        g.add(p);
        g.add(m1);
        g.add(m2);
        System.out.println(g);
    }
}
