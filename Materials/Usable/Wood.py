from Materials.Cell import Cell
from Materials.Usable.Fire import Fire


class Wood(Cell):
    def __init__(self):
        super().__init__("wood", "#966F33")
        self.on_fire = False

    def update(self, surroundings):
        for cell in surroundings.values():
            if cell.cell_type == "fire":
                self.on_fire = True
                return None, None

        if self.on_fire:
            return Fire(), surroundings
        else:
            if surroundings["bottom"].cell_type == "air":
                air = surroundings["bottom"]
                surroundings["bottom"] = self
                return air, "bottom"
            else:
                return None, None
