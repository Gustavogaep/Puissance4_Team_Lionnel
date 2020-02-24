def jouer(grille, numero_joueur, index_colonne):
    if coup_possible(grille, index_colonne) == True:
        if numero_joueur == 1:
            for i in range(6):
                if grille[i][index_colonne] == 0:
                    grille[i][index_colonne] += 1
                    break
        if numero_joueur == 2:
            for i in range(6):
                if grille[i][index_colonne] == 0:
                    grille[i][index_colonne] += 2
                    break
    Affiche_grille(grille)
    return grille

