public class Main {
    public static void main(String[] args) {
        Integer[] os = { 33, 5, 8, 16, 41, 8 };
        var t = new TableauGenerique<Integer>(os);
        t.triBulle();
        System.out.println(t);
    }
}
