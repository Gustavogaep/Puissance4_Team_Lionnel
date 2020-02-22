def Coup_possible(grille, index_colonne):
    if grille[0][index_colonne] == 0:
        pas_vide = True
    else:
        pas_vide = False
    return pas_vide
        
