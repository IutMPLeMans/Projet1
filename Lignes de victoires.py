##Création d'une matrice test
#import numpy as np
#a=np.ones((3,3),np.uint8)
#print(a)

##Définition des lignes de victoires
#if (a[0,:].all() or a[1,:].all() or a[2,:].all() or a[:,0].all() or a[:,1].all() or a[:,2].all())==1    or   a[0,0]==a[1,1]==a[2,2]    or   a[0,2]==a[1,1]==a[2,0]:
#    print("gagne")

##Remplissage de la matrice
#if joueur==1 :
#	grille[int(colonne)+int(ligne)*3]="X"
#	if joueur==2 :
#		grille[int(colonne)+int(ligne)*3]="O"
#    afficher_grille(grille)

#Définition des lignes de victoires
def est_gagnant(grille):
    if (grille[0]==grille[1]) and (grille[0]==grille[2]) and (grille[0]==("X" or "O")):
        return 1
    if (grille[3]==grille[4]) and (grille[3]==grille[5]) and (grille[3]==("X" or "O")):
        return 1
    if (grille[6]==grille[7]) and (grille[6]==grille[8]) and (grille[6]==("X" or "O")):
        return 1
    if (grille[0]==grille[3]) and (grille[0]==grille[6]) and (grille[0]==("X" or "O")):
        return 1
    if (grille[1]==grille[4]) and (grille[1]==grille[7]) and (grille[1]==("X" or "O")):
        return 1
    if (grille[2]==grille[5]) and (grille[2]==grille[8]) and (grille[2]==("X" or "O")):
        return 1
    if (grille[0]==grille[4]) and (grille[0]==grille[8]) and (grille[0]==("X" or "O")):
        return 1
    if (grille[2]==grille[4]) and (grille[2]==grille[6]) and (grille[2]==("X" or "O")):
        return 1

