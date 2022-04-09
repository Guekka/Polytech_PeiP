import os
from random import shuffle
from typing import List

import pygame as pg

from constants import DATA_DIR

### Sounds


def load_sound(file: str) -> pg.mixer.Sound:
    file = os.path.join(DATA_DIR, file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error as e:
        raise SystemExit(f"Couldn't load {file}: {e} ") from e


_SOUNDS = [
    ("HeroHit", ".mp3"),
    ("SwordSlash", ".mp3"),
    ("Teleport", ".mp3"),
    ("DrinkHealthPotion", ".wav"),
    ("LevelUp", ".wav"),
    ("GhostDamaged", ".wav"),
    ("Denied", ".wav"),
    ("BowShot", ".wav"),
    ("Stairs", ".wav"),
]


class Sounds:
    @staticmethod
    def init():
        for name, ext in _SOUNDS:
            sound = load_sound(f"Sounds/{name}{ext}")
            setattr(Sounds, name, sound)

    @staticmethod
    def get(name: str):
        return getattr(Sounds, name)

    @staticmethod
    def play(name: str):
        Sounds.get(name).play()


### Music

_MUSICS = [os.path.join(DATA_DIR, f"Music/{i}.ogg") for i in range(9)]


class Music:
    idx = 0
    EVENT = 402  # Random unused

    @staticmethod
    def increment_idx():
        Music.idx = (Music.idx + 1) % len(_MUSICS)

    @staticmethod
    def init():
        shuffle(_MUSICS)
        pg.mixer.music.load(_MUSICS[Music.idx])
        Music.increment_idx()
        pg.mixer.music.queue(_MUSICS[Music.idx])
        Music.increment_idx()
        pg.mixer.music.set_endevent(Music.EVENT)
        pg.mixer.music.play()

    @staticmethod
    def update(event: pg.event.Event):
        if event.type == Music.EVENT:
            Music.increment_idx()
            pg.mixer.music.queue(_MUSICS[Music.idx])


def init():
    Sounds.init()
    Music.init()
