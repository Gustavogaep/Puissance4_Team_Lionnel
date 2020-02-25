from random import randint
def Ai_vs_ai_aleatoire():
    """partie jouer entre deux IA
    """
    grille = grille_vide()
    while Victoire(grille, 1) or Victoire(grille, 2) != True:
        Coup_aleatoire(grille, 1)
        if Victoire(grille, 1) == True:
            print("L'Ai numéro 1 a gagné !")
            break
        elif:
            Match_nul(grille, 1) == True:
            print("Il y a match nul")
            break
        Coup_aleatoire(grille, 2)
        if Victoire(grille, 2) == True:
            print("L'Ai numéro 2 a gagné !")
            break
        elif:
            Match_nul(grille, 2) == True:
            print("Il y a match nul")
            break
