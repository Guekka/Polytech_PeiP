
import java.util.ArrayList;

public class Recursivite {

    // exceptionnellement, tout est en static (pas beau ...)

    public static int factorielle(int n) {
        if (n == 0)
            return 1;
        return n * factorielle(n - 1);
    }

    public static int sommeCarreRec(int n) {
        if (n == 0)
            return 0;
        return n * n + sommeCarreRec(n - 1);
    }

    public static int compte(String s, char c) {
        if (s.length() == 0)
            return 0;
        if (s.charAt(0) == c)
            return 1 + compte(s.substring(1), c);
        return compte(s.substring(1), c);
    }

    public static ArrayList<String> permute(String s) {
        var res = new ArrayList<String>();
        if (s.length() <= 1) {
            res.add(s);
            return res;
        }

        for (var sub : permute(s.substring(1))) {
            for (int i = 0; i < sub.length(); ++i) {
                res.add(sub.substring(0, i) + s.charAt(0) + sub.substring(i));
            }
            res.add(sub + s.charAt(0));
        }

        return res;
    }

    public static void main(String[] s) {
        System.out.println(factorielle(8));
        System.out.println(compte("abracadabra", 'a'));
        System.out.println(compte("abracadabra", 'i'));
        String s1 = "mou";
        ArrayList<String> ps1 = permute(s1);
        System.out.println(ps1 + " " + factorielle(s1.length()) + " " + ps1.size());
        String s2 = "plage";
        ArrayList<String> ps2 = permute(s2);
        System.out.println(ps2 + " " + factorielle(s2.length()) + " " + ps2.size());
    }
}
