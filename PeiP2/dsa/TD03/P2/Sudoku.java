import java.util.Arrays;

/** une classe pour résoudre les sudokus de façon naive */
public class Sudoku {
  // les valeurs par défaut d'une grille de Sudoku
  private static int TAILLE_DEFAUT = 9;
  private static int TAILLE_CARRE_DEFAUT = 3;

  private int taille; // la taille de la grille
  private int tailleCarre; // la taille d'un carre dans la grille
  private int[][] grille; // la grille de sudoku

  /**
   * constructeur par défaut qui construit une grille de Sudoku
   * standard
   */
  public Sudoku() {
    taille = TAILLE_DEFAUT;
    tailleCarre = TAILLE_CARRE_DEFAUT;
    grille = new int[taille][taille];
  }

  /**
   * construire une grille de taille par défaut
   * avec des valeurs initiales
   * PRECOND : t est de taille 9
   */
  public Sudoku(int[][] t) {
    this(); // appel au constructeur par défaut
    for (int i = 0; i < t.length; i++)
      for (int j = 0; j < t.length; j++)
        grille[i][j] = t[i][j];
  }

  /** place la valeur initiale v en (i,j) */
  public void init(int i, int j, int v) {
    grille[i][j] = v;
  }

  /**
   * CONSEQUENT : renvoie vrai si la valeur v est possible pour la ligne l
   *
   * @param l: le n° de ligne
   * @param v: la valeur
   * @return : true si la valeur v peut être mise dans la ligne l
   */
  private boolean lignePossible(int l, int v) {
    for (int e : grille[l])
      if (e == v)
        return false;
    return true;
  }

  /**
   * CONSEQUENT : renvoie vrai si la valeur v est possible pour la colonne c
   *
   * @param c: le n° de colonne
   * @param v: la valeur
   * @return : true si la valeur v peut être mise dans la colonne l
   */
  private boolean colonnePossible(int c, int v) {
    for (int y = 0; y < grille.length; ++y)
      if (grille[c][y] == v)
        return false;
    return true;
  }

  /**
   * CONSEQUENT : renvoie vrai si la valeur v est possible pour le carre
   * dont le coin (haut,gauche) est (i,j)
   *
   * @param i: la coordonnée x du carré dont le coin (haut,gauche) est en (i,j)
   * @param j: la coordonnée y du carré dont le coin (haut,gauche) est en (i,j)
   * @return : true si la valeur v est possible pour ce carré
   */
  private boolean carrePossible(int i, int j, int v) {
    int coinI = (i / tailleCarre) * tailleCarre;
    int coinJ = (j / tailleCarre) * tailleCarre;
    for (int i1 = 0; i1 < tailleCarre; i1++)
      for (int j1 = 0; j1 < tailleCarre; j1++)
        if (grille[coinI + i1][coinJ + j1] == v)
          return false;
    return true;
  }

  /**
   * renvoie la ligne de la case à droite de la case (i,j)
   *
   * @param i : la coordonnée x de la case
   * @param j : la coordonnée y de la case
   * @return: le n° de ligne de la case à droite de (i,j)
   */
  private int ligneSuivante(int i, int j) {
    if (j == taille - 1)
      return i + 1;
    else
      return i;
  }

  /**
   * renvoie la colonne de la case à droite de (i,j)
   *
   * @param i : la coordonnée x de la case
   * @param j : la coordonnée y de la case
   * @return: le n° de colonne qui est à droite de la case (i,j)
   */
  private int colonneSuivante(int i, int j) {
    if (j == taille - 1)
      return 0;
    else
      return j + 1;
  }

  /**
   * CONSEQUENT : remplit la grille si c'est possible
   *
   * @return : renvoie false si c'est impossible
   */
  public boolean remplir() {
    return remplir(0, 0);
  }

  /* CONSEQUENT : place une valeur en (i,j), renvoie false si c'est impossible */
  private boolean remplir(int i, int j) {
    // on a dépassé la dernière ligne donc la grille est remplie
    if (i == taille)
      return false;
    // Case déjà remplie, on passe à la suivante
    if (grille[i][j] != 0)
      return remplir(ligneSuivante(i, j), colonneSuivante(i, j));

    // on essaie toutes les valeurs possibles
    for (int k = 1; k < taille; ++k) {
      boolean ligne = lignePossible(i, k);
      boolean col = colonnePossible(j, k);
      boolean carre = carrePossible(i, j, k);
      if (ligne && col && carre) {
        grille[i][j] = k;
        if (remplir(ligneSuivante(i, j), colonneSuivante(i, j)))
          return true;
      }
    }
    grille[i][j] = 0;
    return false;
  }

  ////////////////////////////////////////////////////////////////////////////////////////////////////////////

  /**
   * Méthode privée pour dessiner une ligne
   *
   * @return: une ligne de longueur taille formée de tirets
   */
  private String separateurHorizontal() {
    String result = "||";
    // -- pour la place d'un nombre
    for (int i = 0; i < taille; i++)
      result += "--";
    // -- pour la place d'un séparateur vertical
    for (int i = 0; i < taille / tailleCarre; i++)
      result += "--";
    result += "-||\n";
    return result;
  }

  /**
   * le séparateur vertical est ||, les chiffres sont espacés d'un espace,
   * le séparateur horizontal est obtenu par la méthode separateurHorizontal()
   * voir exemple dans la classe de test
   *
   * @return : renvoie une chaine qui représente la grille
   */
  public String toString() {
    String result = "";
    String sepH = separateurHorizontal();
    for (int i = 0; i < taille; i++) {
      if (i % tailleCarre == 0)
        result += sepH;
      for (int j = 0; j < taille; j++) {
        if (j % tailleCarre == 0)
          result += "|| ";
        result += grille[i][j] + " ";
      }
      result += "||\n";
    }
    result += sepH;
    return result;
  }

}
