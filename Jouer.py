def jouer(grille, numero_joueur, index_colonne):
    """ Fonction permettant de jouer un pion correspondant a "1" lorsque vous êtes le joueur 1 et "2" lorsque vous êtes le joueur 2
    """
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



