# Jeu de quilles. PeiP1 G4, BIZEL Edgar et DAHOUN Neil

import constantes
import random
import taille_ecran
import turtle_util as tutil
import util

from collections import namedtuple

# Alias
Etoile = namedtuple('Etoile', ['turtle', 'taille'])


# ### Etoile ####
def init(taille, couleur, pos):
    tl = tutil.creer_turtle()
    tutil.deplacer(tl, pos)
    tl.color(couleur)

    return Etoile(tl, taille)


def avancer_de(etoile, dx, dy):
    x, y = etoile.turtle.pos()
    tutil.deplacer(etoile.turtle, (x + dx, y + dy))


def dessiner(etoile):
    etoile.turtle.clear()
    etoile.turtle.pendown()
    etoile.turtle.begin_fill()
    for _ in range(5):
        etoile.turtle.left(144)
        etoile.turtle.forward(etoile.taille)
    etoile.turtle.end_fill()


def reset(etoile):
    pos = util.position_debut(etoile.turtle.pos(), etoile.taille)
    tutil.deplacer(etoile.turtle, pos)


def sorti_de_lecran(etoile):
    return util.depasse_ecran(etoile.turtle.pos(), etoile.taille)


def generer():
    etoiles = []
    for _ in range(constantes.ETOILE_NOMBRE):
        pos = util.position_aleatoire()
        taille_min = taille_ecran.x / 200
        taille_max = taille_ecran.x / 50

        taille = random.uniform(taille_min, taille_max)
        etoiles.append(init(taille, constantes.COULEUR_PAR_DEFAUT, pos))
    return etoiles
