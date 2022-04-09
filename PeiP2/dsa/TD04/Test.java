import java.util.Arrays;

public class Test {
    public static void main(String[] s) {
        Integer[] t = { 3, 67, 45, 1, 89, 5 };
        QuickSort<Integer> qs = new QuickSort<Integer>(t);
        qs.trier();
        System.out.println(qs);
        System.out.println(Arrays.toString(t));
        QuickSort<Integer> qs2 = new QuickSort<Integer>(t, false);
        qs2.trier();
        System.out.println(qs2);
        System.out.println(Arrays.toString(t));

        Integer[] t2 = { 3, 67, 450, 1000, 89635, 14521453 };
        QuickSort<Integer> qs3 = new QuickSort<Integer>(t);
        qs3.trier();
        System.out.println(qs3);
        System.out.println(Arrays.toString(t2));
    }
}
