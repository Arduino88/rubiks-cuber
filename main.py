from cube import Cube, cube_tile
from properties import color, direction 
from solver import score_heuristic
from typing import List
import copy

def online_scrambler_wrapper(moves: str) -> List[str]:
    return moves.replace("'", "i").strip()

if __name__ == "__main__":
    rubik = Cube()
    #print(rubik.data)
    rubik.load_solved_cube()
    rubik.validate_cube()
    rubik.print_cube()
    solved_cube = copy.deepcopy(rubik)
    print('SCORE:', score_heuristic(rubik, solved_cube))



    print('------------------\n')
    rubik.write_moves(online_scrambler_wrapper("F2 R' D' F2 U' L F R D2 U2 F' U' D' F2 U' B' D2 R B D2 B2 F2 D R F2"))
    
    # Tested: UP, FRONT, RIGHT, LEFT, DOWN, BACK 

    print('SCORE:', score_heuristic(rubik, solved_cube))

    print('TURNED --')
    rubik.print_cube()
