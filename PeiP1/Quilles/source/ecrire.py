# Jeu de quilles. PeiP1 G4, BIZEL Edgar et DAHOUN Neil

import constantes
import taille_ecran
import turtle
import turtle_util as tutil
import util

_tl: turtle.Turtle


def init():
    global _tl
    _tl = tutil.creer_turtle()


def _calculer_taille_texte(texte):
    """
    Calcule la police que devra utiliser le texte pour être bien visible
    """

    # Après plusieurs essais, il a été déterminé que ce calcul fonctionnait
    # correctement en Courier New
    _, longueur_max = util.ligne_la_plus_longue(texte)
    return int(0.6 * taille_ecran.x / longueur_max)


def _police(taille):
    return "Courier New", taille, "normal"


def _pos():
    return 0, taille_ecran.y * 0.2


def message(texte):
    global _tl
    tutil.deplacer(_tl, _pos())

    _tl.color(constantes.COULEUR_PAR_DEFAUT)

    police = _police(_calculer_taille_texte(texte))
    _tl.write(texte, align="center", font=police)


def effacer():
    """
    Efface le texte écrit précédemment
    Normalement, cela devrait être aussi simple qu'appeler
    `_tl.clear()`. Mais j'ignore pourquoi, le texte ne s'efface pas
    On dessine donc un rectangle par dessus
    """
    global _tl

    _tl.clear()
    """
    x, y = _pos()
    tutil.deplacer(_tl, (x - taille_ecran.x / 2, y))

    _tl.color(turtle.bgcolor())
    _tl.begin_fill()
    _tl.setheading(0)
    _tl.forward(taille_ecran.x)
    _tl.left(90)
    _tl.forward(taille_ecran.y / 10)
    _tl.left(90)
    _tl.forward(taille_ecran.x)
    _tl.left(90)
    _tl.forward(taille_ecran.y / 10)
    _tl.end_fill()
    """
