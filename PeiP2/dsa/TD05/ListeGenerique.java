/**
 *
 * @param <E>
 */
public class ListeGenerique<E extends Comparable<E>> {
    private ElementListe<E> premier;

    // liste contenant aucun élément
    public ListeGenerique() {
        this.premier = null;
    }

    // liste avec 1 élément
    public ListeGenerique(E element) {
        this.premier = new ElementListe<E>(element);
    }

    // insère elt au début de la liste
    void insereEnTete(E elt) {
        if (premier == null)
            premier = new ElementListe<E>(elt);
        else {
            premier = new ElementListe<E>(elt, premier);
        }
    }

    // nombre d'éléments dans la liste
    int size() {
        if (premier == null)
            return 0;
        return premier.size();
    }

    // renvoie vrai si elt est dans this
    boolean existe(E elt) {
        if (premier == null)
            return false;
        return premier.existe(elt);
    }

    // renvoie le rang de l'élément (i.e. sa position à gauche dans la liste)
    // -1 si elt n'est pas dans la liste
    int rang(E elt) {
        if (premier == null)
            return -1;
        return premier.rang(elt);
    }

    // enlève l'élément elt de la liste
    // ne fait rien s'il n'y est pas
    void remove(E elt) {
        if (premier != null) {
            if (premier.element.equals(elt))
                premier = premier.suivant;
            else
                premier.remove(elt);
        }
    }

    public String toString() {
        if (premier == null)
            return "[]";
        return "[" + premier + "]";
    }
}
