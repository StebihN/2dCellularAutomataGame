from tkinter import *
from Matrix.Matrix import Matrix


def update_map(provided_matrix):
    for row in range(0, provided_matrix.height):
        for index in range(0, provided_matrix.width):
            cell = provided_matrix.matrix[row][index]

            x1, y1 = index * provided_matrix.block_size, row * provided_matrix.block_size
            x2, y2 = x1 + provided_matrix.block_size, y1 + provided_matrix.block_size

            block_at_position = canvas.find_enclosed(x1, y1, x2, y2)
            canvas.delete(block_at_position)

            rect = canvas.create_rectangle(x1, y1, x2, y2, outline='', fill=cell.color)
            canvas.tag_lower(rect)

    canvas.update()


def frame():
    matrix.update_cells()
    update_map(matrix)
    master.after(round(1 / 100 * 1000), frame())


matrix = Matrix(60, 40, 20, "sand")


master = Tk()
master.bind("<a>", lambda event: matrix.set_draw_mode("sand"))
master.bind("<s>", lambda event: matrix.set_draw_mode("fire"))
master.bind("<d>", lambda event: matrix.set_draw_mode("wood"))
master.bind("<f>", lambda event: matrix.set_draw_mode("water"))
master.bind("<g>", lambda event: matrix.set_draw_mode("balloon"))

width = matrix.width * matrix.block_size
height = matrix.height * matrix.block_size
canvas = Canvas(master, width=width, height=height, bg="#cef", highlightthickness=0)
canvas.bind("<Button-1>", lambda event: matrix.draw_element(event, matrix=matrix.matrix, draw_mode=matrix.draw_mode))
canvas.pack()

master.after(round(1 / 100 * 1000), frame())
master.mainloop()
