import java.util.Scanner;
import java.util.Arrays;

public class Moyenne {
	public static final int kDoubleRead = 3;

	public static void main(String[] args) {
		try (var sc = new Scanner(System.in)) {
			var read = new double[kDoubleRead];
			for (int i = 0; i < kDoubleRead; i++) {
				read[i] = sc.nextDouble();
			}
			final var average = Arrays.stream(read).average().orElse(0.0);
			System.out.println(average);
		}
	}
}
