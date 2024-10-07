from cube import Cube, cube_tile
from properties import color, direction 

if __name__ == "__main__":
    rubik = Cube()
    #print(rubik.data)
    rubik.load_solved_cube()
    rubik.validate_cube()
    rubik.print_cube()
    print('------------------\n')
    rubik.write_moves(['F','R', 'U', 'Ri', 'Ui', 'Fi'])
    
    # Tested: UP, FRONT, RIGHT, LEFT, DOWN, BACK 

    print('TURNED --')
    rubik.print_cube()
