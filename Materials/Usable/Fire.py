from Materials.Cell import Cell
from Materials.Usable.Smoke import Smoke
import random


class Fire(Cell):
    def __init__(self):
        super().__init__("fire", "#cf1920")

    def update(self, surroundings):
        random_move = []
        if surroundings["bottom"].cell_type != "air":
            if surroundings["bottom"].cell_type == "wood":
                return Smoke("#323333"), None
            else:
                return Smoke("#919494"), None
        else:
            if surroundings["bottom"].cell_type == "air":
                random_move.append("bottom")
            if surroundings["bottom_left"].cell_type == "air" and surroundings["bottom_left"].cell_type != "wall":
                random_move.append("bottom_left")
            if surroundings["bottom_right"].cell_type == "air" and surroundings["bottom_right"].cell_type != "wall":
                random_move.append("bottom_right")
            if len(random_move) != 0:
                move = random.choice(random_move)
                air = surroundings[move]
                return air, move
            else:
                return None, None
