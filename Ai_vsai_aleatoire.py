from random import randint
def Ai_vs_ai_aleatoire():
    """partie jouer entre deux IA
    """
    while:   
        if Coup_possible(grille, index_colonne) == True:
            return Coup_aleatoire(grille, numero_joueur)
        else:
            Coup_possible(grille, index_colonne) == False
        if Match_nul(grille) == True:
            break
        else:
            pass
    Victoire(grille, numero_joueur)
    return grille