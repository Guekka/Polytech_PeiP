import pygame as pg
from pygame import freetype

from constants import DEFAULT_TILESIZE, DEFAULT_UI_SQUARE_SIZE
from map import init as init_map
from sounds import init as init_sounds
from start_menu import main_menu
from textures import init as init_image


def init():
    # Only tested on ver 2
    assert pg.version.vernum[0] >= 2

    pg.init()
    freetype.init()
    pg.mixer.init()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

    init_image(DEFAULT_TILESIZE, DEFAULT_UI_SQUARE_SIZE)
    init_map()
    init_sounds()

    return screen


def main():
    screen = init()
    main_menu(screen)


if __name__ == '__main__':
    main()
