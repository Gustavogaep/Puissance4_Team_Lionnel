def Match_nul(grille):
    """ fonction permettant a Python de determiner si le match est nul ou pas
    """
    a = False
    for i in range(6):
        if grille[i][index_colonne] != 0:
            a = True
        else:
            a = False
    return grille
    
