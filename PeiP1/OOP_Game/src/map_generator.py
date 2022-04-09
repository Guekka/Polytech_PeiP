import random
from typing import List

from coord import Coord
from element_manager import ElementManager
from map import Map
from room import Room


class MapGenerator:
    """
    Generates a map
    Has the same functions as the map we wrote in class
    """
    def __init__(self, map: Map):
        self.map = map
        self._roomsToReach: List[Room] = []

    def generate(self, nbrooms: int, el_manager: ElementManager):
        self._generate_rooms(nbrooms)
        self._reach_all_rooms()

        start = self.map.rooms[0].center()
        self.map.put(start, self.map.hero)

        for r in self.map.rooms:
            self._decorate(r, el_manager)

    def _add_room(self, room: Room):
        self._roomsToReach.append(room)
        for x in range(room.c1.x, room.c2.x + 1):
            for y in range(room.c1.y, room.c2.y + 1):
                self.map.set(Coord(x, y), Map.ground)

    def _find_room(self, coord: Coord):
        for r in self._roomsToReach:
            if coord in r:
                return r
        return False

    def _intersect_none(self, room: Room):
        return not any(room.intersect(r) for r in self._roomsToReach)

    def _is_not_border(self, room: Room):
        avoid_x = (0, self.map.width - 1)
        avoid_y = (0, self.map.height - 1)
        return not any(x in avoid_x or y in avoid_y
                       for x, y in [room.c1, room.c2])

    def _dig(self, coord: Coord):
        self.map.set(coord, Map.ground)
        r = self._find_room(coord)
        if r:
            self._roomsToReach.remove(r)
            self.map.rooms.append(r)

    def _corridor(self, start: Coord, end: Coord):
        starty = min(start.y, end.y)
        startx = min(start.x, end.x)
        endy = max(start.y, end.y)
        endx = max(start.x, end.x)

        for y in range(starty, endy + 1):
            self._dig(Coord(start.x, y))

        for x in range(startx, endx + 1):
            self._dig(Coord(x, end.y))

    def _reach(self):
        start = random.choice(self.map.rooms).center()
        end = random.choice(self._roomsToReach).center()

        self._corridor(start, end)

    def _reach_all_rooms(self):
        assert self._roomsToReach
        self.map.rooms.append(self._roomsToReach.pop(0))
        while self._roomsToReach:
            self._reach()

    def _rand_room(self):
        x1 = random.randint(0, self.map.width - 3)
        y1 = random.randint(0, self.map.height - 3)

        largeur = random.randint(3, 8)
        hauteur = random.randint(3, 8)

        x2 = min((self.map.width - 1), (x1 + largeur))
        y2 = min((self.map.height - 1), (y1 + hauteur))

        return Room(Coord(x1, y1), Coord(x2, y2))

    def _generate_rooms(self, n: int):
        counter = 0
        while len(self._roomsToReach) < n and counter < n * 100:
            counter += 1
            room = self._rand_room()
            if self._intersect_none(room) and self._is_not_border(room):
                self._add_room(room)

    def _decorate(self, room: Room, manager: ElementManager):
        pos_one = self.map.rand_empty_coord(room)
        equip = manager.rand_equipment()
        self.map.put(pos_one, equip)

        pos_two = self.map.rand_empty_coord(room)
        monster = manager.rand_monster()
        self.map.put(pos_two, monster)
