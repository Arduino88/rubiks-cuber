from typing import List, Tuple
from collections import deque;
from cube import Cube, cube_tile, cube_face
from visualizer import display_cube
import heapq
import copy
from random import random
import sys

def solve(initial_cube: Cube, solved_cube: Cube) -> List[str]:
    came_from = {initial_cube.hash(): None}
    distances = {initial_cube.hash(): 0}
    heap = [(score_heuristic(solved_cube, initial_cube), random()/1000, initial_cube)]
    min_score = float('inf')
    min_cube_state = None
    visited = set()
    display_counter = 1000

    while heap:
        #print(heap)
        adjusted_distance, _, cube = heapq.heappop(heap)
        visited.add(cube.hash())
        #search loop
        for move in 'U F D L R B Ui Fi Di Li Ri Bi'.split():
            
            temp_cube = copy.deepcopy(cube)
            temp_cube.write_moves(move)
            hash = temp_cube.hash()
            
            if score_heuristic(solved_cube, temp_cube) == 0:
                print('SOLUTION FOUND')
                min_cube_state = temp_cube
                display_cube(min_cube_state)
                return

            if hash not in visited:
                came_from[hash] = cube
                distances[hash] = distances[cube.hash()] + 1
    
            
            else:
                if distances[hash] > distances[cube.hash()] + 1:
                    distances[hash] = distances[cube.hash()] + 1
                    came_from[hash] = cube
            
            
            
            if temp_cube.hash() not in visited:
                score = score_heuristic(solved_cube, temp_cube)
                if score < min_score:
                    min_score = score
                    min_cube_state = copy.deepcopy(temp_cube)
                push_tuple = (score, random()/1000, temp_cube)
                print(f'score: {score}, min_score: {min_score} len(heap): {len(heap)}, size: {sys.getsizeof(heap)}')
                debug_heap = [heap[x][0] for x in range(min(10, len(heap)))]
                print(debug_heap)
                heapq.heappush(heap, push_tuple)
                if display_counter > 0:
                    display_counter -= 1             
                else:
                    display_counter = 1000
                    display_cube(min_cube_state)

    print('A* finished')
    #print(distances)
    #print('SEPARATOR \n\n\n')
    #print(came_from)



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
                print(tile.get_properties())
                score += tile_score(tile, solved_cube, l, r, c)

    return scaled(score, (0, 72), 72)

def opposite(face_set: set) -> set:
    for face in face_set:
        face.replace('UP', 'DOWN')
        face.replace('DOWN', 'UP')
        face.replace('RIGHT', 'LEFT')
        face.replace('LEFT', 'RIGHT')
        face.replace('FRONT', 'BACK')
        face.replace('BACK', 'FRONT')
    return face_set


def tile_score(search_tile: cube_tile, solved_cube: Cube, tile_layer: int, tile_row: int, tile_col: int) -> int:
    score = 0
    searching = True
    
    piece = cube_tile.get_properties(search_tile)
    #print("unsolved", piece)
    piece = piece.replace(': (', ',')
    piece = piece.replace(') (', ',')
    piece_data = piece[:-1].split(',')
    piece_type = piece_data[0] #centre, edge, etc.
    face_orient = set()
    
    for i in piece_data[1:]:
        face_orient.add(i)    

    for l, layer in enumerate(solved_cube.data):
        for r, row in enumerate(layer):
            for c, tile in enumerate(row):
                if tile.type == search_tile.type and set(x.color for x in tile.faces) == set(x.color for x in search_tile.faces):
                    # found
                    s_tile = tile.get_properties()
                    searching = False
                    break
            if not searching:
                break
        if not searching:
            break
    
    s_piece = piece.replace(': (', ',')
    s_piece = s_piece.replace(') (', ',')
    s_piece_data = s_piece[:-1].split(',')
    s_face_orient = set()
    
    for i in s_piece_data[1:]:
        s_face_orient.add(i)
    
        
    #NOTE - Manhattan Distance / 2 is the number of turns required.
    #only true for corner pieces - edge pieces have more dependancies 
    score += (abs(l - tile_layer) + abs(r - tile_row) + abs(c - tile_col)) / 2
    
    #orientation fix
    match score:
        case 0:
            match piece_type:
                case "edge":
                    #+3 if misoriented
                    if(s_face_orient != face_orient):
                        score += 3
                case "corner":
                    #+2 if misoriented
                    if(s_face_orient != face_orient):
                        score += 2
                case _:
                    pass
        case 1:
            match piece_type:
                case "edge":
                    #+1 if actually a double move away
                    if(max(abs(l - tile_layer), abs(r - tile_row), abs(c - tile_col)) == 2):
                        score += 1  
                    #+1 if misaligned 
                    aligned = False
                    for tile_face in face_orient:
                        #print(tile_face, face_orient, s_face_orient)
                        if(tile_face in s_face_orient):
                            aligned = True
                    if(aligned == False):
                        score += 1
                case "corner":
                    #+1 if misoriented
                    aligned = False
                    for tile_face in face_orient:
                        if(tile_face in s_face_orient):
                            aligned = True
                    if(aligned == False):
                        score += 1 
                case _:
                    pass
        case 2:
            match piece_type:
                case "edge":
                    #+1 if far side
                    if((l - tile_layer) == 0 or (r - tile_row) == 0 or (c - tile_col) == 0):
                        score += 1
                    #+1 if opposite orientation matches
                    aligned = True
                    for tile_face in opposite(face_orient):
                        if(tile_face in s_face_orient):
                            aligned = False
                    if(aligned == False):
                        score += 1
                    
                    
                case "corner":
                    pass #must always be two
                case _:
                    pass
        case 3:
            match piece_type:
                case "edge":
                    pass #case doesnt exist lol in our stupid set up
                case "corner":
                    pass #must always be 3
                case _:
                    pass
    
    print(score)
    return score
    
    
