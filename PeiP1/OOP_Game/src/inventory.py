from __future__ import annotations

from typing import List, Optional

from equipment import Armor, Equipment, EquipmentType, Weapon


class Inventory:
    def __init__(self, max_size: Optional[int] = None):
        self.gold = 0
        self.armor: Optional[Armor] = None
        self.weapon: Optional[Weapon] = None
        self.all: List[Equipment] = []
        self.max_size: Optional[int] = max_size

    def __contains__(self, item: Equipment):
        return item in self.all

    def __len__(self):
        return len(self.all)

    def __iter__(self):
        return iter(self.all)

    def __getitem__(self, idx: int):
        return self.all[idx]

    def equip(self, item: Equipment):
        if isinstance(item, Armor):
            if item is self.armor:
                self.armor = None
            else:
                self.armor = item

        if isinstance(item, Weapon):
            if item is self.weapon:
                self.weapon = None
            else:
                self.weapon = item

    def add(self, item: Equipment):
        if item.type == EquipmentType.GOLD:
            self.gold += 1
            return True

        # Combine solidity if same item already in inventory
        for it in self.all:
            if it.name == item.name:
                it.add_solidity(item.get_solidity())
                return True

        if self.max_size and len(self.all) >= self.max_size:
            return False

        for i in range(len(self.all)):
            eq_type = self.all[i].type
            if item.type.value <= eq_type.value:
                self.all.insert(i, item)
                return True

        # If we are here, the inventory was empty
        self.all.append(item)
        return True

    def remove(self, item: Equipment):
        self.all.remove(item)
        if item is self.armor:
            self.armor = None
        if item is self.weapon:
            self.weapon = None

    def destroy_equipped(self):
        for x in [self.armor, self.weapon]:
            if x:
                self.remove(x)
