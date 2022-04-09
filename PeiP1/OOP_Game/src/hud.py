"Displays the player state"

import pygame as pg
from pygame.freetype import SysFont
from pygame.surface import Surface

from constants import MAX_INVENTORY
from creature import Hero
from settings import Settings
from textures import Textures

ACTION_BAR_BACKGROUND = (106, 86, 74)


class HUD:
    """
    Renders the player HUD (inventory)
    """
    def __init__(self, surface: Surface, hero: Hero, sets: Settings):
        self._surface = surface
        self._hero = hero

        self._scale = sets.hud_scale()
        self._height = sets.hud_height()
        self._square_size = sets.ui_square_size()
        self._gamesize = sets.width()

        action_bar = Textures.get("Action_Bar").get_ui()
        self._action_bar = pg.transform.scale(action_bar,
                                              sets.action_bar_size())

        self._action_bar_x = (surface.get_width() -
                              self._action_bar.get_width()) // 2

        self._action_bar_y = (surface.get_height() -
                              self._action_bar.get_height()) // 2

        self._action_bar_start_x = self._action_bar_x + int(131 * self._scale)
        self._action_bar_start_y = self._action_bar_y + int(54 * self._scale)

        self._action_bar_delta_x = round(17.5 * self._scale)

    def _item_pos(self, idx: int):
        x = self._action_bar_start_x
        y = self._action_bar_start_y

        x_delta = self._action_bar_delta_x + self._square_size

        return (x + x_delta * idx, y)

    def _annotate_item(self, surface: Surface, idx: int, text: str):
        font = SysFont('Comic Sans MS', int(45 * self._scale))
        size = font.get_rect(text)

        x, y = self._item_pos(idx)
        x += self._square_size - size.width
        y += self._square_size - size.height

        font.render_to(surface, (x, y),
                       text,
                       bgcolor=ACTION_BAR_BACKGROUND,
                       fgcolor=(255, 255, 255))

    def _draw_gold(self, surface: Surface, hero: Hero):
        delta = self._action_bar_delta_x + self._square_size
        x = self._action_bar_start_x + (delta * MAX_INVENTORY + 1)
        tex = Textures.get("Gold").get_ui()

        dest = pg.Rect(x, self._action_bar_start_y, self._square_size,
                       self._square_size)

        surface.blit(tex, dest)

        self._annotate_item(surface, MAX_INVENTORY, str(hero.inventory.gold))

    def _draw_inventory(self, surface: Surface, hero: Hero):
        surface.fill(ACTION_BAR_BACKGROUND)
        surface.blit(self._action_bar,
                     (self._action_bar_x, self._action_bar_y))

        for idx, item in enumerate(hero.inventory):
            tex = item.texture.get_ui()

            x, y = self._item_pos(idx)
            dest = pg.Rect(x, y, self._square_size, self._square_size)

            surface.blit(tex, dest)

            # Rectangle around item to show it is equipped
            if item in [hero.inventory.weapon, hero.inventory.armor]:
                pg.draw.rect(surface,
                             rect=dest,
                             color=(150, 150, 150),
                             width=2)

            self._annotate_item(surface, idx, str(item.get_solidity()))

        # Last slot is reserved for coin
        self._draw_gold(surface, hero)

    def _draw_hp(self, surface: Surface, hero: Hero):
        pos = (self._height // 20, self._gamesize // 100)
        width = self._height * 0.9 - pos[0]
        height = self._gamesize // 40 - pos[1]
        rect = pg.Rect(pos, (width, height))
        empty_color = (100, 100, 100)

        pg.draw.rect(surface, empty_color, rect)

        percent = hero.hp / hero.max_hp
        full_color = (255, 0, 0)

        rect = pg.Rect(pos, (percent * width, height))
        pg.draw.rect(surface, full_color, rect)

    def draw(self):
        self._draw_inventory(self._surface, self._hero)
        self._draw_hp(self._surface, self._hero)
