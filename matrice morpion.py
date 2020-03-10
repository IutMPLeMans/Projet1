import numpy as np
def grille(grille):
    a= np.ones((3,3),np.uint8)
    print (a)
    
def gagne(grille):
    if (a[0,:].all() or a[1,:].all() or a[2,:].all() or a[:,0].all() or a[:,1].all() or a[:,2].all())==1    or   a[0,0]==a[1,1]==a[2,2]    or   a[0,2]==a[1,1]==a[2,0]:
        return 1
def nul(grille):
    for i in range(9):
        if grille[i]==1:
            return 0
        return 1

def jeu(grille):
    condition= False
    tableau=grille(grille)
    k=0
    while condition== False:
        k=k+1
        if k%2==0:
            print("C'est au tour du joueur 2")
            print(tableau)
            ligne=input("Choisir une ligne: ")
            colonne=input("Choisir une colonne: ")
            if tableau[[int(ligne)],[int(colonne)]]==0 or ligne>3 or colonne>3:
                condition= True
                tableau[[int(ligne)],[int(colonne)]]=tableau[int(ligne)],[int(colonne)]+1
            else:
                print(" cette case est impossible à selectionner veuillez en choisir une autre")
        else:
            print("C'est au tour du joueur 1")
            print(tableau)
            ligne=input("Choisir une ligne: ")
            colonne=input("Choisir une colonne: ")
            if tableau[[int(ligne)],[int(colonne)]]==0 or ligne>3 or colonne>3:
                condition= True
                tableau[[int(ligne)],[int(colonne)]]=tableau[int(ligne)],[int(colonne)]-1
            else:
                print(" cette case est impossible à selectionner veuillez en choisir une autre")
    condition=False

gagne= False
while gagne==False:
    jeu(grille)
    if nul(grille):
        print("Matche Nul")
        gagne=True
    elif gagne(grille):
        if 0==gagne(grille):
            print("le joueur 1 à gagné!")
        elif 1==gagne(grille):
            print("le joueurs 2 à gagné!")
    gange=True
    
    


