def demiSomme(data):
    # Le résultat est une liste de taille égale au nombre de lignes.
    # Le nombre de lignes est donné par "len(l)".
    # L'élément "0" de la liste resultat contient la somme de la ligne "0".
    #
    result = [0 for j in range(len(l))]

    # On itère sur chaque ligne de la matrice...
    # "i" contient donc l'indice de la ligne dans la matrice.
    #
    for i in range(len(l)):
        # On vérifie que la matric est carrée, càd que chaque ligne contient autant
        # d'éléments qu'il y a de colonnes. Et le nombre de colonnes c'est le nombre d'éléments de "l"...
        # Pour rappel, "l" (la matrice) est une liste de listes...
        #
        if len(l[i]) != len(l):
            return None

        # Calcul de la somme des éléments de la ligne. Il suffit donc d'itérer sur les valeurs de la ligne, càd les
        # valeurs de la liste[i] en commencant par l'élément "i".
        #
        somme = 0
        for j in range(i, len(l[i])):
            somme += l[i][j]

        # Maintenant qu'on a la somme pour la ligne "i", on stocke la valeur dans le résultat à la position "i".
        #
        result[i] = somme

    return result


# -----------------------------------------------------------------------
# Variante.
# L'algorithme est le même avec quelques "simplifications" (non obligatoires)...
#
def demiSomme2(l):
    # Variante:
    #   Pas besoin d'initialiser la liste à la taille finale. On peut se contenter d'une liste initialement vide et
    #   faire un "append()" des valeurs successives.
    #
    result = []

    # Variante:
    #   On utilise "len(l)" à plusieurs reprises pour faire référence au nombre de lignes.
    #   Pourquoi ne pas stocker cette valeur dans une variable et y faire référence à chaque fois?
    #   --> le nom de la variable indique clairement de quoi il s'agit ce qui peut faciliter la compréhension
    #       du reste de l'algorithme.
    #
    nbLignes = len(l)

    for i in range(nbLignes):
        # Variante:
        #   "l[i]" est la ligne courante sur laquelle on travaille. Pourquoi ne pas la "nommer" et utiliser une
        #   variable pour y faire référence. De cette manière "ligne[0]" représente le premier élément de la ligne
        #   courante - c'est parfois plus compréhensible que se demander à quoi correspond "l[i][j]"...
        #
        ligne = l[i]

        if len(ligne) != nbLignes:
            return None

        # Variante:
        #   La solution précédente accède aux valeurs de la ligne via leur "indice" (variable "j"). Dans le cas présent
        #   nous n'avons pas besoin de connaître la position de la valeur de la ligne. On peut donc itérer sur les
        #   valeurs silmplement et se passer de l'indice ce qui simplifie la lecture du programme.
        #
        somme = 0
        for j in range(i, nbLignes):
            somme += ligne[j]

        result.append(somme)

    return result


# -----------------------------

def test(input, expected):
    actual = demiSomme2(input)

    print("demiSomme(", input, ") => ", actual)

    if actual != expected:
        print("Erreur! Expected: ", expected)

test(
[
    [1,3,5],
    [2,7,3],
    [9,1,8]
] , [9,10,8])

test([[1], [1,2], [1,2,3]], None)
