from typing import List, Tuple
from collections import deque;
from cube import Cube, cube_tile, cube_face, direction
from visualizer import display_cube
import heapq
import copy
from random import random
import sys

def solve(solved_cube: Cube, initial_cube: Cube) -> List[str]:

    #IDA* search

    def score_node(current_cost, node: Cube):
        return current_cost + score_heuristic(solved_cube, node)

    

    def search(head: Cube, threshhold: int) -> int: # returns -1 if solution found, else returns minimum threshhold to continue search
        q = deque()
        visited = set()

        q.appendleft((0, head, []))
        min_threshhold = float('inf')

        while q:
            #print(q)
            current_cost, node, moves = q.popleft()
            visited.add(node.hash())

            for move in 'U F D L R B Ui Fi Di Li Ri Bi'.split():
                temp_cube = copy.deepcopy(node)
                temp_cube.write_moves(move)
                temp_moves = moves + [move]
                

                if temp_cube.hash() in visited:
                    continue

                if temp_cube.is_solved(solved_cube):
                    print("SOLUTION FOUND")
                    print(temp_moves)
                    temp_cube.print_cube()
                    return -1

                score = score_node(current_cost, temp_cube) 
                
                if score <= threshhold:
                    q.append((current_cost + 1, temp_cube, temp_moves))

                else:
                    min_threshhold = min(min_threshhold, score)

        return min_threshhold


    threshhold = 0
    while True:
        result = search(initial_cube, threshhold)
        print(result)
        if result == -1:
            break
        threshhold = result












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

    return score/8
    #return scaled(score, (0, 72), 26)

def opposite(face_list: list) -> list:
    op_face_list = []
    
    for face in face_list:
        if(face[1] == 'UP'):
            op_face = (face[0], 'DOWN')
        elif(face[1] == 'DOWN'):
            op_face = (face[0], 'UP')
        elif(face[1] == 'RIGHT'):
            op_face = (face[0], 'LEFT')
        elif(face[1] == 'LEFT'):
            op_face = (face[0], 'RIGHT')
        elif(face[1] == 'BACK'):
            op_face = (face[0], 'FRONT')
        elif(face[1] == 'FRONT'):
            op_face = (face[0],  'BACK')

        op_face_list.append(op_face)
        
    return op_face_list


def tile_score(search_tile: cube_tile, solved_cube: Cube, tile_layer: int, tile_row: int, tile_col: int) -> int:
    score = 0
    searching = True
    
    piece = cube_tile.get_properties(search_tile)
    piece_type = piece[0]
    piece_faces = piece[1]    

    for l, layer in enumerate(solved_cube.data):
        for r, row in enumerate(layer):
            for c, tile in enumerate(row):
                if tile.type == search_tile.type and set(x.color for x in tile.faces) == set(x.color for x in search_tile.faces):
                    # found
                    s_piece = tile.get_properties()
                    searching = False
                    break
            if not searching:
                break
        if not searching:
            break
        
    s_piece_faces = s_piece[1]
        
    #NOTE - Manhattan Distance / 2 is the number of turns required.
    #only true for corner pieces - edge pieces have more dependancies 
    score += (abs(l - tile_layer) + abs(r - tile_row) + abs(c - tile_col)) / 2
    
    
    #orientation fix and edge distance fix
    match score:
        case 0:
            match piece_type:
                case piece_type.EDGE:
                    #+3 if misoriented
                    if(s_piece_faces != piece_faces):
                        score += 3
                case piece_type.CORNER:
                    #+2 if misoriented
                    if(s_piece_faces != piece_faces):
                        score += 2
                case _:
                    pass
        case 1:
            match piece_type:
                case piece_type.EDGE:
                    #+1 if actually a double move away
                    if(max(abs(l - tile_layer), abs(r - tile_row), abs(c - tile_col)) == 2):
                        score += 1  
                    #+1 if misaligned 
                    aligned = False
                    for tile_face in piece_faces:
                        #print(tile_face, piece_faces, s_piece_faces)
                        if(tile_face in s_piece_faces):
                            aligned = True
                    if(aligned == False):
                        score += 1
                case piece_type.CORNER:
                    #+2 if misoriented
                    aligned = False
                    for tile_face in piece_faces:
                        if(tile_face in s_piece_faces):
                            aligned = True
                    if(aligned == False):
                        score += 2 
                case _:
                    pass
        case 2:
            match piece_type:
                case piece_type.EDGE:
                    #+1 if far side
                    if((l - tile_layer) == 0 or (r - tile_row) == 0 or (c - tile_col) == 0):
                        score += 1
                    #+1 if opposite orientation matches
                    aligned = True
                    for tile_face in opposite(piece_faces):
                        if(tile_face in s_piece_faces):
                            aligned = False
                    if(aligned == False):
                        score += 1
                    
                    
                case piece_type.CORNER:
                    pass #must always be two
                case _:
                    pass
        case 3:
            match piece_type:
                case piece_type.EDGE:
                    pass #case doesnt exist lol in our stupid set up
                case piece_type.CORNER:
                    pass #must always be 3
                case _:
                    pass

    return score
    
    
