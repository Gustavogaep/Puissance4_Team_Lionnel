from random import randint
def Coup_aleatoire(grille, numero_joueur):
    """ Fonction permettant de jouer un coup de manière aléatoire
    """
    aleatoire = randint(0,6)
    return(Jouer(grille,numero_joueur,aleatoire))
