from cube import Cube
from visualizer import display_cube
from properties import direction, color
from main import online_scrambler_wrapper


rubik = Cube()
rubik.load_solved_cube()
rubik.validate_cube()

display_cube(rubik)

#rubik.write_moves(online_scrambler_wrapper("R2"))
#rubik.write_moves(online_scrambler_wrapper("R2"))


moves = online_scrambler_wrapper("R2 R2")
print(moves, type(moves))
rubik.write_moves(moves)

display_cube(rubik)

