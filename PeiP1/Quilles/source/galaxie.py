# Jeu de quilles. PeiP1 G4, BIZEL Edgar et DAHOUN Neil

import constantes
import etoile
import random
import taille_ecran
import util


def init(nombre_etoiles):

    x, y = util.position_aleatoire()
    etoiles = []

    for _ in range(nombre_etoiles):
        angle = random.randint(-180, 180)

        dist = taille_ecran.x / 100

        x, y = util.position_autour((x, y), angle, dist)

        couleur = random.choice(constantes.COULEURS)

        taille_min = taille_ecran.x / 300
        taille_max = taille_ecran.x / 200
        taille = random.uniform(taille_min, taille_max)

        etoiles.append(etoile.init(taille, couleur, (x, y)))
    return etoiles


def generer():
    etoiles = []
    for _ in range(constantes.GALAXIE_NOMBRE):
        nombre_etoiles = random.randint(constantes.GALAXIE_NOMBRE_ETOILES_MIN,
                                        constantes.GALAXIE_NOMBRE_ETOILES_MAX)
        etoiles += init(nombre_etoiles)
    return etoiles
