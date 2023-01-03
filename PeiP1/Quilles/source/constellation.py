# Jeu de quilles. PeiP1 G4, BIZEL Edgar et DAHOUN Neil

import constantes
import etoile
import random
import taille_ecran
import turtle_util as tutil
import util

from collections import namedtuple

Constellation = namedtuple("Constellation", ["turtle", "etoiles"])


def init(nombre_etoiles, couleur=constantes.COULEUR_PAR_DEFAUT):
    tl = tutil.creer_turtle()
    tl.color(couleur)

    pos = util.position_aleatoire()
    prev_pos = pos
    etoiles = []
    for _ in range(nombre_etoiles):
        taille_min = taille_ecran.x / 400
        taille_max = taille_ecran.x / 100

        first = etoile.init(random.uniform(taille_min, taille_max),
                            constantes.COULEUR_PAR_DEFAUT, pos)

        angle = random.randint(-90, 90)

        distance_min = taille_ecran.x // 60
        distance_max = taille_ecran.x // 30

        distance = random.randint(distance_min, distance_max)
        pos = util.position_autour(prev_pos, angle, distance)

        second = etoile.init(random.randint(7, 15),
                             constantes.COULEUR_PAR_DEFAUT, pos)

        etoiles.append(first)
        etoiles.append(second)

        prev_pos = pos

    return Constellation(tl, etoiles)


def avancer_de(constellation, x, y):
    for e in constellation.etoiles:
        etoile.avancer_de(e, x, y)


def dessiner_lien(constellation, pos1, pos2):
    """
    Trace le lien entre deux étoiles
    """

    # On évite de tracer un trait si les deux étoiles sont trop éloignées
    # Cela se produit généralement quand une étoile a dépassé le bord, mais
    # pas l'autre
    # Ce qui se traduit par un trait immense sur toute la carte
    if util.distance(pos1, pos2) > 100:
        return

    tutil.deplacer(constellation.turtle, pos1)
    constellation.turtle.goto(pos2)


def dessiner(constellation):
    constellation.turtle.clear()

    # Toutes les étoiles sauf la dernière
    for i in range(len(constellation.etoiles) - 1):
        etoile.dessiner(constellation.etoiles[i])

        orig = constellation.etoiles[i].turtle.pos()
        target = constellation.etoiles[i + 1].turtle.pos()

        dessiner_lien(constellation, orig, target)

    # La dernière étoile n'a pas été dessinée
    dessiner_lien(constellation, constellation.etoiles[-2].turtle.pos(),
                  constellation.etoiles[-1].turtle.pos())
    etoile.dessiner(constellation.etoiles[-1])


def sorti_de_lecran(constellation):
    for e in constellation.etoiles:
        if not util.depasse_ecran(e.turtle.pos(), e.taille):
            return False
    return True


def reset(constellation):
    for e in constellation.etoiles:
        etoile.reset(e)


def generer():
    constellations = []
    for _ in range(constantes.CONSTELLATION_NOMBRE):
        nombre_etoiles = random.randint(
            constantes.CONSTELLATION_NOMBRE_ETOILES_MIN,
            constantes.CONSTELLATION_NOMBRE_ETOILES_MAX)

        constellations.append(init(nombre_etoiles))
    return constellations
