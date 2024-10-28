from cube import Cube, cube_tile
from properties import color, direction 
from solver import score_heuristic
from typing import List
import copy
from visualizer import display_cube 

def online_scrambler_wrapper(moves: str) -> List[str]:
    return moves.replace("'", "i").split()

if __name__ == "__main__":
    rubik = Cube()
    rubik.load_solved_cube()
    rubik.validate_cube()
    #rubik.print_cube()
    solved_cube = copy.deepcopy(rubik)
    print('SCORE:', score_heuristic(rubik, solved_cube))

    #display_cube(rubik)

    #rubik.write_moves(online_scrambler_wrapper("F2 R' D' F2 U' L F R D2 U2 F' U' D' F2 U' B' D2 R B D2 B2 F2 D R F2"))
    
    moves = online_scrambler_wrapper("R2 R2")
    print(moves)
    rubik.write_moves(moves)
    #display_cube(rubik)
    #print('SCORE:', score_heuristic(rubik, solved_cube))

    rubik.write_moves(online_scrambler_wrapper("R2"))
    #display_cube(rubik)
    Cube.print_cube(rubik)
    #print('SCORE:', score_heuristic(rubik, solved_cube))
