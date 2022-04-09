public class Etudiant {
    private String name;
    private int range;

    public Etudiant(String n, int r) {
        name=n;
        range=r;
    }

    public int getRange() {
        return range;
    }

    public String getName() {
        return name;
    }


    @Override
    public String toString() {
        return "Etudiant{" +
                "name='" + name + '\'' +
                ", range=" + range +
                '}';
    }


}
