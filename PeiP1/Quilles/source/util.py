# Jeu de quilles. PeiP1 G4, BIZEL Edgar et DAHOUN Neil

import constantes
import math
import random
import taille_ecran


def avant_ecran(pos, rayon):
    """
    Renvoie vrai si l'astre est sorti de l'écran, faux sinon.
    Seuls les bords haut et droit sont pris en compte
    """
    x, y = pos
    depassement_x = x - rayon < (taille_ecran.x / 2)
    depassement_y = y - rayon < (taille_ecran.y / 2)
    return depassement_x or depassement_y


def depasse_ecran(pos, rayon):
    """
    Renvoie vrai si l'astre est sorti de l'écran, faux sinon.
    Seuls les bords haut et droit sont pris en compte
    """
    x, y = pos
    depassement_x = x - rayon > (taille_ecran.x / 2)
    depassement_y = y - rayon > (taille_ecran.y / 2)
    return depassement_x or depassement_y


def position_debut(pos, rayon):
    """
    Déplace la tortue de manière à la faire retourner au début de l'écran.
    La position actuelle et le rayon sont pris en compte afin de faire
    apparaître la tortue peu avant le bord de l'écran
    """
    x, y = pos
    delta_x = 1.5 * taille_ecran.x + rayon
    delta_y = constantes.VITESSE_Y / constantes.VITESSE_X * delta_x

    return x - delta_x, y - delta_y


def position_aleatoire(posMin=None, posMax=None):
    """
    Renvoie un emplacement aléatoire entre les coordonnées minimum et maximum
    """

    if posMin is None:
        posMin = int(-taille_ecran.x / 1.5), int(-taille_ecran.y / 1.5)

    if posMax is None:
        posMax = int(taille_ecran.x / 1.5), int(taille_ecran.y / 1.5)

    x = random.randint(posMin[0], posMax[0])
    y = random.randint(posMin[1], posMax[1])
    return x, y


def position_autour(pos, angle, distance):
    x, y = pos

    x += distance * math.cos(math.radians(angle))
    y += distance * math.sin(math.radians(angle))

    return x, y


def norme(vec):
    return math.sqrt(vec[0]**2 + vec[1]**2)


def distance(point_un, point_deux):
    x = point_deux[0] - point_un[0]
    y = point_deux[1] - point_un[1]
    return norme((x, y))


def scalaire(vec_un, vec_deux):
    return vec_un[0] * vec_deux[1] - vec_un[1] * vec_deux[0]


def angle_normale(centre, point):
    y = (point[1] - centre[1])
    x = (point[0] - centre[0])
    return math.degrees(math.atan2(y, x))


def ligne_la_plus_longue(texte):
    longueur_max = 0
    ligne_max = ''
    for line in texte.split('\n'):
        if (len(line) > longueur_max):
            longueur_max = len(line)
            ligne_max = line
    return ligne_max, longueur_max
