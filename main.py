from cube import Cube, cube_tile
from properties import color, direction 
from solver import score_heuristic
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

    print('SCRAMBLER STRING')
    print(converted)
    print(return_list)
    return return_list


if __name__ == "__main__":
    rubik = Cube()
    rubik.load_solved_cube()
    rubik.validate_cube()
    solved_cube = copy.deepcopy(rubik)
    print('SCORE:', score_heuristic(rubik, solved_cube))

    #display_cube(rubik)

    rubik.write_moves(online_scrambler_wrapper("F2 R' D' F2 U' L F R D2 U2 F' U' D' F2 U' B' D2 R B D2 B2 F2 D R F2"))
    
    #rubik.write_moves(online_scrambler_wrapper("B2 U"))
    display_cube(rubik)
    print('SCORE:', score_heuristic(rubik, solved_cube))
