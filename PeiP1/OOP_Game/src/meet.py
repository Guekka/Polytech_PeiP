"""
The meet() free function
Since meet() needs knowledge about all the classes, it is put in its own file
to reduce coupling.
"""

from __future__ import annotations

from enum import Enum

from creature import Creature, Ghost, Hero
from element import Element, Tile
from equipment import Equipment, Projectile
from stairs import Stairs


class MeetAction(Enum):
    NONE = 0
    DELETE_SELF = 1
    DELETE_OTHER = 2
    STAIRS = 3


def _meet_tile_element(self: Tile, other: Element) -> MeetAction:
    if isinstance(other, Projectile):
        return MeetAction.DELETE_OTHER
    return MeetAction.NONE


def _meet_creature_element(self: Creature, other: Element) -> MeetAction:
    if isinstance(other, Projectile):
        self.take_damage(other._damage)
        if self.hp > 0:
            return MeetAction.DELETE_OTHER
        return MeetAction.DELETE_SELF

    if not isinstance(other, Creature):
        return MeetAction.NONE

    if isinstance(other, Ghost):
        other.make_visible()

    damage = other.give_damage()

    for item in [other.inventory.weapon, self.inventory.armor]:
        if not item:
            continue

        damage = item.change_damage(damage)

        if item._sound:
            item._sound.play()

        if item.deteriorate():
            inv = self.inventory if item is self.inventory.armor else other.inventory
            inv.remove(item)

    self.take_damage(damage)

    if self.hp > 0:
        return MeetAction.NONE

    if isinstance(other, Hero):
        other.add_xp(self)

    return MeetAction.DELETE_SELF


def _meet_equipment_element(self: Equipment, other: Element) -> MeetAction:
    if not isinstance(other, Hero):
        return MeetAction.NONE

    if other.take(self):
        return MeetAction.DELETE_SELF
    return MeetAction.NONE


def _meet_projectile_element(self: Projectile, other: Element) -> MeetAction:
    return MeetAction.DELETE_SELF


def _meet_stairs_element(self: Stairs, other: Element) -> MeetAction:
    return MeetAction.STAIRS


# Couldn't Python add overloads?
def meet(self: Element, other: Element) -> MeetAction:
    if isinstance(self, Tile):
        return _meet_tile_element(self, other)
    if isinstance(self, Creature):
        return _meet_creature_element(self, other)
    if isinstance(self, Projectile):
        return _meet_projectile_element(self, other)
    if isinstance(self, Equipment):
        return _meet_equipment_element(self, other)
    if isinstance(self, Stairs):
        return _meet_stairs_element(self, other)

    raise NotImplementedError
