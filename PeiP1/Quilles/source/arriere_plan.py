# Jeu de quilles. PeiP1 G4, BIZEL Edgar et DAHOUN Neil

import constantes
import constellation
import etoile
import galaxie
import supernova

from sys import modules

_astres = []


def reset():
    global _astres

    _astres = etoile.generer()
    _astres += constellation.generer()
    _astres += supernova.generer()
    _astres += galaxie.generer()


def _cycle_astre(astre):
    """
    Cycle de base pour les astres en arrière plan
    """

    # La ligne suivante permet d'utiliser les fonctions
    # définies dans le module de l'astre, quel qu'il soit
    mod = modules[astre.__module__]

    mod.avancer_de(  # type: ignore
        astre, constantes.VITESSE_X, constantes.VITESSE_Y)

    if mod.sorti_de_lecran(astre):  # type: ignore
        mod.reset(astre)  # type: ignore
    else:
        mod.dessiner(astre)  # type: ignore


def cycle():
    for a in _astres:
        _cycle_astre(a)
