from enum import Enum

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
    DOWN = 5

class tile_type(Enum):
    CENTER = 1
    EDGE = 2
    CORNER = 3
