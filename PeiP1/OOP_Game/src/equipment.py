from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, Any, Callable, Optional

from pygame.mixer import Sound
from pygame.surface import Surface

from coord import Coord
from element import Element

if TYPE_CHECKING:  # Avoid circular import
    from creature import Creature
    from map import Map

    UsageCallback = Optional[Callable[['Equipment', Creature, Map], Any]]
else:
    UsageCallback = Optional[Callable[[Any, Any, Any], Any]]


class EquipmentType(Enum):
    "Type sorted by inventory priority"
    WEAPON = 1
    USABLE = 2
    POTION = 3
    ARMOR = 4
    GOLD = 5


class Equipment(Element):
    def __init__(self,
                 name: str,
                 sound: Optional[Sound],
                 eq_type: EquipmentType,
                 solidity: int = 10):
        super().__init__(name)
        self.type = eq_type
        self._sound = sound
        self._solidity = solidity

    def copy(self):
        return Equipment(self.name, self._sound, self.type, self._solidity)

    def get_solidity(self):
        return self._solidity

    def add_solidity(self, val: int):
        self._solidity += val

    def is_equipable(self):
        return self.type in [EquipmentType.WEAPON, EquipmentType.ARMOR]

    def deteriorate(self):
        self._solidity -= 1
        return self._solidity <= 0


class Weapon(Equipment):
    def __init__(self,
                 name: str,
                 sound: Optional[Sound],
                 damage: int,
                 solidity: int = 10):
        super().__init__(name, sound, EquipmentType.WEAPON, solidity)
        self._damage = damage

    def copy(self):
        return Weapon(self.name, self._sound, self._damage, self._solidity)

    def change_damage(self, damage: int):
        return damage + self._damage


class Projectile(Equipment):
    def __init__(self, name: str, damage: int, direction: Coord):
        super().__init__(name, None, EquipmentType.WEAPON, 1)
        self._damage = damage
        self.direction = direction

    def copy(self):
        return Projectile(self.name, self._damage, self.direction)

    def get_tile(self) -> Surface:
        return self.texture.get_tile(self.direction)


class Armor(Equipment):
    def __init__(
        self,
        name: str,
        sound: Optional[Sound],
        protection: int,
        solidity: int = 10,
    ):
        super().__init__(name, sound, EquipmentType.ARMOR, solidity)
        self.name = name
        self._protection = protection

    def copy(self):
        return Armor(self.name, self._sound, self._protection, self._solidity)

    def change_damage(self, damage: int):
        return max(0, damage - self._protection)


class Usable(Equipment):
    def __init__(self,
                 name: str,
                 sound: Optional[Sound],
                 usage: UsageCallback,
                 solidity: int = 1):
        super().__init__(name, sound, EquipmentType.USABLE, solidity)
        self._usage = usage

    def use(self, creature: Creature, map: Any):
        if not self._usage:
            return False

        if self._sound:
            self._sound.play()

        self._usage(self, creature, map)

    def copy(self):
        return Usable(self.name, self._sound, self._usage, self._solidity)
