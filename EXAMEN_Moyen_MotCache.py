# Note:
#   Cette solution est "identique" au correctif proposé par le professeur...
#   ... il suffit de replacer/copier le contenu des différentes "sous" méthodes
#   dans les boucles "for" où elles sont utilisées ci-dessous.
#
def motCache(grille, mot):
    # dimensions de la grille
    #
    nbLignes = len(grille)
    nbColonnes = len(grille[0]) # Attention: cas de la grille vide...?

    # Recherche du mot sur les lignes (ligne par ligne)
    #
    for numLigne in range(nbLignes):
        if ligneContientMot(grille, numLigne, mot):
            return True

    # Recherche du mot sur les colonnes (colonne par colonne)
    #
    for numColonne in range(nbColonnes):
        if colonneContientMot(grille, numColonne, mot):
            return True

    # Pas trouvé...
    #
    return False

def ligneContientMot(grille, numLigne, mot):
    ligne = grille[numLigne]
    for startPos in range(len(ligne)-len(mot)+1):
        if ligneContientMotAtPos(grille, numLigne, mot, startPos):
            return True
    return False

def ligneContientMotAtPos(grille, numLigne, mot, startPos):
    for i in range(len(mot)):
        if grille[numLigne][startPos+i] != mot[i]:
            return False
    return True

def colonneContientMot(grille, numColonne, mot):
    for startPos in range(len(grille)-len(mot)+1):
        if colonneContientMotAtPos(grille, numColonne, mot, startPos):
            return True
    return False

def colonneContientMotAtPos(grille, numColonne, mot, startPos):
    for i in range(len(mot)):
        if grille[startPos+i][numColonne] != mot[i]:
            return False
    return True

# -------------------------------------------------
grille = [
    [ "B", "A", "B", "A", "B", "A", "S" ],
    [ "N", "X", "B", "A", "T", "R", "A" ],
    [ "V", "P", "Y", "T", "H", "O", "N" ],
    [ "J", "M", "A", "T", "L", "A", "B" ],
    [ "A", "A", "C", "I", "S", "A", "B" ],
    [ "V", "L", "I", "S", "P", "B", "L" ],
    [ "A", "P", "A", "S", "C", "V", "L" ],
    [ "F", "R", "V", "T", "A", "G", "H" ]
]
print(motCache(grille, "JAVA"))   # true
print(motCache(grille, "PYTHON")) # true
print(motCache(grille, "BABAS"))  # true
print(motCache(grille, "BASIC"))  # false
print(motCache(grille, "VBA"))    # false


