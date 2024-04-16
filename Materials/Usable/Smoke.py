from Materials.Cell import Cell
from Materials.Usable.Water import Water
import random


class Smoke(Cell):
    def __init__(self, color):
        super().__init__("smoke", color)
        self.life = 0

    def update(self, surroundings):
        random_move = []
        self.life += 1
        if self.life == 20:
            return Water("air", "#cef", 0), None
        else:
            if surroundings["top"].cell_type == "air":
                random_move.append("top")
            if surroundings["top_left"].cell_type == "air" and surroundings["top_left"].cell_type != "wall":
                random_move.append("top_left")
            if surroundings["top_right"].cell_type == "air" and surroundings["top_right"].cell_type != "wall":
                random_move.append("top_right")
            if len(random_move) != 0:
                move = random.choice(random_move)
                air = surroundings[move]
                return air, move
            else:
                return None, None
