import os
from typing import Any, Callable, Dict, List

from constants import DATA_DIR
from texture_util import (Sprite, Texture, load_sprite, load_spritesheet,
                          load_ui)

TexturesDict = Dict[str, List[str]]

_SPRITESHEET128 = {
    "Sheet128": [
        "Arrow", "Blob", "DarkBlob", "Hero", "KingOrk", "Ork", "Skeleton",
        "Bat", "DarkSkeleton", "Ghost", "Invader", "Mummy", "Pumpkin", "Thing"
    ]
}

_SINGLE = {
    "Armor": [
        "Helmet1", "Helmet2", "Helmet3", "Helmet4", "Helmet5", "Helmet6",
        "Helmet7"
    ],
    "Single": [
        "Gold", "HealthPotion1", "HealthPotion2", "HealthPotion3", "Portoloin",
        "Stairs", "TeleportPotion"
    ],
    "Weapon": [
        "Bow1", "Bow2", "Bow3", "Bow4", "Bow5", "Sword1", "Sword2", "Sword3",
        "Sword4", "Sword5"
    ],
    "Tiles": ["Empty", "Ground"]
}

_UI = {
    "UI": [
        "Action_Bar", "btn_hover", "btn_normal", "left_arrow", "right_arrow",
        "switch_btn"
    ]
}


class Textures:
    """ Contains textures """
    _data: Dict[str, Texture] = {}

    @staticmethod
    def load(dic: TexturesDict, load_func: Callable[[str, int, int], Any],
             tilesize: int, square_size: int):
        for dir, files in dic.items():
            for file in files:
                path = os.path.join(DATA_DIR, dir, file) + ".png"
                tex = load_func(path, tilesize, square_size)
                Textures._data[file] = tex

    @staticmethod
    def get_all_textures() -> List[Texture]:
        return list(Textures._data.values())

    @staticmethod
    def get(name: str) -> Texture:
        return Textures._data[name]


def _load_textures(tilesize: int, square_size: int):
    def load128(file: str, tilesize: int, square_size: int):
        return load_spritesheet(file, 128, tilesize, square_size)

    Textures.load(_SPRITESHEET128, load128, tilesize, square_size)
    Textures.load(_SINGLE, load_sprite, tilesize, square_size)


def _load_ui_textures():
    def load(file: str, _: int, _2: int):
        sprite = Sprite()
        sprite.load_from_surface(load_ui(file))
        return Texture(sprite, sprite)

    Textures.load(_UI, load, 0, 0)


def init(tilesize: int, square_size: int):
    _load_textures(tilesize, square_size)
    _load_ui_textures()
