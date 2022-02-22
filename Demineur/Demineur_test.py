import numpy
from Demineur_main import *


l_plat = 5
h_plat = 5

grid = Grid()
grid.bomb_map[4,0] = 1
grid.bomb_map[2,2] = 1
grid.bomb_map[4,4] = 1
grid.bomb_map[4,1] = 1
print(grid.bomb_map)
print(grid.voisins_bombe(4,3))
if grid.voisins_bombe(0,0) == 0 and grid.voisins_bombe(3,1) == 3 and grid.voisins_bombe(4,3) == 1 :
    print("voisin_bomb Successful")
else : 
    print("Error voisin_bomb")

print("new grid")
grid.display_grid()
grid.disp_map = numpy.ones((grid.h_grid,grid.l_grid), dtype=numpy.int8)
print("fully uncovered grid")
grid.display_grid()
