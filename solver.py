from typing import List
from collections import deque;
import Cube



def solve(cube: Cube) -> List[str]:



def score_heuristic(solved_cube: Cube, cube: Cube) -> int:
    score = 0
    for l, layer in enumerate(cube.data):
        for r, row in enumerate(layer):
            for c, tile in enumerate(row):
                


def distance_to_solved_position(search_tile: cube_tile, solved_cube: Cube, tile_layer: int, tile_row: int, tile_col: int) -> int:
    searching = True
    for l, layer in cube.data:
        for r, row in layer_space:
            for c, tile in layer_space:
                if tile.type == search_tile.type and set(x.color for x in tile.faces) == set(x.color for x in search_tile.faces):
                    # found
                    searching = False
                    break
            if not searching:
                break
        if not searching:
            break

    #NOTE - Manhattan Distance / 2 is the number of turns required.
    manhattan_distance = abs(l - tile_layer) + abs(r - tile_row) + abs(c - tile_col)
    return manhattan_distance / 2
    
    
