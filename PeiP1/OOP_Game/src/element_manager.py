from __future__ import annotations

import random
from typing import Mapping, Sequence

from element import Element
from element_list import ElementList


def rand_element(collection: Mapping[int, Sequence[Element]],
                 level: int) -> Element:
    x = random.expovariate(1 / level)
    i = max(k for k in collection if k <= x)
    return random.choice(collection[i]).copy()


class ElementManager:
    def __init__(self, element_list: ElementList, level: int):
        self.level = level
        self._element_list = element_list

    def rand_equipment(self):
        return rand_element(self._element_list.equipments, self.level)

    def rand_monster(self):
        return rand_element(self._element_list.monsters, self.level)
