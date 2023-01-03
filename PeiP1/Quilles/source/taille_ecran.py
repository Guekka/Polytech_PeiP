# Jeu de quilles. PeiP1 G4, BIZEL Edgar et DAHOUN Neil

import turtle

# Taille de l'écran par défaut
x = 1920
y = 1080


def mettre_a_jour(nouveau_x=None, nouveau_y=None):
    global x, y

    if nouveau_x is None:
        nouveau_x = turtle.window_width()

    if nouveau_y is None:
        nouveau_y = turtle.window_height()

    x, y = nouveau_x, nouveau_y
