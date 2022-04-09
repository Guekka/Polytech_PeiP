from __future__ import annotations

import math


class Coord:
    "Coordonnées"

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __eq__(self, other: Coord):
        return self.x == other.x and self.y == other.y

    def __add__(self, other: Coord):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Coord):
        return Coord(self.x - other.x, self.y - other.y)

    def __iter__(self):
        return iter((self.x, self.y))

    # Careful with this. Usually, only immutable objects should be hashable
    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"<{self.x};{self.y}>"

    def distance(self, other: Coord):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

    def direction(self, other: Coord):
        diff = self - other
        dist = self.distance(other)
        if dist == 0:
            return Coord(0, 0)

        cos = diff.x / dist

        isqrt2 = 1 / math.sqrt(2)

        if cos > isqrt2:
            return Coord(-1, 0)
        if cos < -isqrt2:
            return Coord(1, 0)
        if diff.y > 0:
            return Coord(0, -1)

        return Coord(0, 1)
