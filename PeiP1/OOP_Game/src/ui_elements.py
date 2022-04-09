"""
Contains UI elements, such as Button
I suggest not looking at the code too much. It is quite ugly
Not that bad, but hard to read because it's more coordinates than programming
"""
import abc
from typing import Any, List, Tuple

import pygame as pg
from pygame.surface import Surface

from textures import Textures
from util import render_text, scaled

Pos = Tuple[int, int]


class UiElement(abc.ABC):
    @abc.abstractmethod
    def display(self, surface: Surface, mouse_pos: Pos) -> None:
        pass

    @abc.abstractmethod
    def scale(self, scale: float) -> None:
        pass

    @abc.abstractmethod
    def set_midtop(self, pos: Pos) -> None:
        pass

    @abc.abstractmethod
    def get_width(self) -> int:
        pass

    @abc.abstractmethod
    def get_height(self) -> int:
        pass


class Button(UiElement):
    DEFAULT_FONT_SIZE = 250
    TEXT_COLOR = pg.Color(234, 234, 234)

    def __init__(self, text: str, pos: Pos, scale: float = 1.0):
        self._init(scale, text, pos)

    def _init(self, scale: float, text: str, pos: Pos):
        self.normal = scaled(Textures.get("btn_normal").get_ui(), scale)
        self.hover = scaled(Textures.get("btn_hover").get_ui(), scale)

        self.width = self.normal.get_width()
        self.height = self.normal.get_height()

        self.font_size = round(Button.DEFAULT_FONT_SIZE * scale)

        self.text = text
        self.text_surface, self.text_rect = render_text(
            text, self.font_size, Button.TEXT_COLOR)

        self.rect = pg.Rect(*pos, self.width, self.height)
        w = int(pos[0] + self.width / 2 - self.text_rect.width / 2)
        h = int(pos[1] + self.height / 2 - self.text_rect.height / 2)

        self.text_rect.topleft = w, h

        self._scale = scale

    def display(self, surface: Surface, mouse_pos: Pos):
        texture = self.hover if self.collides(mouse_pos) else self.normal

        surface.blit(texture, self.rect)
        surface.blit(self.text_surface, self.text_rect)

    def collides(self, pos: Pos) -> bool:
        return bool(self.rect.collidepoint(pos))

    def scale(self, scale: float):
        self._init(scale, self.text, self.rect.topleft)

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def set_midtop(self, pos: Pos):
        pos = pos[0] - self.get_width() // 2, pos[1]
        self._init(self._scale, self.text, pos)


