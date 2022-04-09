public class EtudiantComparable implements Comparable<EtudiantComparable> {
    private Etudiant etudiant;

    public EtudiantComparable(Etudiant e) {
        etudiant = e;
    }

    public int compareTo(EtudiantComparable e) {
        return Integer.compare(this.etudiant.getRange(), e.etudiant.getRange());
    }

    public String toString() {
        return etudiant.toString();
    }
}
