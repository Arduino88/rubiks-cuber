from typing import List, Tuple
from matrix_transform import rotate_clockwise, rotate_counterclockwise 
from properties import color, direction, tile_type
import copy

class cube_face:
    def __init__(self, color: color, direction: direction):
        self.color = color
        self.direction = direction


class cube_tile:
    def __init__(self, faces: List[cube_face]): # number of sides -> len(faces)
        self.faces = faces
        #self.orientation = direction.UP
        if faces:
            match len(faces):
                case 1:
                    self.type = tile_type.CENTER

                case 2:
                    self.type = tile_type.EDGE

                case 3:
                    self.type = tile_type.CORNER

    def get_properties(self) -> str:
        return_str = ''
        if self.faces is None:
            return_str += ('core tile')
            return return_str
        
        match self.type:
            case tile_type.CENTER:
                return_str += (f'center: {self.faces}')
                
            case tile_type.EDGE:
                return_str += (f'edge: {self.faces}')

            case tile_type.CORNER:
                return_str += (f'corner: {self.faces}')

        return return_str


class cube:
    def __init__(self):
        self.data = [[[None for _ in range(3)] for _ in range(3)] for _ in range(3)]

    def validate_cube(self):
        if self.data[1][1][1].faces is not None:
            raise ValueError(f'center of cube has been assigned a value: {self.data[1][1][1]}')

    def load_solved_cube(self):
        def generate_tile(layer_num: int, col_num: int, row_num: int) -> List[cube_face]:
            return_list = []
            if layer_num == col_num == row_num == 1:
                return return_list

            match layer_num:
                case 0:
                    return_list.append(cube_face(color.WHITE, direction.UP))

                case 2:
                    return_list.append(cube_face(color.YELLOW, direction.DOWN))

            match row_num:
                case 0:
                    return_list.append(cube_face(color.ORANGE, direction.LEFT))

                case 2:
                    return_list.append(cube_face(color.RED, direction.RIGHT))

            match col_num:
                case 0:
                    return_list.append(cube_face(color.BLUE, direction.BACK))

                case 2:
                    return_list.append(cube_face(color.GREEN, direction.FRONT))

            return return_list

        
        for layer in range(3):
            for i in range(3):
                for j in range(3):
                    self.data[layer][i][j] = cube_tile(generate_tile(layer, i, j))

    def read_face(self, face: direction) -> List[List[cube_tile]]:
        match face:
            case direction.UP:
                matrix = self.data[0]

            case direction.RIGHT:
                matrix = [[self.data[l][r][2] for r in reversed(range(3))] for l in range(3)]

            case direction.FRONT:
                matrix = [[self.data[l][2][c] for c in range(3)] for l in range(3)]

            case direction.LEFT:
                matrix = [[self.data[l][r][0] for r in range(3)] for l in range(3)]

            case direction.BACK:
                matrix = [[self.data[l][0][c] for c in range(3)] for l in range(3)]

            case direction.DOWN:
                matrix = [[self.data[2][r][c] for c in range(3)] for r in reversed(range(3))]

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
                        self.data[i][2 - j][2] = matrix[i][j]

            case direction.FRONT:
                for i in range(3):
                    for j in range(3): 
                        self.data[i][2][j] = matrix[i][j]

            case direction.LEFT:
                for i in range(3):
                    for j in range(3):
                        self.data[i][j][0] = matrix[i][j]

            case direction.BACK:
                for i in range(3):
                    for j in range(3):
                        self.data[2 - i][0][2 - j] = matrix[i][j]

            case direction.DOWN:
                for i in range(3):
                    for j in range(3):
                        self.data[2][2 - i][j] = matrix[i][j]


    def turn(self, face: direction, turns: int, prime: bool):
        matrix = self.read_face(face)
        for _ in range(turns):
            match face:
                case direction.UP:
                    matrix_temp = copy.deepcopy(matrix)
                    for row in matrix:
                        for tile in row:
                            for f in tile.faces:
                                if f 
                                

                case direction.FRONT:

                case direction.LEFT:

                case direction.RIGHT:

                case direction.DOWN:

                case direction.BACK:




            if prime:
                matrix = rotate_counterclockwise(matrix)
            else:
                matrix = rotate_clockwise(matrix)
        self.write_face(face, matrix)



    def print_cube(self):
        for l, layer in enumerate(self.data):
            for r, row in enumerate(layer):
                for t, tile in enumerate(row):
                    print(f'layer {l}, row {r}, tile {t}: {tile.get_properties()}')

                    
                    

