import java.util.Scanner;
import java.util.Calendar;

public class AnneeNaissance {
	public static void main(String[] args) {
		// creer un objet Scanner pour lire depuis l’entree standard
		Scanner sc = new Scanner(System.in);
		// lire le prenom
		System.out.print("Votre prenom : ");
		String prenom = sc.nextLine();
		// lire l’age
		System.out.print("Votre age : ");
		int age = sc.nextInt();
		// afficher l’annee de naissance
		Calendar c = Calendar.getInstance();
		int anneeCourante = c.get(Calendar.YEAR);
		System.out.println(prenom + ", vous etes ne en " + (anneeCourante - age));
	}
}
