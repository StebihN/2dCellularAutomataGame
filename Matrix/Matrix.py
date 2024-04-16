from Materials.Usable.Balloon import Balloon
from Materials.Usable.Fire import Fire
from Materials.Usable.Wall import Wall
from Materials.Usable.Sand import Sand
from Materials.Usable.Water import Water
from Materials.Usable.Wood import Wood
from Materials.Usable.Air import Air
import random


class Matrix:
    def __init__(self, width, height, block_size, draw_mode):
        self.width = width
        self.height = height
        self.block_size = block_size
        self.draw_mode = draw_mode
        self.matrix = []

        self.fill_matrix()

    def fill_matrix(self):
        for matrix_row in range(0, self.height):
            self.matrix.append([])
            for matrix_index in range(0, self.width):
                if matrix_row == 0 or matrix_row == self.height - 1:
                    self.matrix[matrix_row].append(Wall())
                elif matrix_index == 0 or matrix_index == self.width - 1:
                    self.matrix[matrix_row].append(Wall())
                else:
                    number = random.choice((0, 1))
                    if number == 1:
                        self.matrix[matrix_row].append(Wall())
                    else:
                        self.matrix[matrix_row].append(Water("air", "#cef", 0))

    def update_cells(self):
        new_matrix = [row[:] for row in self.matrix]
        for row in range(0, self.height):
            if row == 0:
                top = self.height - 1
            else:
                top = row - 1
            if row == self.height - 1:
                bottom = 0
            else:
                bottom = row + 1
            for index in range(0, self.width):
                if index == 0:
                    left = self.width - 1
                else:
                    left = index - 1
                if index == self.width - 1:
                    right = 0
                else:
                    right = index + 1

                current_cell = self.matrix[row][index]
                surroundings = {"top_left": self.matrix[top][left],
                                "top": self.matrix[top][index],
                                "top_right": self.matrix[top][right],
                                "left": self.matrix[row][left],
                                "right": self.matrix[row][right],
                                "bottom_left": self.matrix[bottom][left],
                                "bottom": self.matrix[bottom][index],
                                "bottom_right": self.matrix[bottom][right]}

                new_cell, move = current_cell.update(surroundings)

                if new_cell:
                    new_matrix[row][index] = new_cell
                if move == "top_left":
                    new_matrix[top][left] = current_cell
                if move == "top":
                    new_matrix[top][index] = current_cell
                if move == "top_right":
                    new_matrix[top][right] = current_cell
                if move == "left":
                    new_matrix[row][left] = current_cell
                if move == "right":
                    new_matrix[row][right] = current_cell
                if move == "bottom_left":
                    new_matrix[bottom][left] = current_cell
                if move == "bottom":
                    new_matrix[bottom][index] = current_cell
                if move == "bottom_right":
                    new_matrix[bottom][right] = current_cell

        self.matrix = [row[:] for row in new_matrix]

    def set_draw_mode(self, draw_mode):
        self.draw_mode = draw_mode

    def draw_element(self, event, matrix, draw_mode="sand"):
        x, y = event.x // self.block_size, event.y // self.block_size
        if matrix[y][x].cell_type == "air":
            if draw_mode == "sand":
                matrix[y][x] = Sand()
            elif draw_mode == "wood":
                matrix[y][x] = Wood()
            elif draw_mode == "fire":
                matrix[y][x] = Fire()
            elif draw_mode == "water":
                matrix[y][x] = Water("water", "#2389da", 1)
            elif draw_mode == "balloon":
                matrix[y][x] = Balloon()
