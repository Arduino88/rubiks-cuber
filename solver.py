from typing import List, Tuple
from collections import deque;
from cube import Cube, cube_tile, cube_face



def solve(cube: Cube) -> List[str]:
    pass

def scaled(score: float, score_range: Tuple[float], max_return: float) -> float:
    if not score_range[0] <= score <= score_range[1]:
        raise ValueError(f'invalid score: {score}, range: {score_range}')
    ratio = score / score_range[1]
    return max_return * ratio
    

def score_heuristic(solved_cube: Cube, cube: Cube) -> int:
    score = 0
    for l, layer in enumerate(cube.data):
        for r, row in enumerate(layer):
            for c, tile in enumerate(row):
                score += tile_score(tile, solved_cube, l, r, c)

    return scaled(score, (0, 60), 26)


def tile_score(search_tile: cube_tile, solved_cube: Cube, tile_layer: int, tile_row: int, tile_col: int) -> int:
    score = 0
    searching = True
    for l, layer in enumerate(solved_cube.data):
        for r, row in enumerate(layer):
            for c, tile in enumerate(row):
                if tile.type == search_tile.type and set(x.color for x in tile.faces) == set(x.color for x in search_tile.faces):
                    # found 
                    searching = False
                    break
            if not searching:
                break
        if not searching:
            break

    #NOTE - Manhattan Distance / 2 is the number of turns required.
    score += (abs(l - tile_layer) + abs(r - tile_row) + abs(c - tile_col)) / 2
    return score
    
    
