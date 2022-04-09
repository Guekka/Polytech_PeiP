from math import floor, gcd, sqrt
from time import sleep
from typing import cast

from constants import (BASE_HUD_HEIGHT, BASE_HUD_WIDTH, DEFAULT_TILECOUNT,
                       HUD_RATIO)


def lcm(a: int, b: int):
    return abs(a * b) // gcd(a, b)


class Settings:
    def __init__(self,
                 scr_width: int,
                 scr_height: int,
                 room_count: int,
                 tilecount: int = DEFAULT_TILECOUNT):
        self._init(scr_width, scr_height, room_count, tilecount)

    def _init_hud_size(self, scr_width: int, scr_height: int):
        ratio = scr_height / scr_width
        self._hud_height = round(scr_height * HUD_RATIO / ratio)
        self._hud_scale = self._hud_height / BASE_HUD_HEIGHT

        self._width = scr_width
        self._game_height = scr_height - self._hud_height

        awidth = round(self._hud_scale * BASE_HUD_WIDTH)
        self._action_bar_size = (awidth, self._hud_height)

    def _init_tile_count(self, game_height: int, game_width: int,
                         tilecount: int):
        # Sometimes it is impossible to get perfect tilecount
        def okay(x_count: float, y_count: float):
            count = x_count * y_count
            diff = tilecount - count
            return abs(diff) < 0.1 * tilecount

        x_count = game_width
        y_count = game_height
        while not okay(x_count, y_count):
            x_count *= 0.95
            y_count *= 0.95

        self._x_tile_count = floor(x_count)
        self._y_tile_count = floor(y_count)
        self._tilesize = game_width // self._x_tile_count

    def _init(self, scr_width: int, scr_height: int, room_count: int,
              tilecount: int):
        self.room_count = room_count
        self._init_hud_size(scr_width, scr_height)

        # Algorithm will fail otherwise
        assert tilecount >= 200

        self._init_tile_count(self._game_height, self._width, tilecount)

    def tile_size(self):
        return self._tilesize

    def x_tile_count(self):
        return self._x_tile_count

    def y_tile_count(self):
        return self._y_tile_count

    def width(self):
        return self._width

    def height(self):
        return self.game_height() + self.hud_height()

    def game_height(self):
        return self._game_height

    def hud_scale(self):
        return self._hud_scale

    def hud_width(self):
        return self._width

    def hud_height(self):
        return self._hud_height

    def action_bar_size(self):
        return self._action_bar_size

    def ui_square_size(self):
        return round(109.4 * self.hud_scale())

    def set_tilecount(self, val: int):
        self._init(self.width(), self.height(), self.room_count, val)
