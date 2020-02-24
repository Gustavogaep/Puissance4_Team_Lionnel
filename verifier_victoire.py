def verifier_victoire_horizontale(grille, numero_joueur, index_ligne, index_colonne):
    a = 0
    t = False
    for i in range(len(grille[index_colonne])):
        if grille[index_colonne][i] == numero_joueur:
            a +=1
            if a == 4:
                t = True
        else:
            a = 0
    return t

def verifier_victoire_vertical(grille, numero_joueur, index_ligne, index_colonne):
    a = 0
    t = False
    for i in range(len(grille[index_ligne])):
        if grille[index_ligne][i] == numero_joueur:
            a +=1
            if a == 4:
                t = True
        else:
            a = 0
    return t
