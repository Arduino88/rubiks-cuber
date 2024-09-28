from cube import cube, cube_tile
from properties import color, direction 

if __name__ == "__main__":
    tile1 = cube_tile([color.RED, color.GREEN, color.YELLOW])
    rubik = cube()
    #print(rubik.data)
    rubik.load_solved_cube()
    rubik.validate_cube()
    rubik.print_cube()
    print('------------------\n')
    rubik.turn(direction.BACK, turns=1, prime=True)

    # Tested: UP, FRONT, RIGHT, LEFT, DOWN, BACK 

    print('TURNED --')
    rubik.print_cube()
