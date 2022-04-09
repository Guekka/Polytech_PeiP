import os
from typing import Tuple, cast

import pygame as pg
from pygame import Color
from pygame.freetype import Font
from pygame.rect import Rect
from pygame.surface import Surface

from constants import DATA_DIR

FONT_PATH = os.path.join(DATA_DIR, "Fonts", "HeartbitXX.ttf")


def render_text(text: str, font_size: int,
                color: Color) -> Tuple[Surface, Rect]:
    font = Font(FONT_PATH, font_size)
    return font.render(text, color)


def scaled(surface: Surface, scale: float):
    surface = surface.copy()
    size = tuple(map(lambda x: round(x * scale), surface.get_size()))
    size = cast(Tuple[int, int], size)
    return pg.transform.scale(surface, size)
