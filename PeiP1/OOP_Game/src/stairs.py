from element import Element


class Stairs(Element):
    def __init__(self):
        super().__init__("Stairs")

    def copy(self):
        return Stairs()
