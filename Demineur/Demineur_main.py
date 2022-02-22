from msilib.schema import Error
import string
import numpy

l_plat = 5 #largeur du plateau   
h_plat = 5 #hauteur du plateau
num_mine = 5 #nombre de mine


class Grid :
    def __init__(self):
        self.num_mine = num_mine
        self.l_grid = l_plat
        self.h_grid = h_plat
        self.bomb_map = numpy.zeros((self.l_grid,self.h_grid),dtype=numpy.int8) 
        self.disp_map = numpy.zeros((self.l_grid,self.h_grid),dtype=numpy.int8) 
    
    def reveal(self,row, col):
        """reveals the tile located at location row, col"""
        if self.bomb_map[row,col] == 1 :
            print("GAME OVER")
        else :
            self.disp_map[row,col] = 1

    def display_grid(self) :
        """displays the uncovered grid in console"""
        grid_disp = numpy.zeros((self.l_grid,self.h_grid),dtype = numpy.str_) 
        for row in range (self.h_grid) :
            for col in range (self.l_grid):
                if self.disp_map[row,col] == 1:
                    if self.bomb_map[row,col] == 1:
                        grid_disp[row,col] = "X"
                    else :
                        grid_disp[row,col] = str(self.voisins_bombe(row,col))
                else :
                    grid_disp[row,col] = ""
        print(grid_disp)
                    




    def voisins_bombe(self,row,col):
        """Donne le nombre de bombes voisines d'une case donnée
        bomb_map : plateau sous forme de tableau numpy de 1 et de 0, 1 représentant une bombe
        return un entier entre 0 et 9"""
        if self.bomb_map[row,col] == 1 :
            raise Error
        compteur=0
        if row == 0 : #si on est sur l'arête du haut
            start_row = 0
            end_row = 1
        elif row == self.h_grid-1: #si on est sur l'arête du bas
            start_row = self.h_grid-2
            end_row = self.h_grid-1
        else :
            start_row =row-1
            end_row = row+1
        if col == 0 :   #si on est sur l'arête de gauche
            start_col = 0
            end_col = 1
        elif col == self.l_grid-1: #si on est sur l'arête de droite
            start_col = self.l_grid-2
            end_col = self.l_grid-1
        else :
            start_col =col-1
            end_col = col+1

        for i in range (start_row,end_row+1):
            for j in range (start_col,end_col+1):
                compteur += int(self.bomb_map[i,j])
        return compteur



