# Première approche...
#
def estMagique(mat):
    # Vérifier que la matric est carrée.
    # Le nombre de lignes et donné par "len(mat)".
    # On itère sur chaque ligne et on vérifie que la taille de la ligne est égale au nombre de lignes...
    #
    nbLignes = len(mat)
    for ligne in mat:
        if len(ligne) != nbLignes:
            return False

    # Calcul de la somme de chaque LIGNE.
    #
    # On va itérer sur chaque ligne, en calculer la somme et si la somme est différente de la précédente on peut
    # s'arrêter immédiatement - pas besoin de calculer les colonnes ni les diagonales...
    # Il faut donc se souvenir de "la somme précédente" et "la somme de la ligne courante". Par exemple:
    #
    #    previousSomme = 0
    #    sommeLigne = <... calcul de la somme de la ligne courante...>
    #    if sommeLigne != previousSomme:
    #        return False
    #
    # Ok, mais on a un soucis pour la première ligne: il n'y a pas encore de "somme précédente" et il y a donc de fortes
    # chances que la condition du IF soit False dès la première itération (sauf si par chance la somme de la première
    # ligne soit égale à "0" - la valeur d'initialisation utilisée). On a donc besoin d'un moyen pour savoir qu'il n'y
    # a pas encore de somme précédente. Différentes stratégies:
    # - on pourrait initialiser "previousSomme=-1" pour indique "une absence de valeur" - mais cela ne fonctionne que si
    #   toutes les valeurs de la matric sont positives (aucune somme ne sera donc égale à -1)
    # - on pourrait initialiser "previousSomme=None" - c'est mieux
    # - on peut aussi simplement se baser sur le "numéro de la ligne" (l'indice du FOR) - si c'est 0 (càd la première
    #   ligne), on sait qu'il ne peut pas y avoir de somme précédente et on n'effectue pas la comparaison... Dans ce
    #   cas, peut importe la valeur d'initialisatio de "previousSomme".
    #
    # La dernière approche est la plus naturelle.
    #
    previousSomme = 0

    # On itère sur les lignes...
    for l in range(nbLignes):
        somme = 0

        # On itère sur les valeurs de la ligne...
        for v in mat[l]:
            somme += v

        if l == 0:
            previousSomme = somme

        if somme != previousSomme:
            return False


    # Si on arrive ici on sait que toutes les lignes ont la même somme et que cette somme se trouve dans "previousSomme".
    # On peut donc faire la même chose sur les colonnes. Cette fois nous n'avons plus le problème de savoir si
    # "previousSomme" a déjà été calculé ou pas...
    #
    # Note: il s'agit d'un carré - donc nb lignes == nb colonnes...
    #
    for c in range(nbLignes):
        somme = 0
        for l in range(nbLignes):
            somme += mat[l][c]

        if somme != previousSomme:
            return False


    # Les colonnes et les lignes sont ok - calcul des deux diagonales.
    # La première diagonale est composée des éléments mat[0][0], mat[1][1], ... mat[i][i]
    #
    somme = 0
    for l in range(nbLignes):
        somme += mat[l][l]

    if somme != previousSomme:
        return False


    # La seconde diagonale est composée des éléments mat[0][nbLignes-0-1], mat[1][nbLignes-1-1], ... mat[i][nbLignes-1-i]
    #
    somme = 0
    for l in range(nbLignes):
        somme += mat[l][nbLignes-1-l]

    if somme != previousSomme:
        return False


    # Si on arrive ici, c'est que toutes les sommes sont les mêmes...
    #
    return True


# -------------------------------------------------------------------------
# Alternative
#
# Dans la première solution nous avions un petit problème pour savoir si "previousSomme" avait déjà été calculée ou pas.
# On pourrait éviter cette question en commencant par calculer une des diagonales au lieu des lignes...
#
def estMagique2(mat):
    # Vérifier que c'est un carré
    #
    nbLignes = len(mat)
    for l in range(nbLignes):
        if len(mat[l]) != nbLignes:
            return False


    # Calcul d'une première diagonale. On se souvient de la somme qui servira de comparaison pour les autres...
    #
    somme = 0
    for l in range(nbLignes):
        somme += mat[l][l]

    previousSomme = somme

    #
    # On peut ensuite poursuivre avec la seconde diagonale ou les lignes/colonnes (au choix)...
    #

    # La dernière diagonale...
    #
    somme = 0
    for l in range(nbLignes):
        somme += mat[l][nbLignes-1-l]

    if somme != previousSomme:
        return False


    # Somme sur les lignes...
    for l in range(nbLignes):
        somme = 0
        for v in mat[l]:
            somme += v

        if somme != previousSomme:
            return False


    # Somme sur les colonnes...
    for c in range(nbLignes):
        somme = 0
        for l in range(nbLignes):
            somme += mat[l][c]

        if somme != previousSomme:
            return False


    # Si on arrive ici, c'est que toutes les sommes sont les mêmes...
    #
    return True


# -------------------------------------------------------------------------
# Alternative
#
# On remarque que nous avons plusieurs boucles similaires: elles itèrent toutes sur les lignes...
# On pourrait donc les regrouper en une seule boucle dans laquelle on fait plusieurs choses.
# La logique reste la même - il s'agit d'une optimisation (on évite de parcourir plusieurs fois les lignes) - au
# détriment parfois  de la lisibilité de la solution.
#
# (exercice laissé au lecteur si il le souhaite)
#

# -----------------------------

def test(input, expected):
    actual = estMagique(input)

    print(input, " => ", actual)

    if actual != expected:
        print("Erreur! Expected: ", expected)


test([[4,9,2],[3,5,7],[8,1,6]], True)
test([[4,9,2],[1,2],[1]], False)  # Ce n'est pas un carré...
