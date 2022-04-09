public class TestParenthese {
    public static void main(String[] s) {
        Parenthesage p = new Parenthesage("(}56 [9] ) {[34)]");
        System.out.println(p.verificationParen());
        System.out.println(p.verificationCrochet());
        System.out.println(p.verificationAcco());

        Parenthesage pok = new Parenthesage("(([23]{[]({})}))");
        System.out.println(pok.verificationKO());
        Parenthesage pko = new Parenthesage("(([23]{[])))({})}");
        System.out.println(pko.verificationKO());

        Parenthesage ppb = new Parenthesage("(([23]{[]({)}}))");
        System.out.println(ppb.verificationKO());

        System.out.println("avec la pile java");
        System.out.println(p.verification());
        System.out.println(pok.verification());
        System.out.println(pko.verification());
        System.out.println(ppb.verification());

        System.out.println("avec la pile maison");
        System.out.println(p.verificationMaison());
        System.out.println(pok.verificationMaison());
        System.out.println(pko.verificationMaison());
        System.out.println(ppb.verificationMaison());
    }
}
