
def average(mat):
    # Input:
    # - colonne -> personne
    # - ligne   -> soirée
    # - valeur: nombre de bières bues par la personne durant la soirée

    nbSoiree = len(mat)
    nbPersonne = len(mat[0])

    # Calcul de la moyenne de chaque personne
    #
    moyenneParPersonne = [0] * nbPersonne
    for s in range(nbSoiree):
        soiree = mat[s] # "soiree" est donc une liste des bières bues par chaque personne (première valeur = personne 0)

        for p in range(nbPersonne):
            moyenneParPersonne[p] += soiree[p] / nbSoiree


    # Calcul de la moyenne des bieres bues lors de chaque soiree
    #
    moyenneParSoiree = [0] * nbSoiree
    for s in range(nbSoiree):
        soiree = mat[s] # "soiree" est donc une liste des bières bues par chaque personne (première valeur = personne 0)

        for p in range(nbPersonne):
            moyenneParSoiree[s] += soiree[p] / nbPersonne


    return [moyenneParPersonne, moyenneParSoiree]

# ----------------------
# Les deux boucles "extérieures" sont similaires -> on peut les regrouper
#
def average2(mat):
    # Input:
    # - colonne -> personne
    # - ligne   -> soirée
    # - valeur: nombre de bières bues par la personne durant la soirée

    nbSoiree = len(mat)
    nbPersonne = len(mat[0])

    moyenneParPersonne = [0] * nbPersonne
    moyenneParSoiree = [0] * nbSoiree
    for s in range(nbSoiree):
        soiree = mat[s] # "soiree" est donc une liste des bières bues par chaque personne (première valeur = personne 0)

        # Moyenne par personne
        for p in range(nbPersonne):
            moyenneParPersonne[p] += soiree[p] / nbSoiree

        # Moyenne par soiree
        for p in range(nbPersonne):
            moyenneParSoiree[s] += soiree[p] / nbPersonne

    return [moyenneParPersonne, moyenneParSoiree]


# ----------------------
# Les deux boucles "interieures" sont similaires -> on peut les regrouper
#
def average3(mat):
    # Input:
    # - colonne -> personne
    # - ligne   -> soirée
    # - valeur: nombre de bières bues par la personne durant la soirée

    nbSoiree = len(mat)
    nbPersonne = len(mat[0])

    moyenneParPersonne = [0] * nbPersonne
    moyenneParSoiree = [0] * nbSoiree
    for s in range(nbSoiree):
        soiree = mat[s] # "soiree" est donc une liste des bières bues par chaque personne (première valeur = personne 0)

        for p in range(nbPersonne):
            # Moyenne par personne
            moyenneParPersonne[p] += soiree[p] / nbSoiree

            # Moyenne par soiree
            moyenneParSoiree[s] += soiree[p] / nbPersonne

    return [moyenneParPersonne, moyenneParSoiree]


# ----------------------
# Propagation des erreurs: le calcul des moyennes est pas "top" -> mieux vaut faire la somme totale et diviser par le
# nombre de valeur une fois la somme obtenue
#
def average4(mat):
    # Input:
    # - colonne -> personne
    # - ligne   -> soirée
    # - valeur: nombre de bières bues par la personne durant la soirée

    nbSoiree = len(mat)
    nbPersonne = len(mat[0])

    moyenneParPersonne = [0] * nbPersonne
    moyenneParSoiree = [0] * nbSoiree
    for s in range(nbSoiree):
        soiree = mat[s] # "soiree" est donc une liste des bières bues par chaque personne (première valeur = personne 0)

        for p in range(nbPersonne):
            # Moyenne par personne
            moyenneParPersonne[p] += soiree[p]

            # Moyenne par soiree
            moyenneParSoiree[s] += soiree[p]

    # Conversion des totaux en moyennes
    #
    for p in range(nbPersonne):
        moyenneParPersonne[p] = moyenneParPersonne[p] / nbSoiree
    for s in range(nbSoiree):
        moyenneParSoiree[s] = moyenneParSoiree[s] / nbPersonne

    return [moyenneParPersonne, moyenneParSoiree]

# ----------------------
mat = [[2,4,6,8], [1,3,5,7]]
print(average4(mat))
