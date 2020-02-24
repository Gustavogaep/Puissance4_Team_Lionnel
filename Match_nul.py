def Match_nul(grille):
    a = False
    for i in range(6):
        if grille[i][index_colonne] != 0:
            a = True
        else:
            a = False
    return grille
    