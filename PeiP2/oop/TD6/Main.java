public class Main {
    public static void main(String[] args) {
        var d = new Disque();
        d.ajouter(new Fichier("1"));
        d.ajouter(new Fichier("2"));
        d.ajouter(new Fichier("3"));

        var r = new Repertoire("R1");
        r.ajouter(new Fichier("4"));
        r.ajouter(new Fichier("5"));
        r.ajouter(new Fichier("6"));

        d.ajouter(r);

        d.lister();
    }
}
