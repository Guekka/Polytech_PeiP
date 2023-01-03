# Jeu de quilles. PeiP1 G4, BIZEL Edgar et DAHOUN Neil

import constantes

import math
import random
import turtle
import turtle_util as tutil
import util

from dataclasses import dataclass
from typing import List

DETRUIT_PAR_JOUEUR = "J"
DETRUIT_NON = "N"
DETRUIT_PAR_ORDI = "O"


@dataclass
class Asteroide:
    turtle: turtle.Turtle
    centre: turtle.Vec2D
    positions: List[turtle.Vec2D]
    rayon_min: float
    rayon_max: float
    detruit: str = DETRUIT_NON


def _generer_asteroide(rayon_min, rayon_max, pos):
    """
    Renvoie une liste de positions formant, une fois reliées, un astéroide
    """
    liste_positions = []
    angle = 1

    while angle < 360:
        dist = random.uniform(rayon_min, rayon_max)
        nouvelle_pos = util.position_autour(pos, angle, dist)
        liste_positions.append(nouvelle_pos)
        angle += random.randint(5, 40)

    # On enlève le dernier trait s'il est invalide
    if angle > 1:
        liste_positions.pop()

    liste_positions.append(liste_positions[0])
    return liste_positions


def init(rayon_min, rayon_max, pos, couleur):
    tl = tutil.creer_turtle()
    tl.color(couleur)

    positions = _generer_asteroide(rayon_min, rayon_max, pos)
    return Asteroide(tl, pos, positions, rayon_min, rayon_max, DETRUIT_NON)


def _dessiner_destruction(asteroide):
    if asteroide.detruit == DETRUIT_PAR_JOUEUR:
        couleur = constantes.COULEUR_LASER_JOUEUR
        couleurs = constantes.COULEURS_LASER_JOUEUR
    else:
        couleur = constantes.COULEUR_LASER_ORDI
        couleurs = constantes.COULEURS_LASER_ORDI

    nombre_fissures = random.randint(asteroide.rayon_min // 16,
                                     asteroide.rayon_min // 8)

    for point in random.sample(asteroide.positions, nombre_fissures):
        tutil.trait_irregulier(tl=asteroide.turtle,
                               couleur=couleur,
                               point=point,
                               centre=asteroide.centre)

    tutil.deplacer(asteroide.turtle, asteroide.centre)
    tutil.point_degrade(tl=asteroide.turtle,
                        centre=asteroide.centre,
                        taille=asteroide.rayon_min * 1.5,
                        couleurs=couleurs)


def dessiner(asteroide):
    asteroide.turtle.clear()
    tutil.deplacer(asteroide.turtle, asteroide.positions[0])
    asteroide.turtle.begin_fill()

    for pos in asteroide.positions:
        asteroide.turtle.goto(pos)

    asteroide.turtle.end_fill()

    if asteroide.detruit != DETRUIT_NON:
        _dessiner_destruction(asteroide)


def generer_ligne(nombre, limite_gauche, limite_droite, limite_haut,
                  limite_bas):
    """
    Génère une ligne d'astéroides. Adapte leur taille pour qu'ils rentrent tous
    """
    largeur = limite_droite - limite_gauche
    hauteur = limite_haut - limite_bas

    delta_x = largeur / nombre

    rayon_max = min(largeur, hauteur) / 2.5
    rayon_min = rayon_max / 2

    asteroides = []
    x = limite_gauche + rayon_max
    y = (limite_haut + limite_bas) / 2
    for _ in range(nombre):
        couleur = random.choice(constantes.COULEURS_ASTEROIDES)
        a = init(rayon_min, rayon_max, (x, y), couleur)
        asteroides.append(a)
        x += delta_x
    return asteroides


def _taille_carre_dans_rectangle(x, y, n):
    """
    Cette fonction détermine la taille d'un carré de manière à ce que `nombre`
    carrés rentrent dans un rectangle de x * y
    """
    # Calcule le nombre de lignes et de colonnes, et la taille des carrés
    ratio = x / y
    ncols_float = math.sqrt(n * ratio)
    nrows_float = n / ncols_float

    # Trouve la meilleure option pour la hauteur
    nrows1 = math.ceil(nrows_float)
    ncols1 = math.ceil(n / nrows1)
    while nrows1 * ratio < ncols1:
        nrows1 += 1
        ncols1 = math.ceil(n / nrows1)
    taille_carre1 = y / nrows1

    # Trouve la meilleure option pour la largeur
    ncols2 = math.ceil(ncols_float)
    nrows2 = math.ceil(n / ncols2)
    while ncols2 < nrows2 * ratio:
        ncols2 += 1
        nrows2 = math.ceil(n / ncols2)
    taille_carre2 = x / ncols2

    # Trouve la meilleure valeur
    nrows, ncols, taille_carre = 0, 0, 0
    if taille_carre1 < taille_carre2:
        nrows = nrows2
        ncols = ncols2
        taille_carre = taille_carre2
    else:
        nrows = nrows1
        ncols = ncols1
        taille_carre = taille_carre1

    return taille_carre, nrows, ncols


def generer(nombre, limite_gauche, limite_droite, limite_haut, limite_bas):
    """
    Génère des lignes d'astéroides de manière à ce que tous rentrent dans le
    rectangle donné
    """
    x = limite_droite - limite_gauche
    y = limite_haut - limite_bas
    res = _taille_carre_dans_rectangle(x, y, nombre)

    diametre_max = res[0]
    nombre_par_ligne = res[2]
    nombre_par_colonne = res[1]

    astr = []

    limite_bas = limite_haut - diametre_max
    for _ in range(nombre_par_colonne - 1):
        astr += generer_ligne(nombre_par_ligne, limite_gauche, limite_droite,
                              limite_haut, limite_bas)
        limite_haut -= diametre_max
        limite_bas = limite_haut - diametre_max
    # Dernière ligne
    deja_traces = nombre_par_ligne * (nombre_par_colonne - 1)
    restant = nombre - deja_traces
    astr += generer_ligne(restant, limite_gauche, limite_droite, limite_haut,
                          limite_bas)

    return astr
