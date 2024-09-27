from matrix_transform import print_matrix, rotate_clockwise, rotate_counterclockwise

if __name__ == "__main__":
    matrix = [[y + 3*x for y in range(3)] for x in range(3)]
    
    for _ in range(10):
        print_matrix(matrix)
        matrix = rotate_clockwise(matrix)


