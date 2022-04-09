from __future__ import annotations

from typing import Any, Optional

from pygame.surface import Surface

from coord import Coord
from element import Element
from equipment import Equipment, Usable
from inventory import Inventory
from sounds import Sounds


class Creature(Element):
    def __init__(self,
                 name: str,
                 inventory_size: Optional[int],
                 hp: int,
                 strength: int = 1):
        super().__init__(name)
        self.inventory = Inventory(inventory_size)
        self.hp: int = hp
        self.max_hp = hp
        self._strength = strength
        self.direction = Coord(0, 1)

    def take_damage(self, count: int):
        self.hp = max(self.hp - count, 0)

    def heal(self, count: int):
        self.hp = min(self.hp + count, self.max_hp)

    def give_damage(self):
        return self._strength

    def xp_given(self):
        return self.max_hp * self._strength

    def copy(self):
        return Creature(self.name, self.inventory.max_size, self.hp,
                        self._strength)

    def get_tile(self) -> Surface:
        return self.texture.get_tile(self.direction)


class Ghost(Creature):
    def __init__(self,
                 inventory_size: Optional[int],
                 hp: int,
                 strength: int = 1):
        # Camouflage as ground
        super().__init__("Ground", inventory_size, hp, strength)

    def take_damage(self, count: int):
        self.hp -= count
        self.make_visible()
        Sounds.get("GhostDamaged").play()

    def give_damage(self):
        self.make_visible()
        return super().give_damage()

    def make_visible(self):
        self.name = "Ghost"
        self.reload_texture()

    def copy(self):
        g = Ghost(self.inventory.max_size, self.hp, self._strength)
        g.name = self.name
        g.reload_texture()
        return g


class Hero(Creature):
    def __init__(self,
                 inventory_size: Optional[int],
                 name: str = "Hero",
                 hp: int = 10,
                 strength: int = 2):
        super().__init__(name, inventory_size, hp, strength)
        self.xp = 0
        self.level = 1

    def take(self, item: Equipment):
        res = self.inventory.add(item)
        if not res:
            Sounds.play("Denied")
        return res

    def take_damage(self, count: int):
        super().take_damage(count)
        Sounds.get("HeroHit").play()

    def use(self, item: Equipment, map: Any):
        if item not in self.inventory:
            raise ValueError("Item not in inventory")

        if item.is_equipable():
            self.inventory.equip(item)
        elif isinstance(item, Usable):
            item.use(self, map)
            if item.deteriorate():
                self.inventory.remove(item)

    def add_xp(self, other: Creature):
        self.xp += other.xp_given()
        if self.xp > self.level**3 + 25:
            self.xp = 0
            self.level += 1
            self._strength += 1
            self.max_hp += 1
            self.hp = self.max_hp
            Sounds.get("LevelUp").play()

    def copy(self):
        return Hero(self.inventory.max_size, self.name, self.hp,
                    self._strength)
