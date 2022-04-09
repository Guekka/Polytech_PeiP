public class Carre extends Rectangle {
    public Carre(int l) {
        super(l, l);
    }

    public void setLongueur(int l) {
        super.setLongueur(l);
        super.setLargeur(l);
    }

    public void setLargeur(int l) {
        this.setLongueur(l);
    }
}
