import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import colors as mcolors
from enum import Enum
from properties import color

color_map = {
    color.WHITE: 'white',
    color.GREEN: 'green',
    color.RED: 'red',
    color.BLUE: 'blue',
    color.ORANGE: 'orange',
    color.YELLOW: 'yellow'
}

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
        
        for i in range(3):
            for j in range(3):
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
