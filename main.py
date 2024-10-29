from cube import Cube, cube_tile
from properties import color, direction 
from solver import score_heuristic, solve
from typing import List
import copy
from visualizer import display_cube

def online_scrambler_wrapper(moves: str) -> List[str]:
    converted = moves.replace("'", "i").split()
    return_list = []
    for move in converted:
        if len(move) == 2 and move[1] == str(2):
            for _ in range(2):
                return_list.append(move[0])

        else:
            return_list.append(move)

    return return_list


if __name__ == "__main__":
    rubik = Cube()
    rubik.load_solved_cube()
    rubik.validate_cube()
    solved_cube = copy.deepcopy(rubik)
    #print('SCORE:', score_heuristic(solved_cube, rubik))

    #display_cube(rubik)

    rubik.write_moves(online_scrambler_wrapper("F' D R' F"))
    
    #moves = online_scrambler_wrapper("R2")
    #print(moves)
    #rubik.write_moves(moves)
    display_cube(rubik)
    #display_cube(rubik)
    print('SCORE:', score_heuristic(solved_cube, rubik))
    print(solve(solved_cube, rubik))

    #display_cube(rubik)
    #Cube.print_cube(rubik)
    #print('SCORE:', score_heuristic(rubik, solved_cube))
