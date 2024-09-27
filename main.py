from enum import Enum
from typing import Set, List
from copy import deepcopy
from matrix_transform import rotate_clockwise, rotate_counterclockwise 

class color(Enum):
    WHITE = 0
    GREEN = 1
    RED = 2
    BLUE = 3
    ORANGE = 4
    YELLOW = 5

class direction(Enum):
    UP = 0
    FRONT = 1
    RIGHT = 2
    BACK = 3
    LEFT = 4
    BOTTOM = 5

class tile_type(Enum):
    CENTER = 1
    EDGE = 2
    CORNER = 3

class cube_tile:
    def __init__(self, faces: Set[color]): # number of sides -> len(faces)
        self.faces = faces
        self.orientation = direction.UP
        if faces:
            match len(faces):
                case 1:
                    self.type = tile_type.CENTER

                case 2:
                    self.type = tile_type.EDGE

                case 3:
                    self.type = tile_type.CORNER

    def print(self):
        if self.faces is None:
            print('core tile')
            return
        
        match self.type:
            case tile_type.CENTER:
                print(f'center: {self.faces}, orientation: {self.orientation}')
                
            case tile_type.EDGE:
                print(f'edge: {self.faces}, orientation: {self.orientation}')

            case tile_type.CORNER:
                print(f'corner: {self.faces}, orientation: {self.orientation}')


class cube:
    def __init__(self):
        self.data = [[[None for _ in range(3)] for _ in range(3)] for _ in range(3)]

    def validate_cube(self):
        if self.data[1][1][1].faces is not None:
            raise ValueError(f'center of cube has been assigned a value: {self.data[1][1][1]}')

    def load_solved_cube(self):
        def generate_tile(layer_num: int, col_num: int, row_num: int) -> set:
            if layer_num == col_num == row_num == 1:
                return None

            return_set = set()

            match layer_num:
                case 0:
                    return_set.add(color.WHITE)

                case 2:
                    return_set.add(color.YELLOW)

            match row_num:
                case 0:
                    return_set.add(color.ORANGE)

                case 2:
                    return_set.add(color.RED)

            match col_num:
                case 0:
                    return_set.add(color.BLUE)

                case 2:
                    return_set.add(color.GREEN)

            return return_set

        
        for layer in range(3):
            for i in range(3):
                for j in range(3):
                    self.data[layer][i][j] = cube_tile(generate_tile(layer, i, j))

    def read_face(self, face: direction) -> List[List[cube_tile]]:
        match face:
            case direction.UP:
                matrix = self.data[0]

            case direction.RIGHT:
                matrix = [[self.data[i][j][2] for j in range(3)] for i in range(3)]

            case direction.FRONT:
                matrix = [[self.data[i][2][j] for j in reversed(range(3))] for i in range(3)]

            case direction.BACK:
                matrix = [[self.data[i][j][0] for j in reversed(range(3))] for i in range(3)]

            case direction.LEFT:
                matrix = [[self.data[i][0][j] for j in range(3)] for i in range(3)]

            case direction.BOTTOM:
                matrix = [[self.data[2][i][j] for j in range(3)] for i in range(reversed(3))]

            case _:
                raise ValueError(f'Direction {face} not valid')

        return matrix

    def write_face(self, face: direction, matrix: List[List[cube_tile]]):
        match face:
            case direction.UP:
                self.data[0] = matrix;
            
            case direction.RIGHT:
                for i in range(3):
                    for j in range(3):
                        self.data[i][j][2] = matrix[i][j]

            case direction.FRONT:
                for i in range(3):
                    for j in reversed(range(3)): 
                        self.data[i][2][j] = matrix[i][j]

            case direction.BACK:
                for i in range(3):
                    for j in reversed(range(3)):
                        self.data[i][j][0] = matrix[i][j]

            case direction.LEFT:
                for i in range(3):
                    for j in range(3):
                        self.data[i][0][j] = matrix[i][j]

            case direction.BOTTOM:
                for i in reversed(range(3)):
                    for j in range(3):
                        self.data[2][i][j] = matrix[i][j]


    def turn(self, face: direction, turns: int, prime: bool):
        matrix = self.read_face(face)
        for _ in range(turns):
            print('turning...')
            if prime:
                matrix = rotate_counterclockwise(matrix)
            else:
                matrix = rotate_clockwise(matrix)
        self.write_face(face, matrix)



    def print_cube(self):
        for l, layer in enumerate(self.data):
            for r, row in enumerate(layer):
                for t, tile in enumerate(row):
                    print(f'layer {l}, row {r}, tile {t}:')
                    tile.print()
                    

if __name__ == "__main__":
    tile1 = cube_tile([color.RED, color.GREEN, color.YELLOW])
    rubik = cube()
    #print(rubik.data)
    rubik.load_solved_cube()
    rubik.validate_cube()
    rubik.print_cube()
    print('------------------\n')
    rubik.turn(direction.LEFT, turns=1, prime=False)


    print('TURNED --')
    rubik.print_cube()
