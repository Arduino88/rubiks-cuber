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


moves = online_scrambler_wrapper("F2 R' D' F2 U' L F R D2 U2 F' U' D' F2 U' B' D2 R B D2 B2 F2 D R F2")
#print(moves, type(moves))
rubik.write_moves(moves)

display_cube(rubik)

