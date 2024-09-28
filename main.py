from cube import cube, cube_tile
from properties import color, direction 

if __name__ == "__main__":
    rubik = cube()
    #print(rubik.data)
    rubik.load_solved_cube()
    rubik.validate_cube()
    rubik.print_cube()
    print('------------------\n')
    rubik.turn(direction.FRONT, turns=1, prime=False)

    # Tested: UP, FRONT, RIGHT, LEFT, DOWN, BACK 

    print('TURNED --')
    rubik.print_cube()
