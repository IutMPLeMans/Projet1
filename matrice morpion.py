import numpy as np
class Plateau:
    def __init__(self,ligne,colonne):          #Initialisation du plateau de jeu
        self.ligne= ligne
        self.colonne= colonne
        self.p = np.zeros((ligne,colonne),np.int32)
 #convertion pour afficher la matrice
    def __repr__(self):
        return np.array_str(self.p)
    def caselibre(self,l,c):
        condition= False
        if  self.p[l][c]==0 and l>ligne and c>colonne:          #'c' et 'l' sont la taille de la matrice, 'ligne' et 'colonne' servent à situer la cellule de la matrice
            return True

        return False

    def set1(self,l,c):
        self.p[l][c]=="X"
    def set2(self,l,c):
        self.p[l][c]=="O"

    def est_gagnant(self):
        if (self.p[0]==self.p[1]) and (self.p[0]==grille[2]) and (self.p[0]==("X" or "O")):
            return 1
        if (self.p[3]==self.p[4]) and (self.p[3]==self.p[5]) and (self.p[3]==("X" or "O")):
            return 1
        if (self.p[6]==self.p[7]) and (self.p[6]==self.p[8]) and (self.p[6]==("X" or "O")):
            return 1
        if (self.p[0]==self.p[3]) and (self.p[0]==self.p[6]) and (self.p[0]==("X" or "O")):
            return 1
        if (self.p[1]==self.p[4]) and (self.p[1]==self.pe[7]) and (self.p[1]==("X" or "O")):
            return 1
        if (self.p[2]==self.p[5]) and (self.p[2]==self.p[8]) and (self.p[2]==("X" or "O")):
            return 1
        if (self.p[0]==self.p[4]) and (self.p[0]==self.p[8]) and (self.p[0]==("X" or "O")):
            return 1
        if (self.p[2]==self.p[4]) and (self.p[2]==self.p[6]) and (self.p[2]==("X" or "O")):
            return 1


    def nul(self):
        for i in range(9):
            if self.p[i]==1:
                return 0
        return 1

    def jeu(self):
        condition= False
        jeu=Plateau(9,9)
        k=0
        while condition== False:
            k=k+1
            if k%2==0:
                print("C'est au tour du joueur 2")
                print(jeu)
                ligne=int(input("Choisir une ligne: "))
                colonne=int(input("Choisir une colonne: "))
                if jeu.caselibre(l,c) :
                    jeu.set1(l,c)
                else:
                    print(" cette case est impossible à selectionner veuillez en choisir une autre")
            else:
                print("C'est au tour du joueur 1")
                print(jeu)
                ligne=input("Choisir une ligne: ")
                colonne=input("Choisir une colonne: ")
                if jeu.caselibre(l,c) :
                    jeu.set2(l,c)
                else:
                    print(" cette case est impossible à selectionner veuillez en choisir une autre")
        condition=False
        print(jeu)

gagne= False
while gagne==False:
    jeu(self)
    if nul(self):
        print("Matche Nul")
        gagne=True
    elif gagne(self):
        if 0==gagne(self):
            print("le joueur 1 à gagné!")
        elif 1==gagne(slef):
            print("le joueurs 2 à gagné!")
    gange=True
    
    


