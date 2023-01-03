# Jeu de quilles. PeiP1 G4, BIZEL Edgar et DAHOUN Neil

import arriere_plan
import constantes
import curseur
import ecrire
import jeu
import taille_ecran
import texte
import turtle

# Utilisé pour passer des arguments aux fonctions appelées par turtke.onkey
from functools import wraps

# Utilisé pour empêcher une erreur à la fermeture
en_cours = True


def plein_ecran(ecran):
    ecran.screensize()
    ecran.setup(width=0.5, height=1.0, startx=None, starty=None)
    taille_ecran.mettre_a_jour()
    # On enlève les touches fermer, maximiser, réduire
    canvas = ecran.getcanvas()
    root = canvas.winfo_toplevel()
    root.overrideredirect(1)


def touche_droite(jeu_etat):
    jeu.action_suivante(jeu_etat)


def touche_gauche(jeu_etat):
    jeu.action_precedente(jeu_etat)


def verifier_jeu_termine(jeu_etat, texte_a_afficher):
    if jeu.est_termine(jeu_etat):
        clavier_base()
        ecrire.effacer()
        ecrire.message(texte_a_afficher + '\n' + texte.TOUCHE_POUR_DEMARRER)


def espace(jeu_etat):
    # Joueur joue
    jeu.jouer_joueur(jeu_etat)
    verifier_jeu_termine(jeu_etat, texte.MESSAGE_VICTOIRE)

    # Ordi joue
    jeu.jouer_ordi(jeu_etat)
    ecrire.effacer()
    ecrire.message(texte.ORDI_A_JOUE(jeu_etat.action))

    verifier_jeu_termine(jeu_etat, texte.MESSAGE_DEFAITE)

    # On remet une position valide
    if not jeu.est_termine(jeu_etat):
        jeu.action_suivante(jeu_etat)


def echap():
    global en_cours
    en_cours = False


def clavier_base():
    turtle.onkey(None, "Left")  # type: ignore
    turtle.onkey(None, "Right")  # type: ignore

    turtle.onkey(commencer, "r")
    turtle.onkey(None, "space")  # type: ignore

    turtle.onkey(echap, "Escape")


def clavier_complet(jeu_etat):
    @wraps(touche_droite)
    def touche_droite_():
        return touche_droite(jeu_etat)

    turtle.onkey(touche_droite_, "Right")

    @wraps(touche_gauche)
    def touche_gauche_():
        return touche_gauche(jeu_etat)

    turtle.onkey(touche_gauche_, "Left")

    @wraps(espace)
    def espace_():
        return espace(jeu_etat)

    turtle.onkey(espace_, "space")

    turtle.onkey(echap, "Escape")


def init():
    turtle.hideturtle()

    ecran = turtle.Screen()
    ecran.tracer(False)
    plein_ecran(ecran)
    ecran.listen()

    curseur.init()
    ecrire.init()


def reset():
    turtle.reset()
    turtle.hideturtle()

    ecran = turtle.Screen()
    ecran.clear()
    ecran.tracer(False)
    plein_ecran(ecran)
    ecran.listen()

    arriere_plan.reset()

    turtle.bgcolor(constantes.COULEUR_FOND)

    clavier_base()

    return jeu.init(), ecran


def commencer():
    jeu_etat, ecran = reset()
    clavier_complet(jeu_etat)

    while en_cours:
        ecran.update()
        arriere_plan.cycle()

        jeu.afficher_quilles(jeu_etat)
        curseur.dessiner(jeu_etat)
    turtle.Screen().bye()


if __name__ == '__main__':
    try:
        init()
        reset()
        ecrire.message(texte.TOUCHE_POUR_DEMARRER)
        turtle.done()
    except Exception:
        exit(0)
