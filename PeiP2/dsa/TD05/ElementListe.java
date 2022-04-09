/***
 * classe pour les éléments des listes qui sont reliés entre eux
 *
 * @param <E>
 */
public class ElementListe<E extends Comparable<E>> {
    // l'élément
    E element;
    // le lien vers le suivant
    ElementListe<E> suivant;

    public ElementListe(E element) {
        this(element, null);
    }

    public ElementListe(E element, ElementListe<E> suivant) {
        this.element = element;
        this.suivant = suivant;
    }

    // renvoie le nombre d'éléments qui sont chainés à this
    int size() {
        if (suivant == null)
            return 1;
        return 1 + suivant.size();
    }

    // renvoie vrai si elt est l'élément courant ou un élément parmi les suivants
    boolean existe(E elt) {
        if (element.equals(elt))
            return true;
        if (suivant == null)
            return false;
        return suivant.existe(elt);
    }

    // renvoie le rang de l'élément (i.e. sa position dans la liste)
    // -1 si elt n'est pas dans la liste
    int rang(E elt) {
        if (element.equals(elt))
            return 0;
        if (suivant == null)
            return -1;
        return 1 + suivant.rang(elt);
    }

    // enlève elt de la liste, ne fait rien si elt n'est pas dans la liste
    // NOTA: il faut garder l'élément précédent
    void remove(E elt) {
        if (suivant == null)
            return;
        if (suivant.element.equals(elt)) {
            suivant = suivant.suivant;
            return;
        }

        suivant.remove(elt);
    }

    public String toString() {
        String res = "";
        ElementListe<E> el = this;
        while (el != null) {
            res += el.element + " ";
            el = el.suivant;
        }
        return res;
    }
}
