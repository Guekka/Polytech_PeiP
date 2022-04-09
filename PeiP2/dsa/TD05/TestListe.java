public class TestListe {

    public static void main(String[] s) {
        // ListeOrdonneeGenerique<String> l = new ListeOrdonneeGenerique<>();
        // l.insere("q");
        // l.insere("z");
        // l.insere("a");
        // l.insere("z");
        // System.out.println(l);
        // l.insere("t");
        // System.out.println(l);

        ListeGenerique<String> l = new ListeGenerique<>();
        l.insereEnTete("q");
        l.insereEnTete("z");
        l.insereEnTete("a");
        l.insereEnTete("z");
        System.out.println(l);
        l.insereEnTete("t");
        System.out.println(l);
        System.out.println(l.size());
        System.out.println(l.existe("q"));
        System.out.println(l.existe("w"));
        System.out.println(l.existe("a"));
        System.out.println(l.rang("q"));
        l.remove("x");
        System.out.println(l);
        l.remove("a");
        System.out.println(l);
        System.out.println(l.size());
        l.remove("t");
        System.out.println(l);
        l.remove("q");
        System.out.println(l);
    }
}
