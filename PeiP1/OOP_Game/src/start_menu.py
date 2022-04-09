import sys

import pygame as pg
from pygame.surface import Surface

from constants import BACKGROUND_COLOR, DEFAULT_ROOMCOUNT
from game import Game
from settings import Settings
from ui_elements import Button, SwitchButton, layout


def play(settings: Settings, screen: Surface):
    screen.fill(BACKGROUND_COLOR)
    game = Game(screen, settings)
    game.run()


def options(surface: Surface, settings: Settings):
    available_tilecount = list(range(1000, 10000, 100))
    tilecount_sbutton = SwitchButton("Tile Count", available_tilecount, (0, 0))
    available_roomcount = list(range(3, 30))
    roomcount_sbutton = SwitchButton("Room count", available_roomcount, (0, 0))

    quit_button = Button("Return", (100, 100))
    layout(surface, [tilecount_sbutton, roomcount_sbutton, quit_button])

    tilecount = settings.x_tile_count() * settings.y_tile_count()
    closest_tilecount = 100 * round(tilecount / 100)
    closest_tilecount = min(9900, max(1000, closest_tilecount))  # Clamp

    tilecount_sbutton.set_selected(closest_tilecount)
    roomcount_sbutton.set_selected(settings.room_count)

    while True:
        mouse = pg.mouse.get_pos()
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                sys.exit()

            #checks if a mouse is clicked
            if ev.type == pg.MOUSEBUTTONDOWN:
                tilecount_sbutton.handle_buttons(mouse)
                roomcount_sbutton.handle_buttons(mouse)
                settings.set_tilecount(tilecount_sbutton.get_selected())
                settings.room_count = roomcount_sbutton.get_selected()
                if quit_button.collides(mouse):
                    return

        surface.fill(BACKGROUND_COLOR)

        tilecount_sbutton.display(surface, mouse)
        roomcount_sbutton.display(surface, mouse)
        quit_button.display(surface, mouse)

        pg.display.flip()


def main_menu(screen: Surface):
    play_button = Button("Play", (0, 0))
    options_button = Button("Options", (0, 0))
    quit_button = Button("Quit", (0, 0))
    layout(screen, [play_button, options_button, quit_button])

    sets = Settings(screen.get_width(), screen.get_height(), DEFAULT_ROOMCOUNT)

    # Main loop
    while True:
        mouse = pg.mouse.get_pos()
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                sys.exit()

            #checks if a mouse is clicked
            if ev.type == pg.MOUSEBUTTONDOWN:
                if play_button.collides(mouse):
                    play(sets, screen)
                elif options_button.collides(mouse):
                    options(screen, sets)
                elif quit_button.collides(mouse):
                    sys.exit()

        screen.fill(BACKGROUND_COLOR)

        for button in [play_button, options_button, quit_button]:
            button.display(screen, mouse)

        pg.display.flip()
