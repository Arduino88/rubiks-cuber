from typing import List

def transpose(matrix: List[list]) -> List[list]:
    print('transpose() called')
    n = len(matrix)
    m = len(matrix[0])

    transposed = [[matrix[i][j] for i in range(n)] for j in range(m)]
    return transposed

def transpose_reversed(matrix: List[list]) -> List[list]:
    n = len(matrix)
    m = len(matrix[0])

    transposed = [[matrix[i][j] for i in reversed(range(n))] for j in reversed(range(m))]
    return transposed

def flip_horizontal(matrix: List[list]) -> List[list]:
    transposed = [list(reversed(row)) for row in matrix]
    return transposed


def rotate_counterclockwise(matrix: List[list]) -> List[list]:
    return flip_horizontal(transpose(matrix))

def rotate_clockwise(matrix: List[list]) -> List[list]:
    return flip_horizontal(transpose_reversed(matrix))


def print_matrix(matrix: List[list]):
    for r, row in enumerate(matrix):
        print(f'row {r}: {row}')
