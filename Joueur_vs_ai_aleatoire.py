from random import randint
def Joueur_vs_ai_aleatoire():
    """Fonction permettant a un joueur de jouer au Puissance 4 contre une IA
    """
    grille = Grille_vide()
    pion = int(input("Quel pion voulez vous choisir: \nX\nO\n"))
    numero_joueur = 0
    a = "Le joueur a gagné !"
    b = "L'IA a gagné !"
    c = "C'est un match nul !"

    if pion == "X" or pion == "x":
        numero_joueur = 1
        numero_IA = 2
    elif pion == "O" or pion == "o":
        numero_joueur = 2
        numero_IA = 1
    Affiche_grille(grille)
    while Victoire(grille, 1) or Victoire(grille, 2) != True:
        print("\nVotre tour!\n")
        choix = int(input("Quelle colonne choisissez vous ?"))
        if Coup_possible(grille, choix) == True:
            coup_joueur(grille, numero_joueur, choix)
        if Match_nul(grille) == True:
            print(c)
            break 
        if Victoire(grille, numero_joueur) == True:
            print (a)
            break
        if Coup_possible(grille, randint(0,6):
            Coup_aleatoire(grille, numero_IA)
        if Match_nul(grille) == True:
            print(c)
            break
        if Victoire(grille,numero_IA)==True:
            print(b)
            break
        
    




       
