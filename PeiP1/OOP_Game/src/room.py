from __future__ import annotations

import random

from coord import Coord


class Room:
    def __init__(self, c1: Coord, c2: Coord):
        assert c2.x >= c1.x and c2.y >= c1.y
        self.c1 = c1
        self.c2 = c2

    def __contains__(self, c: Coord):
        return c.x in range(self.c1.x, self.c2.x + 1) and c.y in range(
            self.c1.y, self.c2.y + 1)

    def center(self):
        return Coord((self.c1.x + self.c2.x) // 2,
                     (self.c1.y + self.c2.y) // 2)

    def intersect(self, other: Room):
        """Test if the room has an intersection with another room"""
        dx = 1 if self.c1.x > self.c2.x else -1
        dy = 1 if self.c1.y > self.c2.y else -1

        for x in range(self.c1.x - 2 * dx, self.c2.x + 2 * dx, dx):
            for y in range(self.c1.y - 2 * dy, self.c2.y + 2 * dy, dy):
                if Coord(x, y) in other:
                    return True

        return False

    def rand_coord(self):
        x = random.randint(self.c1.x, self.c2.x)
        y = random.randint(self.c1.y, self.c2.y)
        return Coord(x, y)
