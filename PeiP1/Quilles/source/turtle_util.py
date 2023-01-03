# Jeu de quilles. PeiP1 G4, BIZEL Edgar et DAHOUN Neil

import turtle
import util
import random


def creer_turtle():
    """
    Renvoie une tortue avec des paramètres par défaut
    """
    tl = turtle.Turtle(undobuffersize=0)
    tl.hideturtle()
    tl.speed(0)
    return tl


def deplacer(turtle, pos):
    """
    Déplace la tortue et la prépare à écrire
    """
    turtle.penup()
    turtle.setpos(pos)
    turtle.pendown()


def point_degrade(tl, centre, taille, couleurs):
    """
    Dessine un point de taille "taille", contenant des points de plus en
    plus petits
    """
    deplacer(tl, centre)

    delta = taille / len(couleurs)

    for c in couleurs:
        tl.dot(taille, c)
        taille -= delta


def trait_irregulier(tl, couleur, point, centre):
    orig = tl.pen()

    tl.color(couleur)

    tl.pensize(2)
    deplacer(tl, point)

    angle_base = util.angle_normale(centre, point)
    rayon = util.distance(tl.pos(), centre)
    longueur_max = rayon / 5
    while rayon > longueur_max:
        angle = random.uniform(angle_base - 5, angle_base + 5)
        point = util.position_autour(centre, angle, rayon)
        tl.goto(point)
        rayon -= random.uniform(0, longueur_max)

    tl.goto(centre)

    tl.pen(orig)
