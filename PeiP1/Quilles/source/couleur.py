# Jeu de quilles. PeiP1 G4, BIZEL Edgar et DAHOUN Neil
"""
Les trois fonctions qui suivent (hex_vers_rgb, rgb_vers_hex, degrade_lineaire)
ont été trouvées sur StackOverflow
"""


def hex_vers_rgb(hex):
    ''' "#FFFFFF" -> [255,255,255] '''
    # Pass 16 to the integer function for change of base
    return [int(hex[i:i + 2], 16) for i in range(1, 6, 2)]


def rgb_vers_hex(rgb):
    ''' [255,255,255] -> "#FFFFFF" '''
    # Components need to be integers for hex to make sense
    rgb = [int(x) for x in rgb]
    return "#" + "".join(
        ["0{0:x}".format(v) if v < 16 else "{0:x}".format(v) for v in rgb])


def degrade_lineaire(hex_debut, hex_fin="#FFFFFF", n=10):
    """
    Renvoie une liste contenant n couleurs, dégradées entre hex_debut
    et hex_fin
    """
    # Starting and ending colors in RGB form
    s = hex_vers_rgb(hex_debut)
    f = hex_vers_rgb(hex_fin)
    # Initilize a list of the output colors with the starting color
    RGB_list = [s]
    # Calcuate a color at each evenly spaced value of t from 1 to n
    for t in range(1, n):
        # Interpolate RGB vector for color at the current value of t
        curr_vector = [
            int(s[j] + (float(t) / (n - 1)) * (f[j] - s[j])) for j in range(3)
        ]
        # Add it to our list of output colors
        RGB_list.append(curr_vector)

    return [rgb_vers_hex(RGB) for RGB in RGB_list]
