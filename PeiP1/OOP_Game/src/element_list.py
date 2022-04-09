import random
from typing import Dict, List

from constants import MAX_INVENTORY
from coord import Coord
from creature import Creature, Ghost
from equipment import (Armor, Equipment, EquipmentType, Projectile, Usable,
                       Weapon)
from map import Map
from meet import MeetAction, meet
from sounds import Sounds


def _heal(val: int):
    def ret(e: Equipment, c: Creature, m: Map):
        c.heal(val)

    return ret


def _teleport(creature: Creature, unique: bool, map: Map):
    target = map.rand_empty_coord(random.choice(map.rooms))
    orig = map.pos(creature)
    delta = target - orig
    map.move(creature, delta)
    return unique


def _ranged_weapon_usage(damage: int):
    """
    Returns a function that puts the projectile on the map.
    This design is not ideal. Ideally, we should not have knowledge of Map
    """
    def usage(e: Equipment, creature: Creature, map: Map):
        pos = map.pos(creature) + creature.direction
        proj = Projectile("Arrow", damage, Coord())

        proj.direction = creature.direction
        if map.is_empty(pos):
            map.put(pos, proj)
        else:
            el = map.get(pos)
            if isinstance(el, Creature) and meet(
                    el, proj) == MeetAction.DELETE_SELF:
                map.rm(pos)
        return False

    return usage


def _make_creature(name: str, hp: int, strength: int = 1):
    return Creature(name, MAX_INVENTORY, hp, strength)


class ElementList:
    def __init__(self):
        self._init_equipment()
        self._init_creatures()

    def _init_equipment(self):
        self.gold = Equipment("Gold", None, EquipmentType.GOLD)

        self.health_potions: List[Usable] = []
        for i in range(1, 4):
            self.health_potions.append(
                Usable(f"HealthPotion{i}", Sounds.get("DrinkHealthPotion"),
                       _heal(i * 3)))

        self.swords: List[Weapon] = []
        self.bows: List[Usable] = []
        for i in range(1, 6):
            self.swords.append(
                Weapon(f"Sword{i}", Sounds.get("SwordSlash"), i, 10))

            self.bows.append(
                Usable(f"Bow{i}", Sounds.get("BowShot"),
                       _ranged_weapon_usage(i), 3))

        self.helmets: List[Armor] = []
        for i in range(1, 8):
            self.helmets.append(Armor(f"Helmet{i}", None, i))

        self.teleport_potion = Usable(
            "TeleportPotion",
            Sounds.get("Teleport"),
            usage=lambda _e, user, map: _teleport(user, True, map))

        self.portoloin = Usable(
            "Portoloin",
            Sounds.get("Teleport"),
            usage=lambda _e, user, map: _teleport(user, False, map),
            solidity=5)

        self.equipments = {
            0: [self.health_potions[0], self.gold, self.swords[0]],
            1: [self.helmets[0], self.bows[0]],
            2: [self.teleport_potion, self.swords[1]],
            3: [self.helmets[1], self.bows[1]],
            4: [self.health_potions[1], self.swords[2]],
            5: [self.helmets[2], self.bows[2]],
            6: [self.health_potions[1], self.swords[3]],
            7: [self.portoloin, self.helmets[3], self.bows[3]],
            8: [self.health_potions[2], self.swords[4]],
            9: [self.helmets[4], self.bows[4]],
            10: [self.health_potions[2], self.swords[4]],
            11: [self.helmets[5], self.bows[4]],
            13: [self.helmets[6]],
        }

    def _init_creatures(self):
        self.bat = _make_creature("Bat", 2)
        self.skeleton = _make_creature("Skeleton", 4)

        self.pumpkin = _make_creature("Pumpkin", 6, strength=2)
        self.blob = _make_creature("Blob", 10)

        self.ghost = Ghost(MAX_INVENTORY, 1, 5)
        self.ork = _make_creature("Ork", 10, strength=3)

        self.dark_skeleton = _make_creature("DarkSkeleton", 8, 2)
        self.dark_blob = _make_creature("DarkBlob", 30)

        self.invader = _make_creature("Invader", 15, strength=3)
        self.mummy = _make_creature("Mummy", 20, strength=3)

        self.ork_king = _make_creature("KingOrk", 30, strength=5)
        self.thing = _make_creature("Thing", 50, strength=3)

        self.monsters: Dict[int, List[Creature]] = {
            0: [self.skeleton, self.bat],
            2: [self.pumpkin, self.blob],
            4: [self.ghost, self.ork],
            6: [self.dark_skeleton, self.dark_blob],
            8: [self.invader, self.mummy],
            10: [self.ork_king, self.thing]
        }
