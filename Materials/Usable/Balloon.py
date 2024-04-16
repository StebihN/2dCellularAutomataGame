from Materials.Cell import Cell
from Materials.Usable.Water import Water


class Balloon(Cell):
    def __init__(self):
        super().__init__("balloon", "#219906")
        self.popped = False

    def update(self, surroundings):
        if self.popped:
            return Water("air", "#cef", 0), None
        else:
            if surroundings["top"].cell_type == "air":
                air = surroundings["top"]
                return air, "top"
            else:
                self.popped = True
                return None, None
