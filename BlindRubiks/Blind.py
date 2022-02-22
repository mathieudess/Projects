#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Objectifs de l'appli : On donne un scramble, on nous retourne le solve avec la technique de notre choix, ainsi que le nombre de move (difficulté du solve) et une représentation graphique du cube
Une classe cube représenté par tableau de tableau de taille 6x8, dans l'ordre UDRLFB,sens lecture. Chaque couleur a une valeur associée:
blanc=0
jaune=1
bleu=2
vert=3
rouge=4
orange=5
Le cube est supposé orienté blanc sur U et rouge sur F"""
#def echange(cube,s1,s2):
#    [['A','a','X','c','d','D','g','G'],['P','x','S','t','v','J','r','M'],['H','f','W','m','l','U','u','O'],['B','d','F','i','p','L','s','R'],['E','h','H','o','n','Q','w','T'],['V','b','B','k','j','N','q','K']]=cube
import random

class Cube:
    def __init__(self, Faces):
        #Faces est un tableau de face de taille 6, chaque face est un objet qui contient 9 element couleur (entre 0 et 5)
        self.u = Face(Faces[0])
        self.d = Face(Faces[1])
        self.r = Face(Faces[2])
        self.l = Face(Faces[3])
        self.f = Face(Faces[4])
        self.b = Face(Faces[5])
    def __str__(self):
        return '________' + '\n' + str(self.u) + '\n\n' + str(self.l) + '\n\n' + str(self.f) + '\n\n' + str(self.r) + '\n\n' + str(self.d) + '\n\n' + str(self.b)
    def U(self):
        self.u.turnClock()
        temp = self.f.ul, self.f.uu, self.f.ur
        self.f.ul, self.f.uu, self.f.ur = self.r.ul, self.r.uu, self.r.ur
        self.r.ul, self.r.uu, self.r.ur = self.b.ul, self.b.uu, self.b.ur
        self.b.ul, self.b.uu, self.b.ur = self.l.ul, self.l.uu, self.l.ur
        self.l.ul, self.l.uu, self.l.ur = temp
    def U_(self):
        self.U()
        self.U()
        self.U()
    def U2(self):
        self.U()
        self.U()
    def D(self):
        self.d.turnClock()
        temp = self.f.dl, self.f.dd, self.f.dr
        self.f.dl, self.f.dd, self.f.dr = self.l.dl, self.l.dd, self.l.dr
        self.l.dl, self.l.dd, self.l.dr = self.b.dl, self.b.dd, self.b.dr
        self.b.dl, self.b.dd, self.b.dr = self.r.dl, self.r.dd, self.r.dr
        self.r.dl, self.r.dd, self.r.dr = temp
    def D_(self):
        self.D()
        self.D()
        self.D()
    def D2(self):
        self.D()
        self.D()
    def R(self):
        self.r.turnClock()
        temp = self.f.ur, self.f.rr, self.f.dr
        self.f.ur, self.f.rr, self.f.dr = self.d.ur, self.d.rr, self.d.dr
        self.d.ur, self.d.rr, self.d.dr = self.b.dl, self.b.ll, self.b.ul
        self.b.dl, self.b.ll, self.b.ul = self.u.ur, self.u.rr, self.u.dr
        self.u.ur, self.u.rr, self.u.dr = temp
    def R_(self):
        self.R()
        self.R()
        self.R()
    def R2(self):
        self.R()
        self.R()
    def L(self):
        self.l.turnClock()
        temp = self.f.ul, self.f.ll, self.f.dl
        self.f.ul, self.f.ll, self.f.dl = self.u.ul, self.u.ll, self.u.dl
        self.u.ul, self.u.ll, self.u.dl = self.b.dr, self.b.rr, self.b.ur
        self.b.dr, self.b.rr, self.b.ur = self.d.ul, self.d.ll, self.d.dl
        self.d.ul, self.d.ll, self.d.dl = temp
    def L_(self):
        self.L()
        self.L()
        self.L()
    def L2(self):
        self.L()
        self.L()
    def F(self):
        self.f.turnClock()
        temp = self.u.dl, self.u.dd, self.u.dr
        self.u.dl, self.u.dd, self.u.dr = self.l.dr, self.l.rr, self.l.ur
        self.l.dr, self.l.rr, self.l.ur = self.d.ur, self.d.uu, self.d.ul
        self.d.ur, self.d.uu, self.d.ul = self.r.ul, self.r.ll, self.r.dl
        self.r.ul, self.r.ll, self.r.dl = temp
    def F_(self):
        self.F()
        self.F()
        self.F()
    def F2(self):
        self.F()
        self.F()
    def B(self):
        self.b.turnClock()
        temp = self.u.ul, self.u.uu, self.u.ur
        self.u.ul, self.u.uu, self.u.ur = self.r.ur, self.r.rr, self.r.dr
        self.r.ur, self.r.rr, self.r.dr = self.d.dr, self.d.dd, self.d.dl
        self.d.dr, self.d.dd, self.d.dl = self.l.dl, self.l.ll, self.l.ul
        self.l.dl, self.l.ll, self.l.ul = temp
    def B_(self):
        self.B()
        self.B()
        self.B()
    def B2(self):
        self.B()
        self.B()
    def scramble(self,sequence):
        """sequence is a string of moves in the form URLFBU'R'B2 all attached"""
        #first split the sequence in its individual moves
        def splitSequence(sequence):
            finalList = []
            letters = ['U', 'D', 'R', 'L', 'F', 'B']
            currentValue = 'U'
            for i in range (len(sequence)-1):
                currentValue = sequence[i]
                if currentValue in letters :
                    if sequence[i+1] in letters:
                        finalList.append(currentValue)
                    else :
                        finalList.append(currentValue+sequence[i+1])
            #final element is treated apart for out of bounds issues
            if sequence[-1] in letters:
                finalList.append(sequence[-1])
            return finalList
        moves = splitSequence(sequence)
        #Then execute each move
        for move in moves:
            if move == "U":
                self.U()
            elif move == "U'":
                self.U_()
            elif move == "U2":
                self.U2()
            elif move == "D":
                self.D()
            elif move == "D'":
                self.D_()
            elif move == "D2":
                self.D2()
            elif move == "R":
                self.R()
            elif move == "R'":
                self.R_()
            elif move == "R2":
                self.R2()
            elif move == "L":
                self.L()
            elif move == "L'":
                self.L_()
            elif move == "L2":
                self.L2()
            elif move == "F":
                self.F()
            elif move == "F'":
                self.F_()
            elif move == "F2":
                self.F2()
            elif move == "B":
                self.B()
            elif move == "B'":
                self.B_()
            elif move == "B2":
                self.B2()
    def randomScramble(self, numberOfMoves = 21):
        moves = {0 : "U", 1 : "R", 2: "L",3:"D",4:"F",5:"B"}
        sequence =''
        printedSequence = ''
        lastMove = None
        currentMove = random.randint(0,5)
        for k in range (numberOfMoves):
            #il faut faire en sorte de ne pas bouger 2 fois de suite la meme face
            while currentMove == lastMove :
                currentMove = random.randint(0,5)
            lastMove = currentMove
            #on rajoute de manière aléatoire un demi tour ou un counterclockwise
            bonus = random.random()
            if bonus < 0.34:
                sequence += moves[currentMove]
                printedSequence += moves[currentMove]+ ' '
            elif bonus < 0.67:
                sequence += moves[currentMove]+"'"
                printedSequence += moves[currentMove]+ "' "
            else :
                sequence += moves[currentMove]+"2"
                printedSequence += moves[currentMove]+ '2 '
        self.scramble(sequence)
        return printedSequence




class Face:
        def __init__(self, colors):
            """colors est une liste de taille 9"""
            if len(colors) == 9:
                #on donne uen couleur à chaque facette de haut en gauche à en bas à droite
                #le 'haut' est pris avec la face blanche vers le haut pour rflb et rouge en bas pour u et rouge en haut pour d
                self.ul = colors[0]
                self.uu = colors[1]
                self.ur = colors[2]
                self.ll = colors[3]
                self.center = colors[4]
                self.rr = colors[5]
                self.dl = colors [6]
                self.dd = colors [7]
                self.dr = colors [8]
                #on donne aussi un attribut par ligne et colonne pour simplifier les déplacements ensuite
                self.u = [self.ul,self.uu,self.ur]
                self.e = [self.ll,self.center,self.rr]
                self.d = [self.dl,self.dd,self.dr]
                self.l = [self.ul,self.ll,self.dl]
                self.m = [self.uu,self.center,self.dd]
                self.r = [self.ur,self.rr,self.dr]

            else:
                print('Erreur, une face a 9 facettes !')
        def __str__(self):
            return str(self.ul) + str(self.uu) + str(self.ur) + '\n' + str(self.ll) + str(self.center) +str(self.rr)+ '\n' + str(self.dl)+str(self.dd)+str(self.dr)
            #return str(self.u) + '\n' +str(self.e) + '\n' +str(self.d)
        def turnClock(self):
            tempEdges = self.uu
            tempCorner = self.ul
            #on fait tourner les arêtes
            self.uu = self.ll
            self.ll = self.dd
            self.dd = self.rr
            self.rr = tempEdges
            #pareil pour les coins
            self.ul = self.dl
            self.dl = self.dr
            self.dr = self.ur
            self.ur = tempCorner
        def __getitem__(self, item):
            if item == 0:
                return self.ul
            if item == 1 :
                return self.uu
            if item == 2:
                return self.ur
            if item == 3:
                return self.ll
            if item == 4 :
                return self.center
            if item == 5:
                return self.rr
            if item == 6:
                return self.dl
            if item == 7 :
                return self.dd
            if item == 8:
                return self.dr
        def __len__(self):
            return 9


def salut():
    print("oui")
newFace = Face ([0,0,0,1,1,1,2,2,2])
#print(newFace)
#print(newFace.u)
newCube = Cube([ [i,i,i,i,i,i,i,i,i] for i in range (6)])
#print(newFace[6])
#print(newCube)
newCube.U()
newCube.randomScramble()
print(newCube)