class SwitchButton(UiElement):
    DEFAULT_FONT_SIZE = 300
    TEXT_COLOR = pg.Color(234, 234, 234)

    def __init__(self,
                 caption: str,
                 values: List[Any],
                 pos: Pos,
                 scale: float = 1.0):
        self._init_all(scale, caption, values, pos)
        self.index = 0

    def _init_all(self, scale: float, caption: str, texts: List[Any],
                  pos: Pos):
        self._scale = scale
        self._init_tex(caption)
        self._init_rect(pos)
        self._init_text(texts, pos)

    def _init_tex(self, caption_txt: str):
        self.caption = caption_txt

        self.left = scaled(Textures.get("left_arrow").get_ui(), self._scale)
        self.right = scaled(Textures.get("right_arrow").get_ui(), self._scale)

        normal = scaled(Textures.get("switch_btn").get_ui(), self._scale)
        txsize = round(SwitchButton.DEFAULT_FONT_SIZE * self._scale)
        caption, text_rect = render_text(caption_txt, txsize,
                                         SwitchButton.TEXT_COLOR)
        text_rect.midtop = (normal.get_width() // 2, 0)

        self.normal = Surface(
            (normal.get_width(), text_rect.height + normal.get_height()),
            pg.SRCALPHA)
        self.normal.convert_alpha()

        self.normal.blit(caption, text_rect)

        normal_rect = pg.Rect(0, text_rect.height, normal.get_width(),
                              normal.get_height())
        self.normal.blit(normal, normal_rect)

        lw = self.left.get_width()
        mw = self.normal.get_width()
        rw = self.right.get_width()
        self.width = lw + mw + rw
        self.height = self.normal.get_height()

    def _init_text(self, values: List[Any], pos: Pos):
        self.font_size = round(SwitchButton.DEFAULT_FONT_SIZE * self._scale)

        first_text, self.text_rect = render_text(str(values[0]),
                                                 self.font_size,
                                                 SwitchButton.TEXT_COLOR)

        self.values = values
        self.texts: List[Surface] = [first_text]
        for text in values[1:]:  # First one already processed
            render = render_text(str(text), self.font_size,
                                 pg.Color(234, 234, 234))[0]
            self.texts.append(render)

        w = round(pos[0] + self.width / 2)
        h = round(pos[1] + self.height / 2)

        self.text_rect.center = w, h

    def _init_rect(self, pos: Pos):
        # Middle left
        pos = pos[0], pos[1] + self.normal.get_height() // 2

        self.left_rect = pg.Rect(*pos, self.left.get_width(),
                                 self.left.get_height())
        self.left_rect.midleft = pos

        pos = pos[0] + self.left.get_width(), pos[1]

        self.normal_rect = pg.Rect(*pos, self.normal.get_width(),
                                   self.normal.get_height())
        self.normal_rect.midleft = pos

        pos = pos[0] + self.normal.get_width(), pos[1]

        self.right_rect = pg.Rect(*pos, self.left.get_width(),
                                  self.left.get_height())
        self.right_rect.midleft = pos

    def display(self, surface: Surface, mouse_pos: Pos):
        surface.blit(self.left, self.left_rect)
        surface.blit(self.normal, self.normal_rect)
        surface.blit(self.right, self.right_rect)

        surface.blit(self.texts[self.index], self.text_rect)

    def handle_buttons(self, pos: Pos):
        if self.left_rect.collidepoint(pos):
            self.index = (self.index - 1) % len(self.texts)

        elif self.right_rect.collidepoint(pos):
            self.index = (self.index + 1) % len(self.texts)

    def get_selected(self) -> Any:
        return self.values[self.index]

    def set_selected(self, value: Any):
        if value in self.values:
            self.index = self.values.index(value)

    def scale(self, scale: float):
        self._init_all(scale, self.caption, self.values,
                       self.left_rect.topleft)

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def set_midtop(self, pos: Pos):
        # Convert to left top
        pos = pos[0] - self.get_width() // 2, pos[1]
        self._init_all(self._scale, self.caption, self.values, pos)


def layout(surface: Surface, elements: List[UiElement]):
    """Resizes and moves UI elements vertically"""
    height = surface.get_height()

    start_h = round(height * 0.1)
    end_h = round(height * 0.9)
    available_height = end_h - start_h

    for e in elements:
        e.scale(1.0)  # So that scale calculation is correct

    total_height = sum(e.get_height() for e in elements)

    # Leave some space between the elements
    scale = 0.8 * available_height / total_height

    for e in elements:
        e.scale(scale)

    total_height = sum(e.get_height() for e in elements)
    average_height = total_height // len(elements)

    pos = surface.get_width() // 2, start_h
    for e in elements:
        e.set_midtop(pos)
        pos = pos[0], round(pos[1] + average_height * 1.1)


# class Splash(tools._State):
#     """This State is updated while our game shows the splash screen."""
#     def __init__(self):
#         tools._State.__init__(self)
#         self.next = "INTRO"
#         self.timeout = 5
#         self.cover = pg.Surface((prepare.SCREEN_SIZE)).convert()
#         self.cover.fill(0)
#         self.cover_alpha = 256
#         self.alpha_step = 2
#         self.image = prepare.GFX['splash1']
#         self.rect = self.image.get_rect(center=prepare.SCREEN_RECT.center)

#     def update(self, surface, keys, current_time, time_delta):
#         """Updates the splash screen."""
#         self.current_time = current_time
#         surface.blit(self.image, self.rect)
#         self.cover.set_alpha(self.cover_alpha)
#         self.cover_alpha = max(self.cover_alpha - self.alpha_step, 0)
#         surface.blit(self.cover, (0, 0))
#         if self.current_time - self.start_time > 1000.0 * self.timeout:
#             self.done = True

#     def get_event(self, event):
#         """Get events from Control. Currently changes to next state on any key
#         press."""
#         if event.type == pg.KEYDOWN:
#             self.done = True
