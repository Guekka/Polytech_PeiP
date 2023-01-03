# Jeu de quilles. PeiP1 G4, BIZEL Edgar et DAHOUN Neil

import random

ACTION_PAR_DEFAUT = "0:G"


def separer_action(action):
    """
    Sépare les deux parties d'une action
    """
    idx, pos = action.split(":")
    idx = int(idx)

    return idx, pos


def creer_action(idx, pos):
    return f"{idx}:{pos}"


def action_precedente(nombre_lignes, action):
    """
    Renvoie l'action précédente. Exemple : 1:M => 1:G
    """
    action = assainir_action(action, nombre_lignes)
    idx, pos = separer_action(action)

    if idx < 0:
        idx = nombre_lignes - 1

    if pos == 'G':
        if idx <= 0:
            idx = nombre_lignes - 1
        else:
            idx -= 1

        pos = 'D'

    elif pos == 'M':
        pos = 'G'
    else:
        pos = 'M'

    return creer_action(idx, pos)


def action_suivante(nombre_lignes, action):
    """
    Renvoie l'action suivante. Exemple : 1:M => 1:D
    """
    action = assainir_action(action, nombre_lignes)
    idx, pos = separer_action(action)

    if pos == 'G':
        pos = 'M'
    elif pos == 'M':
        pos = 'D'
    else:
        if idx >= nombre_lignes - 1:
            idx = 0
        else:
            idx += 1

        pos = 'G'

    return creer_action(idx, pos)


def assainir_action(action, nombre_lignes):
    """
    Vérifie qu'une action est valide.
    Si elle ne l'est pas, renvoie une action valide.
    """
    idx, pos = separer_action(action)

    if idx >= nombre_lignes:
        idx = 0
    elif idx < 0:
        idx = nombre_lignes - 1

    if not position_valide(pos):
        pos = "G"

    return creer_action(idx, pos)


def position_valide(pos):
    """
    Renvoie un booléen indiquant si une position est valide
    """
    return pos == 'G' or pos == 'M' or pos == 'D'


def ligne_valide(nombre_lignes, ligne):
    """
    Renvoie un booléen indiquant si une ligne est valide
    """
    return ligne >= 0 and ligne < nombre_lignes


def action_valide(nombre_lignes, action):
    """
    Renvoie un booléen indiquant si l'action est valide
    """
    idx, pos = separer_action(action)
    return position_valide(pos) and ligne_valide(nombre_lignes, idx)


def action_aleatoire(nombre_lignes):
    """
    Renvoie une action aléatoire
    """
    ligne = random.randint(0, nombre_lignes - 1)
    pos = random.choice(['G', 'M', 'D'])
    return creer_action(ligne, pos)
