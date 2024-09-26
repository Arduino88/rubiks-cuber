from enum import Enum
from typing import Set, List

class color(Enum):
    WHITE = 0
    BLUE = 1
    RED = 2
    GREEN = 3
    ORANGE = 4
    YELLOW = 5

class tile_type(Enum):
    CENTER = 1
    EDGE = 2
    CORNER = 3

class cube_tile:
    def __init__(self, faces: Set[color]): # number of sides -> len(faces)
        self.faces = faces
        if faces:
            match len(faces):
                case 1:
                    self.type = tile_type.CENTER

                case 2:
                    self.type = tile_type.EDGE

                case 3:
                    self.type = tile_type.CORNER


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

            match col_num:
                case 0:
                    return_set.add(color.RED)

                case 2:
                    return_set.add(color.ORANGE)

            match row_num:
                case 0:
                    return_set.add(color.GREEN)

                case 2:
                    return_set.add(color.BLUE)

            return return_set

        
        for layer in range(3):
            for i in range(3):
                for j in range(3):
                    self.data[layer][i][j] = cube_tile(generate_tile(layer, i, j))


    def print_cube(self):
        for layer in self.data:
            for column in layer:
                for tile in column:
                    if tile.faces is None:
                        print('core tile')
                        continue

                    match tile.type:
                        case tile_type.CENTER:
                            print(f'center: {tile.faces}')
                        
                        case tile_type.EDGE:
                            print(f'edge: {tile.faces}')

                        case tile_type.CORNER:
                            print(f'corner: {tile.faces}')



if __name__ == "__main__":
    tile1 = cube_tile([color.RED, color.GREEN, color.YELLOW])
    rubik = cube()
    print(rubik.data)
    rubik.load_solved_cube()
    rubik.validate_cube()
    rubik.print_cube()
