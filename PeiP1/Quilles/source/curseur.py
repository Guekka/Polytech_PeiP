# Jeu de quilles. PeiP1 G4, BIZEL Edgar et DAHOUN Neil

import constantes
import turtle
import turtle_util as tutil

_tl: turtle.Turtle


def init():
    global _tl
    _tl = tutil.creer_turtle()


def dessiner(jeu_etat):
    global _tl
    _tl.clear()

    # On ne dessine pas le curseur si le jeu est terminé
    if len(jeu_etat.quilles) == 0:
        return

    debut, fin = jeu_etat.quilles_selectionnees

    for ast in jeu_etat.asteroides[debut:fin + 1]:
        pos = ast.centre
        taille = ast.rayon_min * 1.5
        tutil.deplacer(_tl, pos)
        _tl.dot(taille, constantes.COULEUR_PAR_DEFAUT)
