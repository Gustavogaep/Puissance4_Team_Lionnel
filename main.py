def Main():
    """ Fonction principale qui permet de choisir entre 2 modes de jeux:
    le mode de jeu Ai contre Ai, le mode de jeu Joueur contre Ai et le mode joueur contre joueur.
    """
    print("(1)---> Le mode de jeu Ai contre Ai.")
    print("(2)---> Le mode de jeu Joueur contre Ai.")
    print("(3)---> Le mode de jeu est Joueur contre Joueur.")
    try:
        choix = int(input("Choisissez un mode de jeu:"))
    except ValueError:
        print(f"Le choix {choix} est invalide, réessayez.")
        return None
    if choix == 1:
        Ai_vs_ai_aleatoire()
    elif choix == 2:
        Joueur_vs_ai_aleatoire()
    elif choix == 3:
        Joueur_vs_joueur()
    else:
        print(f"Le choix {choix} est invalide, réessayez.")
        Main()
