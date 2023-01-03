# Jeu de quilles. PeiP1 G4, BIZEL Edgar et DAHOUN Neil
"""
Ce fichier définit les constantes utilisées dans le programme
"""

import couleur

# Mode debug
DEBUG = False

# Couleurs par défaut
COULEURS = ["#058396", "#0275A6", "#827E01", "#fc99da"]

COULEURS_ASTEROIDES = [
    "#dbdbdb", "#c4c4c4", "#c4c4c4", "#a8a4aa", "#aaa4a8", "#aea7ac",
    "#a7a2a7", "#ac9cac", "#afa0ac", "#a99ca9"
]

COULEUR_FOND = "#191970"  # MidnightBlue
COULEUR_PAR_DEFAUT = "#FFFFFF"  # White

COULEUR_LASER_JOUEUR = "#ff0000"
# On stocke le dégradé pour éviter de le recalculer
COULEURS_LASER_JOUEUR = couleur.degrade_lineaire(
    COULEUR_LASER_JOUEUR, COULEUR_PAR_DEFAUT, 20) + couleur.degrade_lineaire(
        COULEUR_PAR_DEFAUT, "#ffff00", 20)

COULEUR_LASER_ORDI = "#000000"
# On stocke le dégradé pour éviter de le recalculer
COULEURS_LASER_ORDI = couleur.degrade_lineaire(COULEUR_LASER_ORDI,
                                               COULEUR_PAR_DEFAUT, 20)

# Vitesse de déplacement des astres
VITESSE = 20

VITESSE_X = 1 * VITESSE
VITESSE_Y = 0.2 * VITESSE

# Nombre d'éléments à l'écran
ETOILE_NOMBRE = 40
CONSTELLATION_NOMBRE = 3
GALAXIE_NOMBRE = 3
SUPERNOVA_NOMBRE = 1

CONSTELLATION_NOMBRE_ETOILES_MIN = 15
CONSTELLATION_NOMBRE_ETOILES_MAX = 20

GALAXIE_NOMBRE_ETOILES_MIN = 20
GALAXIE_NOMBRE_ETOILES_MAX = 30
