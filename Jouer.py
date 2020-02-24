def jouer(grille, numero_joueur, index_colonne):
    if numero_joueur == 1:
        for i in range(6):
            if grille[i][index_colonne] == 0:
                grille[i][index_colonne] == numero_joueur
                break
    if numero_joueur == 2:
        for i in range(6):
            if grille[i][index_colonne] == 0:
                grille[i][index_colonne] == numero_joueur
                break
    return grille



