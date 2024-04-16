from Materials.Cell import Cell
import random


class Sand(Cell):
    def __init__(self):
        super().__init__("sand", "#e6be0e")

    def update(self, surroundings):
        random_move = []
        if surroundings["bottom"].cell_type == "air" or surroundings["bottom"].cell_type == "water":
            air = surroundings["bottom"]
            return air, "bottom"
        else:
            if surroundings["bottom_left"].cell_type == "air" and surroundings["left"].cell_type != "wall":
                random_move.append("bottom_left")
            if surroundings["bottom_left"].cell_type == "water" and surroundings["left"].cell_type != "wall":
                random_move.append("bottom_left")
            if surroundings["bottom_right"].cell_type == "air" and surroundings["right"].cell_type != "wall":
                random_move.append("bottom_right")
            if surroundings["bottom_right"].cell_type == "water" and surroundings["right"].cell_type != "wall":
                random_move.append("bottom_right")
            if len(random_move) != 0:
                move = random.choice(random_move)
                air = surroundings[move]
                return air, move
            else:
                return None, None
