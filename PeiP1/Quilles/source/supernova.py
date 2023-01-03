# Jeu de quilles. PeiP1 G4, BIZEL Edgar et DAHOUN Neil

import constantes
import turtle
import util
import random
import math
import taille_ecran
import turtle_util as tutil

from collections import namedtuple

Supernova = namedtuple(
    "Supernova",
    ["turtle", "couleurs", "nombre_poly", "taille", "ecart", "nombre_cotes"])


def init(couleurs, pos, nombre_poly=30, taille=100, ecart=0.15, cotes=8):
    tl = tutil.creer_turtle()
    tutil.deplacer(turtle, pos)

    return Supernova(turtle=tl,
                     couleurs=couleurs,
                     nombre_poly=nombre_poly,
                     taille=taille,
                     ecart=ecart,
                     nombre_cotes=cotes)


def dessiner(nova):
    nova.turtle.clear()
    taille = nova.taille
    orig_pos = nova.turtle.pos()
    orig_heading = nova.turtle.heading()

    angle = 360 / nova.nombre_cotes
    for _ in range(nova.nombre_poly):
        for _ in range(nova.nombre_cotes):
            couleur = random.choice(nova.couleurs)
            nova.turtle.color(couleur)
            nova.turtle.forward(taille)
            nova.turtle.left(angle)
        taille = _preparer_trait_suivant(nova, taille, angle)

    tutil.deplacer(nova.turtle, orig_pos)
    nova.turtle.setheading(orig_heading)


def avancer_de(nova, x, y):
    curr_x, curr_y = nova.turtle.pos()
    tutil.deplacer(nova.turtle, (curr_x + x, curr_y + y))


def rayon(nova):
    """
    Renvoie une (forte) approximation du rayon
    """
    return nova.taille * nova.nombre_cotes / 2


def reset(nova):
    pos = util.position_debut(nova.turtle.pos(), rayon(nova))

    tutil.deplacer(nova.turtle, pos)


# Voir le schéma du problème 3 sur les énoncés itératifs
def _preparer_trait_suivant(nova, taille, GBK):
    GB = taille * nova.ecart
    nova.turtle.forward(GB)

    GK = GB * math.sin(math.radians(GBK))
    BK = math.sqrt(GB**2 - GK**2)

    FK = taille - GB + BK
    FG = math.sqrt(FK**2 + GK**2)
    GFB = math.degrees(math.asin(GK / FG))

    nova.turtle.left(GFB)

    return FG


def sorti_de_lecran(nova):
    return util.depasse_ecran(nova.turtle.pos(), rayon(nova))


def generer():
    supernovas = []
    for _ in range(constantes.SUPERNOVA_NOMBRE):
        taille_min = taille_ecran.x / 40
        taille_max = taille_ecran.x / 20
        s = init(
            couleurs=constantes.COULEURS,
            pos=util.position_aleatoire(),
            taille=random.uniform(taille_min, taille_max),
        )
        supernovas.append(s)
    return supernovas
