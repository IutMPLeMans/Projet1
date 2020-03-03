import numpy as np
a= np.ones((3,3),np.uint8)
print (a)
k=0
while k<9:
    #joueur 1 
    print("le joueur 1 joue !")
    ligne=input("Choisir une ligne :" )
    colonne= input("choisir une colonne :")
    print("Vous avez joué la case ("+ligne+","+colonne+")")
    a[[int(ligne)],[int(colonne)]]= a[[int(ligne)],[int(colonne)]]+1
    print (a)
    #joueur 2
    print("c'est au tour du 2eme joueur")
    ligne=input("Choisir une ligne :" )
    colonne= input("choisir une colonne :")
    print("Vous avez joué la case ("+ligne+","+colonne+")")
    a[[int(ligne)],[int(colonne)]]= a[[int(ligne)],[int(colonne)]]-1
    print (a)
    k=k+1

