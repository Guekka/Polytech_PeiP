from __future__ import annotations

import random
from typing import Dict, List, Optional, Set, Union

from coord import Coord
from creature import Creature, Hero
from element import Element, Tile
from equipment import Projectile
from meet import MeetAction, meet
from room import Room
from stairs import Stairs


class Map:
    ground: Tile
    empty: Tile

    def __init__(self, width: int, height: int, hero: Hero):
        self._mat: List[List[Element]] = [[Map.empty for _ in range(width)]
                                          for _ in range(height)]

        self.width = width
        self.height = height

        self._elem: Dict[Element, Coord] = {}
        self.rooms: List[Room] = []
        self.hero = hero
        self.stairs_taken = False

    def __contains__(self, elem: Union[Element, Coord]):
        if isinstance(elem, Coord):
            return self.is_free_pos(elem)
        return elem in self._elem

    def __iter__(self):
        return iter(self._mat)

    def is_valid_pos(self, pos: Coord):
        return pos.x in range(self.width) and pos.y in range(self.height)

    def is_free_pos(self, pos: Coord):
        empty = self.get(pos) == Map.empty
        return not empty and self.is_valid_pos(pos)

    def rand_empty_coord(self, room: Room):
        coord = room.rand_coord()
        while self.get(coord) != Map.ground or coord == room.center():
            coord = room.rand_coord()
        return coord

    def check_coord(self, pos: Coord):
        if not self.is_valid_pos(pos):
            raise IndexError("Out of map coord")

    def get(self, pos: Coord) -> Element:
        self.check_coord(pos)
        return self._mat[pos.y][pos.x]

    def pos(self, e: Element):
        return self._elem[e]

    def set(self, pos: Coord, e: Tile):
        self.check_coord(pos)
        self._mat[pos.y][pos.x] = e

    def put(self, pos: Coord, e: Element):
        self.check_coord(pos)

        val = self._mat[pos.y][pos.x]
        if val != Map.ground:
            raise ValueError("Incorrect cell")

        for line in self._mat:
            for obj in line:
                if obj is e:
                    raise KeyError("Already placed")

        self._elem[e] = pos

        self._mat[pos.y][pos.x] = e

    def rm(self, pos: Coord):
        e = self.get(pos)
        del self._elem[e]
        self._mat[pos.y][pos.x] = Map.ground

    def is_empty(self, pos: Coord):
        return self.get(pos) == Map.ground

    def move(self, e: Element, way: Coord) -> Optional[Coord]:
        """Moves the element e in the direction way."""

        if way == Coord(0, 0):
            return None  # Do not move

        orig = self.pos(e)
        dest = orig + way

        if dest not in self or dest is Map.empty:
            return None

        dest_type = self.get(dest)

        if dest_type == Map.ground:
            self._mat[orig.y][orig.x] = Map.ground
            self._mat[dest.y][dest.x] = e
            self._elem[e] = dest
            return None

        meet_res = meet(dest_type, e)

        if meet_res == MeetAction.DELETE_SELF:
            return dest
        if meet_res == MeetAction.DELETE_OTHER:
            return orig
        if meet_res == MeetAction.STAIRS:
            self.stairs_taken = True

    def move_hero(self, h: Hero, way: Coord):
        h.direction = way
        e = self.move(h, way)
        if e:
            self.rm(e)

    def can_move(self, creature: Creature, way: Coord):
        pos = self.pos(creature) + way
        dest = self.get(pos)
        return dest == Map.ground or isinstance(dest, Hero)

    def move_all_monsters(self):
        hero_pos = self.pos(self.hero)

        to_remove: Set[Element] = set()
        for creature, pos in self._elem.items():
            if pos.distance(hero_pos) > 6:
                continue

            if not isinstance(creature, Creature):
                continue

            if isinstance(creature, Hero):
                continue

            # Very basic pathfinding
            directions = [
                pos.direction(hero_pos),
                Coord(0, -1),
                Coord(-1, 0),
                Coord(0, 1),
                Coord(1, 0)
            ]
            best = Coord(0, 0)
            for direction in directions:
                best_dist = (pos + best).distance(hero_pos)
                cur_dist = (pos + direction).distance(hero_pos)
                can_move = self.can_move(creature, direction)
                if can_move and cur_dist < best_dist:
                    best = direction
            creature.direction = best

            destroyed = self.move(creature, creature.direction)
            if destroyed:
                to_remove.add(self.get(destroyed))

        for c in to_remove:
            self.rm(self.pos(c))

    def move_projectiles(self):
        to_remove: List[Coord] = []
        for proj in self._elem:
            if not isinstance(proj, Projectile):
                continue

            for _ in range(4):  # Projectile velocity
                destroyed = self.move(proj, proj.direction)
                if destroyed and destroyed not in to_remove:
                    to_remove.append(destroyed)
                    break

        for c in to_remove:
            self.rm(c)

    def cleared(self):
        def pred(e: Element):
            return isinstance(e, Creature) and not isinstance(e, Hero)

        return not any(pred(e) for e in self._elem)

    def spawn_stairs(self):
        room = random.choice(self.rooms)
        pos = self.rand_empty_coord(room)
        self.put(pos, Stairs())


def init():
    setattr(Map, "ground", Tile("Ground"))
    setattr(Map, "empty", Tile("Empty"))
