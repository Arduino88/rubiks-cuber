import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import colors as mcolors
from enum import Enum
from properties import color, direction
from cube import Cube
from typing import List

color_map = {
    color.WHITE: 'white',
    color.GREEN: 'green',
    color.RED: 'red',
    color.BLUE: 'blue',
    color.ORANGE: 'orange',
    color.YELLOW: 'yellow'
}

def read_face_colors(cube: Cube, scan_face: direction) -> List[List[color]]:
    unprocessed_matrix = cube.read_face(scan_face)
    matrix = [
        [
            [tile_face.color for tile_face in tile.faces if tile_face.direction == scan_face][0]
            for tile in row if any(tile_face.direction == scan_face for tile_face in tile.faces)
        ]
        for row in unprocessed_matrix
    ]

    shape = [len(x) for x in matrix]

    if shape != [3, 3, 3]:
        cube.print_cube()
        raise ValueError(f'matrix is misshapen: {shape} read_face_colors()') 

    return matrix


def display(matrix_up, matrix_front, matrix_right, matrix_back, matrix_left, matrix_down):
    fig, axs = plt.subplots(3, 4, figsize=(10, 10))

    face_matrices = [
        (matrix_up, 'UP'),
        (matrix_left, 'LEFT'),
        (matrix_front, 'FRONT'),
        (matrix_right, 'RIGHT'),
        (matrix_back, 'BACK'),
        (matrix_down, 'DOWN')
    ]

    for (matrix, label), (row, col) in zip(face_matrices, [(0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1)]):
        axs[row, col].set_title(label)
       
        print(matrix)
        for i in range(3):
            for j in range(3):
                print(label, i, j)
                color = color_map[matrix[i][j]]
                rect = patches.Rectangle((j, i), 1, 1, facecolor=color, edgecolor='black')
                axs[row, col].add_patch(rect)

        axs[row, col].set_xlim(0, 3)
        axs[row, col].set_ylim(0, 3)
        axs[row, col].set_aspect('equal')
        axs[row, col].axis('off')  

    for ax in axs.flat:
        if not ax.has_data():
            ax.axis('off')

    plt.tight_layout()
    plt.show()

def display_cube(cube: Cube):
    matrix_up = read_face_colors(cube, direction.UP)
    matrix_right = read_face_colors(cube, direction.RIGHT)
    matrix_back = read_face_colors(cube, direction.BACK)
    matrix_left = read_face_colors(cube, direction.LEFT)
    matrix_front = read_face_colors(cube, direction.FRONT)
    matrix_down = read_face_colors(cube, direction.DOWN)
    display(matrix_up, matrix_front, matrix_right, matrix_back, matrix_left, matrix_down)


if __name__ == '__main__':
    matrix_up = [[color.WHITE, color.WHITE, color.WHITE],
                 [color.WHITE, color.WHITE, color.WHITE],
                 [color.WHITE, color.WHITE, color.WHITE]]

    matrix_right = [[color.RED, color.RED, color.RED],
                 [color.RED, color.RED, color.RED],
                 [color.RED, color.RED, color.RED]]

    matrix_back = [[color.BLUE, color.BLUE, color.BLUE],
                 [color.BLUE, color.BLUE, color.BLUE],
                 [color.BLUE, color.BLUE, color.BLUE]]

    matrix_left = [[color.ORANGE, color.ORANGE, color.ORANGE],
                 [color.ORANGE, color.ORANGE, color.ORANGE],
                 [color.ORANGE, color.ORANGE, color.ORANGE]]

    matrix_front = [[color.GREEN, color.GREEN, color.GREEN],
                 [color.GREEN, color.GREEN, color.GREEN],
                 [color.GREEN, color.GREEN, color.GREEN]]

    matrix_down = [[color.YELLOW, color.YELLOW, color.YELLOW],
                 [color.YELLOW, color.YELLOW, color.YELLOW],
                 [color.YELLOW, color.YELLOW, color.YELLOW]]


    display(matrix_up, matrix_front, matrix_right, matrix_back, matrix_left, matrix_down)
