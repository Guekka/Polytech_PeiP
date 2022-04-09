import java.util.Optional;

/**
 * exemple d'utilisation d'une pile pour le parenthésage
 */
public class Parenthesage {

    String phrase;

    public Parenthesage(String phrase) {
        this.phrase = phrase;
    }

    // renvoie le caractère qui ferme un ouvrant
    private static char ferme(char d) {
        switch (d) {
            case '(':
                return ')';
            case '[':
                return ']';
            default:
                return '}';
        }
    }

    // vrai si s est un délimiteur ouvrant
    private static boolean estOuvrant(char s) {
        return s == '(' | s == '{' | s == '[';
    }

    // vrai si s est un délimiteur fermant
    private static boolean estFermant(char s) {
        return s == ')' | s == '}' | s == ']';
    }

    // vérifie les parenthèses
    public boolean verificationParen() {
        return verifieLeDelimiteur('(');
    }

    // vérifie les []
    public boolean verificationCrochet() {
        return verifieLeDelimiteur('[');
    }

    // vérifie les {}
    public boolean verificationAcco() {
        return verifieLeDelimiteur('{');
    }

    // vérifie uniquement le delimiteur "delimiteur"
    private boolean verifieLeDelimiteur(char delimiteur) {
        int counter = 0;
        for (char c : phrase.toCharArray()) {
            if (c == delimiteur)
                counter += 1;
            if (c == ferme(delimiteur))
                counter -= 1;
            if (c < 0)
                return false;
        }
        return counter == 0;
    }

    // verifie les 3 délimiteurs mais ne tient pas compte
    // des intercroisements ([)] est considéré comme OK alors que c'est KO
    public boolean verificationKO() {
        return verifieLeDelimiteur('(') && verifieLeDelimiteur('[') && verifieLeDelimiteur('{');
    }

    // verification OK : version avec la pile java
    public boolean verification() {
        return verificationMaison();
    }

    // verification OK : version avec la pile maison
    public boolean verificationMaison() {
        var pile = new Pile<Character>();
        for (char c : phrase.toCharArray()) {
            if (estOuvrant(c))
                pile.push(c);
            else if (estFermant(c)) {
                var top = pile.pop().map(s -> ferme(s));
                if (!top.equals(Optional.of(c)))
                    return false;
            }
        }
        return true;
    }
}
