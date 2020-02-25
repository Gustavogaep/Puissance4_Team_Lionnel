def Victoire(grille, numero_joueur):
    """ fonction permettant de determiner si il y a victoire ou pas
    """
    if Verifier_victoire_horizontale(grille, numero_joueur, index_ligne, index_colonne) or Verifier_victoire_verticale(grille, numero_joueur, index_ligne, index_colonne) or Verifier_victoire_diagonale(grille, numero_joueur, index_ligne, index_colonne) == True:
        return True
    else:
        return False
