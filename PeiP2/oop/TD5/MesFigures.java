import PaD.*;
import java.util.Random;

public class MesFigures {
    public static void main(String[] args) {
        // 6
        // var rec = new Rectangle(50, 70);
        // L'erreur obtenue est liée au fait que le point d'origine n'est pas
        // initialisé

        // 12
        var car = new Carre(4);
        System.out.println(car);
        car.setLongueur(6);
        // Seule la longueur est modifiée, le Carre devient un rectangle
        System.out.println(car);

        // 15
        Rectangle r1 = new Carre(8);
        // Rectangle r2 = new Cercle(8); // Ne compile pas

        // On voit bien que la première compile car un Carre est un Rectangle
        // Mais pas la deuxième, car un Cercle n'est pas un Rectangle

        // 16
        // Carre r2 = new Rectangle(2, 8);
        // Cela ne marche pas, car Carre est une classe fille de Rectangle, pas
        // l'inverse

        // 17
        // Carre r2 = r1;
        // Cela ne marche pas, car même si r1 est un Carre, le compilateur ne
        // le sait pas. On lui a désigné comme Rectangle, pas comme Carre. Il
        // faudrait le cast pour pouvoir compiler cette assignation.

        // 18
        var tf = new Figure[4];
        tf[0] = new Ellipse(3, 5); // 21 on ne peut plus instantier une classe abstraite
        tf[1] = new Rectangle(8, 3);
        tf[2] = new Carre(4);
        tf[3] = new Cercle(4);

        var cast_rect = (Rectangle) tf[1];
        System.out.println(cast_rect.surface() + " " + cast_rect.perimetre());
        var cast_carre = (Carre) tf[2];
        System.out.println(cast_carre.surface() + " " + cast_carre.perimetre());
        var cast_cercle = (Cercle) tf[3];
        System.out.println(cast_cercle.surface() + " " + cast_cercle.perimetre());

        // 22
        var rand = new Random();
        for (int i = 0; i < tf.length; i++) {
            var type = rand.nextInt(4);
            switch (type) {
                case 0:
                    tf[i] = new Ellipse(rand.nextInt(10) + 10, rand.nextInt(10) + 10);
                    break;
                case 1:
                    tf[i] = new Cercle(rand.nextInt(10) + 10);
                    break;
                case 2:
                    tf[i] = new Rectangle(rand.nextInt(10) + 10, rand.nextInt(10) + 10);
                    break;
                case 3:
                    tf[i] = new Carre(rand.nextInt(10) + 10);
                    break;
            }
        }

        PlancheADessin pad = new PlancheADessin(1000, 1000);
        for (var fig : tf) {
            // 23
            System.out.println("surface: " + fig.surface() + " perimetre: " + fig.perimetre());
            // 25
            var x = rand.nextInt(700) + 100;
            var y = rand.nextInt(700) + 100;
            fig.setOrigine(new Point(x, y));
            fig.dessiner(pad);
        }
    }
}
