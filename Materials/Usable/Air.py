from Materials.Cell import Cell


class Air(Cell):
    def __init__(self):
        super().__init__("air", "#ff0000")

    def update(self, surroundings):
        return None, None
