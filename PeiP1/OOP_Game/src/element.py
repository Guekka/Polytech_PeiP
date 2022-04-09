from __future__ import annotations

from abc import ABC, abstractmethod

from pygame.surface import Surface

from coord import Coord
from textures import Textures


class Element(ABC):
    def __init__(self, nom: str):
        self.name = nom
        self.reload_texture()

    @abstractmethod
    def copy(self) -> Element:
        pass

    def get_tile(self) -> Surface:
        return self.texture.get_tile(Coord(0, 0))

    def reload_texture(self):
        self.texture = Textures.get(self.name)


class Tile(Element):
    def copy(self):
        return Tile(self.name)
