from __future__ import annotations

import abc
from pathlib import Path
from typing import List

import pygame as pg
from pygame.surface import Surface

from constants import DATA_DIR
from coord import Coord


class AbstractSprite(abc.ABC):
    @abc.abstractmethod
    def get(self, line: int = 0) -> Surface:
        pass

    @abc.abstractmethod
    def scale(self, sprite_size: int) -> None:
        pass

    @abc.abstractmethod
    def copy(self) -> AbstractSprite:
        pass

    @abc.abstractmethod
    def load_from_surface(self, surface: Surface):
        pass


class SpriteSheet(AbstractSprite):
    "A sprite sheet containing several sprites"
    DEFAULT_COL = 0

    def __init__(self, sprite_size: int):
        self.sprite_size = sprite_size
        self._sheet: Surface
        self._data: List[List[Surface]]

    def load_from_surface(self, surface: Surface):
        self._sheet = surface
        self._data = self._split()

    def get(self, line: int = 0) -> Surface:
        return self._data[SpriteSheet.DEFAULT_COL][line]

    def scale(self, sprite_size: int):
        percent = sprite_size / self.sprite_size
        newwidth = round(percent * self._sheet.get_width())
        newheight = round(percent * self._sheet.get_height())
        newsize = (newwidth, newheight)
        self._sheet = pg.transform.scale(self._sheet, newsize)

        self.sprite_size = sprite_size
        self._data = self._split()

    def copy(self):
        s = SpriteSheet(self.sprite_size)
        s.load_from_surface(self._sheet.copy())
        return s

    def _split(self):
        """
        Parses images from the spritesheet
        Returns a list of subsurfaces
        """
        res: List[List[Surface]] = []

        ss = self.sprite_size
        for x in range(self._sheet.get_width() // self.sprite_size):
            res.append([])
            for y in range(self._sheet.get_height() // self.sprite_size):
                rect = pg.Rect(x * ss, y * ss, ss, ss)
                res[x].append(self._sheet.subsurface(rect))

        return res


class Sprite(AbstractSprite):
    "A single sprite"

    def __init__(self):
        """Loads the sprite."""
        self._sprite: Surface

    def load_from_surface(self, surface: Surface):
        self._sprite = surface

    def get(self, line: int = 0):  # line is unused
        return self._sprite

    def scale(self, sprite_size: int):
        self._sprite = pg.transform.scale(self._sprite,
                                          (sprite_size, sprite_size))

    def copy(self):
        s = Sprite()
        s.load_from_surface(self._sprite.copy())
        return s


def _get_load_path(path: str):
    return str((Path(DATA_DIR) / Path(path)).resolve())


def _load_helper(sprite: AbstractSprite, path: str, tilesize: int,
                 ui_square_size: int):
    try:
        path = _get_load_path(path)
        image = pg.image.load(path).convert_alpha()
        sprite.load_from_surface(image)
        return prepare_scaled_texture(sprite, tilesize, ui_square_size)
    except pg.error as err:
        raise SystemExit(f"Could not load image '{path}': {err}") from err


def load_sprite(path: str, tilesize: int, ui_square_size: int):
    return _load_helper(Sprite(), path, tilesize, ui_square_size)


def load_spritesheet(path: str, sprite_size: int, tilesize: int,
                     ui_square_size: int):
    sprite = SpriteSheet(sprite_size)
    return _load_helper(sprite, path, tilesize, ui_square_size)


def load_ui(path: str) -> Surface:
    try:
        path = _get_load_path(path)
        return pg.image.load(path).convert_alpha()
    except pg.error as err:
        raise SystemExit(f"Could not load image '{path}': {err}") from err


class Texture:
    "Handles texture"

    def __init__(self, tile: AbstractSprite, ui: AbstractSprite):
        self._tile = tile
        self._ui = ui

    def get_tile(self, dir: Coord = Coord(0, 0)):
        if isinstance(self._tile, Sprite):
            return self._tile.get()

        # Spritesheet are in this order: SQDZ
        dic = {
            Coord(0, 0): 0,  # Front when not moving
            Coord(0, -1): 3,  # Up
            Coord(-1, 0): 1,  # Left
            Coord(0, 1): 0,  # Down
            Coord(1, 0): 2  # Right
        }
        return self._tile.get(dic[dir])

    def get_ui(self):
        return self._ui.get()

    def copy(self):
        return Texture(self._tile, self._ui)


def prepare_scaled_texture(orig: AbstractSprite, tilesize: int,
                           ui_square_size: int):
    """
    Prepares two versions of the Sprite: one for tiles and for one action bar
    """
    tile = orig.copy()
    tile.scale(tilesize)
    ui = orig.copy()
    ui.scale(ui_square_size)

    return Texture(tile, ui)
