def coup_joueur(grille, numero_joueur, index_colonne):
    """fonction permettant au joueur de jouer un coup
    """
    if Coup_possible(grille, index_colonne) == True:
        return(jouer(grille, numero_joueur, index_colonne))
    else:
        coup_joueur(grille, numero_joueur, index_colonne)

    


