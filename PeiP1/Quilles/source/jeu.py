# Jeu de quilles. PeiP1 G4, BIZEL Edgar et DAHOUN Neil

import action
import asteroide
import random
import taille_ecran

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Jeu:
    """
    Contient l'état du jeu
    """
    quilles: List[List[int]]
    nombre_quilles: int

    quilles_selectionnees: Tuple[int, int]
    action: str

    asteroides: List[asteroide.Asteroide]


def init():
    nb_q = random.randint(8, 20)

    zone_de_jeu_x = taille_ecran.x / 6
    zone_de_jeu_y = taille_ecran.y / 6

    ast = asteroide.generer(nb_q, -zone_de_jeu_x, zone_de_jeu_x, zone_de_jeu_y,
                            -zone_de_jeu_y)

    q = [[0, nb_q - 1]]

    return Jeu(quilles=q,
               nombre_quilles=nb_q,
               quilles_selectionnees=(0, 0),
               action=action.ACTION_PAR_DEFAUT,
               asteroides=ast)


def nombre_lignes(jeu):
    return len(jeu.quilles)


def afficher_quilles(jeu):
    for ast in jeu.asteroides:
        asteroide.dessiner(ast)


def _selectionner_quilles_milieu(jeu):
    """
    Sélectionne les quilles qui seraient supprimées en jouant au milieu
    """
    index, _ = action.separer_action(jeu.action)

    ligne = jeu.quilles[index]
    nombreQuilles = ligne[1] + 1 - ligne[0]

    if nombreQuilles <= 2:
        jeu.quilles_selectionnees = tuple(jeu.quilles[index])
        return

    if nombreQuilles % 2 == 0:
        # Le milieu est la deuxième quille en cas de nombre pair
        milieu = (ligne[1] + ligne[0]) // 2 + 1
        # Et le trou commence une quille avant le milieu
        debutTrou = milieu - 1
    else:
        milieu = (ligne[1] + ligne[0]) // 2
        # En cas d'impair, le trou commence sur le milieu ou une case avant
        debutTrou = random.randint(milieu - 1, milieu)

    finTrou = debutTrou + 1

    jeu.quilles_selectionnees = debutTrou, finTrou


def _selectionner_quilles_cote(jeu):
    """
    Sélectionne les quilles qui seraient supprimées en jouant sur le côté
    """
    index, pos = action.separer_action(jeu.action)

    # Contient seulement une quille
    if jeu.quilles[index][0] == jeu.quilles[index][1]:
        jeu.quilles_selectionnees = tuple(jeu.quilles[index])
        return

    quille = jeu.quilles[index][0 if pos == 'G' else 1]
    jeu.quilles_selectionnees = quille, quille


def selectionner_quilles(jeu):
    """
    Sélectionne les quilles qui seraient supprimées
    """
    _, pos = action.separer_action(jeu.action)
    assert action.action_valide(nombre_lignes(jeu), jeu.action)

    if pos == 'M':
        _selectionner_quilles_milieu(jeu)
    else:
        _selectionner_quilles_cote(jeu)


def jouer_milieu(jeu, joueur):
    if jeu.quilles_selectionnees is None:
        selectionner_quilles(jeu)

    index, _ = action.separer_action(jeu.action)
    debut, fin = jeu.quilles_selectionnees

    ligne = jeu.quilles[index]
    del jeu.quilles[index]

    for ast in jeu.asteroides[debut:fin + 1]:
        ast.detruit = joueur

    if debut > ligne[0]:
        jeu.quilles.insert(index, [ligne[0], debut - 1])
        index += 1

    if fin < ligne[1]:
        jeu.quilles.insert(index, [fin + 1, ligne[1]])


def jouer_cote(jeu, joueur):
    index, pos = action.separer_action(jeu.action)

    # Contient seulement une quille
    if jeu.quilles[index][0] == jeu.quilles[index][1]:
        jeu.asteroides[jeu.quilles[index][0]].detruit = joueur
        del jeu.quilles[index]
    elif pos == 'G':
        jeu.asteroides[jeu.quilles[index][0]].detruit = joueur
        jeu.quilles[index][0] += 1
    else:
        jeu.asteroides[jeu.quilles[index][1]].detruit = joueur
        jeu.quilles[index][1] -= 1


def jouer(jeu, joueur):
    assert action.action_valide(nombre_lignes(jeu), jeu.action)

    _, pos = action.separer_action(jeu.action)

    if pos == 'M':
        jouer_milieu(jeu, joueur)
    else:
        jouer_cote(jeu, joueur)


def jouer_joueur(jeu):
    jouer(jeu, asteroide.DETRUIT_PAR_JOUEUR)


def jouer_ordi(jeu):
    jeu.action = action.action_aleatoire(nombre_lignes(jeu))
    selectionner_quilles(jeu)
    jouer(jeu, asteroide.DETRUIT_PAR_ORDI)


def est_termine(jeu):
    return nombre_lignes(jeu) == 0


def _action_helper(jeu, func):
    if nombre_lignes(jeu) <= 1:
        jeu.action = func(nombre_lignes(jeu), jeu.action)
        selectionner_quilles(jeu)
        return

    select = jeu.quilles_selectionnees
    while jeu.quilles_selectionnees == select:
        jeu.action = func(nombre_lignes(jeu), jeu.action)
        selectionner_quilles(jeu)


def action_precedente(jeu):
    _action_helper(jeu, action.action_precedente)


def action_suivante(jeu):
    _action_helper(jeu, action.action_suivante)
