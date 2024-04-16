from Materials.Cell import Cell
from Materials.Usable.Air import Air
from Materials.Usable.Water import Water

class Wall(Cell):
    def __init__(self):
        super().__init__(cell_type="wall", color="#703b0a")

    def update(self, surroundings):
        cell_count = 0
        for cell in surroundings.values():
            if cell.cell_type == "wall":
                cell_count += 1

        if (cell_count > 8) or (cell_count < 2):
            return Water("air", "#cef", 0), None
        elif (cell_count == 6) or (cell_count == 7) or (cell_count == 8):
            return None, None
        else:
            return None, None
