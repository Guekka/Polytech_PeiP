from __future__ import annotations

import sys
from time import sleep
from typing import Any, Callable, Dict

import pygame as pg
from pygame.surface import Surface

import textures
from constants import MAX_INVENTORY
from coord import Coord
from creature import Hero
from element import Tile
from element_list import ElementList
from element_manager import ElementManager
from hud import HUD
from map import Map
from map_generator import MapGenerator
from settings import Settings
from sounds import Music, Sounds


class Game:
    "The main class"
    dir = {
        "z": Coord(0, -1),
        "s": Coord(0, 1),
        "d": Coord(1, 0),
        "q": Coord(-1, 0)
    }

    _actions: Dict[str, Callable[[Hero, Game], Any]] = {
        'z': lambda _, game: game.move_hero('z'),
        's': lambda _, game: game.move_hero('s'),
        'q': lambda _, game: game.move_hero('q'),
        'd': lambda _, game: game.move_hero('d'),
        ' ': lambda _h, _g: None
    }

    _actions_no_update: Dict[str, Callable[[Hero, Game], Any]] = {
        'c': lambda hero, _: hero.__setattr__('hp', 999),  # Cheat
        'r': lambda _, game: game.start(),  # Restart
        'l': lambda _, game: game.sleep_hero(),
        'k': lambda hero, _: hero.__setattr__('hp', 0),
        't': lambda hero, _: hero.inventory.destroy_equipped()
    }

    def __init__(self, screen: Surface, settings: Settings):
        """
        Initializes all the internal variables
        """
        # decorate the game window
        pg.display.set_caption("Roguelike")

        self._screen = screen
        self._settings = settings
        self._floor_cleared = False
        self._hero_slept = False

        self._background: Surface = Surface(
            (screen.get_width(), screen.get_height()))

        self.start()
        self._reload_textures()

    def _reload_textures(self):
        """
        Reloads textures for all elements on the map
        """
        settings = self._settings
        textures.init(settings.tile_size(), settings.ui_square_size())

        for line in self.floor:
            for e in line:
                e.reload_texture()
        self._init_background()

    def move_hero(self, key: str):
        self.floor.move_hero(self.hero, Game.dir[key])

    def sleep_hero(self):
        if self._hero_slept:
            Sounds.play("Denied")
            return

        self._hero_slept = True

        for _ in range(10):
            if self.hero.hp <= 0:
                return

            self.floor.move_all_monsters()
            self.floor.move_projectiles()
            self._draw()
            sleep(0.1)

        self.hero.heal(5)

    def _init_background(self):
        """
        A pre-rendered background to improve performance
        """

        # First pass, walls everywhere
        wall = Map.empty.get_tile()
        tilesize = self._settings.tile_size()

        for x in range(0, self._background.get_width(), tilesize):
            for y in range(0, self._background.get_height(), tilesize):
                self._background.blit(wall, (x, y))

        # Ground when needed
        for x in range(0, self.floor.width):
            for y in range(0, self.floor.height):
                e = self.floor.get(Coord(x, y))
                tex = e.get_tile()
                if not isinstance(e, Tile):
                    tex = Map.ground.get_tile()

                pos = (x * tilesize, y * tilesize)
                self._background.blit(tex, pos)

    def start(self):
        self.hero = Hero(MAX_INVENTORY)
        self.level = 1

        # Init HUD
        sets = self._settings
        hud_surface = self._screen.subsurface(
            [0, sets.game_height(),
             sets.width(),
             sets.hud_height()])

        self.hud = HUD(hud_surface, self.hero, self._settings)

        self._build_floor()

    def _build_floor(self):
        self.floor = Map(self._settings.x_tile_count(),
                         self._settings.y_tile_count(), self.hero)
        self._hero_slept = False
        generator = MapGenerator(self.floor)
        el_list = ElementList()
        manager = ElementManager(el_list, self.level)
        generator.generate(self._settings.room_count, manager)
        self._init_background()

    def run(self):
        "Game loop"

        while self.hero.hp > 0:
            self._draw()
            if self._events():
                self._update()

    def quit(self):
        pg.quit()
        sys.exit()

    def _update(self):
        # Have to move monsters first
        self.floor.move_all_monsters()
        self.floor.move_projectiles()

        # Handle level cleared
        if not self._floor_cleared and self.floor.cleared():
            self.floor.spawn_stairs()
            self._floor_cleared = True

        if self._floor_cleared and self.floor.stairs_taken:
            Sounds.play("Stairs")
            self._floor_cleared = False
            self.level += 1
            self._build_floor()

    def _draw(self):
        self._screen.blit(self._background, (0, 0))
        for x in range(self.floor.width):
            for y in range(self.floor.height):
                element = self.floor.get(Coord(x, y))
                image = element.get_tile()

                tilesize = self._settings.tile_size()
                self._screen.blit(image, (x * tilesize, y * tilesize))

        self.hud.draw()
        pg.display.flip()

    def _events(self):
        "Handles events. Returns whether an update should happen"
        res = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.TEXTINPUT:
                text = event.text
                if text in Game._actions:
                    Game._actions[text](self.hero, self)
                    res = True
                elif text in Game._actions_no_update:
                    Game._actions_no_update[text](self.hero, self)
            if event.type == pg.KEYDOWN and event.unicode.isdigit():
                res = self._use_item(int(event.unicode) - 1)

            Music.update(event)

        return res

    def _use_item(self, idx: int) -> bool:
        if idx >= len(self.hero.inventory):
            Sounds.play("Denied")
            return False

        item = self.hero.inventory[idx]
        self.hero.use(item, self.floor)
        return True
