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
        if  self.p[l][c]==0 and l<self.ligne and c<self.colonne:          #'c' et 'l' servent à situer la cellule de la matrice, 'ligne' et 'colonne' sont la taille de la matrice
            return True
        else:
            return False

    def set1(self,l,c):
        self.p[l][c]=2
    def set2(self,l,c):
        self.p[l][c]=1

    def est_gagnant(self,p):
        if (self.p[0]==self.p[1]) and (self.p[0]==grille[2]) and (self.p[0]==("X" or "O")):
            return True
        if (self.p[3]==self.p[4]) and (self.p[3]==self.p[5]) and (self.p[3]==("X" or "O")):
             return True
        if (self.p[6]==self.p[7]) and (self.p[6]==self.p[8]) and (self.p[6]==("X" or "O")):
             return True
        if (self.p[0]==self.p[3]) and (self.p[0]==self.p[6]) and (self.p[0]==("X" or "O")):
             return True
        if (self.p[1]==self.p[4]) and (self.p[1]==self.pe[7]) and (self.p[1]==("X" or "O")):
             return True
        if (self.p[2]==self.p[5]) and (self.p[2]==self.p[8]) and (self.p[2]==("X" or "O")):
             return True
        if (self.p[0]==self.p[4]) and (self.p[0]==self.p[8]) and (self.p[0]==("X" or "O")):
             return True
        if (self.p[2]==self.p[4]) and (self.p[2]==self.p[6]) and (self.p[2]==("X" or "O")):
             return True


    def nul(self):
        for i in range(9):
            if self.p[i]==1:
                return 0
        return 1

    def jouer(self):
        condition= False
        x=3
        jeu=Plateau(x,x)
        k=0
        while condition== False:
            k=k+1
            if k%2==0:
                print("C'est au tour du joueur 2")
                print(self.p)
                l=int(input("Choisir une ligne: "))
                c=int(input("Choisir une colonne: "))
                if self.caselibre(l,c) :
                    self.set1(l,c)
                else:
                    print(" cette case est impossible à selectionner veuillez en choisir une autre")
            else:
                print("C'est au tour du joueur 1")
                print(self.p)
                l=int(input("Choisir une ligne: "))
                c=int(input("Choisir une colonne: "))
                if self.caselibre(l,c)== True:
                    self.set2(l,c)
                else:
                    print("Cette case est impossible à selectionner veuillez en choisir une autre")
        condition=False

gagne= False
a=Plateau(3,3)
ch=Plateau(3,3)
ok=Plateau(3,3)
while gagne==False:
    a.jouer()
    if ch.nul():
        print("Matche Nul")
        gagne=True
    elif ok.gagne(self):
        if "O"==ok.gagne(self):
            print("le joueur 1 à gagné!")
        elif "X"==ok.gagne(self):
            print("le joueurs 2 à gagné!")
    gagne=True
    
    


