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

        else:
            self.type = tile_type.CORE

    def get_properties(self) -> str:
        return_str = ''
        if self.faces is None:
            return_str += ('core tile')
            return return_str
        
        match self.type:
            case tile_type.CENTER:
                return_str += (f'center:')
                
            case tile_type.EDGE:
                return_str += (f'edge:')

            case tile_type.CORNER:
                return_str += (f'corner:')

        for face in self.faces:
            return_str += ' (' + str(face.color) + ' ' + str(face.direction) + ')'

        return return_str


class Cube:
    def __init__(self):
        self.data = [[[None for _ in range(3)] for _ in range(3)] for _ in range(3)]

    def validate_cube(self):
        if len(self.data[1][1][1].faces) > 0:
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

    def read_face(self, face: direction):
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
                self.data[0] = matrix
            
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


    def turn(self, turn_face: direction, turns: int, prime: bool):
        matrix = self.read_face(turn_face)
        for _ in range(turns):
            if prime:
                matrix = rotate_counterclockwise(matrix)
            else:
                matrix = rotate_clockwise(matrix)

            matrix_temp = copy.copy(matrix)
            match turn_face:
                case direction.UP:
                    for r, row in enumerate(matrix_temp):
                        for t, tile in enumerate(row):
                            for f, copied_face in enumerate(tile.faces):
                                match copied_face.direction:                                        
                                    case direction.LEFT:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.BACK)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.FRONT)
                                    
                                    case direction.FRONT:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.LEFT)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.RIGHT)

                                    case direction.RIGHT:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.FRONT)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.BACK)

                                    case direction.BACK:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.RIGHT)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.LEFT)

                                    case _:
                                        pass

                case direction.FRONT:
                    for r, row in enumerate(matrix_temp):
                        for t, tile in enumerate(row):
                            for f, copied_face in enumerate(tile.faces):
                                match copied_face.direction:                                        
                                    case direction.LEFT:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.UP)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.DOWN)
                                    
                                    case direction.UP:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.RIGHT)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.LEFT)

                                    case direction.RIGHT:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.DOWN)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.UP)

                                    case direction.DOWN:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.LEFT)
                                            #debug = cube_face(copied_face.color, direction.LEFT)
                                            #print("HERE MF ->", cube_face.color, cube_face.direction)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.RIGHT)

                                    case _:
                                        pass
                

                case direction.LEFT:
                    for r, row in enumerate(matrix_temp):
                        for t, tile in enumerate(row):
                            for f, copied_face in enumerate(tile.faces):
                                match copied_face.direction:                                        
                                    case direction.UP:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.FRONT)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.BACK)
                                    
                                    case direction.FRONT:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.DOWN)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.UP)

                                    case direction.DOWN:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.BACK)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.FRONT)

                                    case direction.BACK:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.UP)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.DOWN)

                                    case _:
                                        pass


                case direction.RIGHT:
                    for r, row in enumerate(matrix_temp):
                        for t, tile in enumerate(row):
                            for f, copied_face in enumerate(tile.faces):
                                match copied_face.direction:                                        
                                    case direction.FRONT:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.UP)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.DOWN)
                                    
                                    case direction.DOWN:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.FRONT)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.BACK)

                                    case direction.BACK:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.DOWN)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.UP)

                                    case direction.UP:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.BACK)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.FRONT)

                                    case _:
                                        pass

                case direction.DOWN:
                    for r, row in enumerate(matrix_temp):
                        for t, tile in enumerate(row):
                            for f, copied_face in enumerate(tile.faces):
                                match copied_face.direction:                                        
                                    case direction.FRONT:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.RIGHT)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.LEFT)
                                    
                                    case direction.RIGHT:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.BACK)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.FRONT)

                                    case direction.BACK:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.LEFT)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.RIGHT)

                                    case direction.LEFT:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.FRONT)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.BACK)

                                    case _:
                                        pass


                case direction.BACK:
                    for r, row in enumerate(matrix_temp):
                        for t, tile in enumerate(row):
                            for f, copied_face in enumerate(tile.faces):
                                match copied_face.direction:                                        
                                    case direction.UP:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.LEFT)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.RIGHT)
                                    
                                    case direction.LEFT:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.DOWN)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.UP)

                                    case direction.DOWN:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.RIGHT)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.LEFT)

                                    case direction.RIGHT:
                                        if not prime:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.UP)
                                        else:
                                            matrix[r][t].faces[f] = cube_face(copied_face.color, direction.DOWN)

                                    case _:
                                        pass

        for row in matrix:
            for tile in row:
                stringamabob = ''
                for x in tile.faces: 
                    stringamabob += f'{x.color}, {x.direction} -- '
                

        self.write_face(turn_face, matrix)



    def print_cube(self):
        for l, layer in enumerate(self.data):
            for r, row in enumerate(layer):
                for t, tile in enumerate(row):
                    print(f'layer {l}, row {r}, tile {t}: {tile.get_properties()}')
                    
    
    def write_moves(self, moveList: List[str]):
        for move in moveList:
            dir: direction
            double_turn = False
            prime = False
            match move[0]:
                case "U":
                    dir = direction.UP
                case "F":
                    dir = direction.FRONT
                case "R":
                    dir = direction.RIGHT
                case "B":
                    dir = direction.BACK
                case "L":
                    dir = direction.LEFT
                case "D":
                    dir = direction.DOWN
            
            if len(move) > 1:
                match move[1]:
                    case "i":
                        prime = True
                    case "2":
                        double_turn = True
            
            if not double_turn:
                self.turn(dir, 1, prime)    
            else:
                self.turn(dir, 2, prime)

