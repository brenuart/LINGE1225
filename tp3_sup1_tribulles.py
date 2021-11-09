def tribulles(l):
    # comme le dit l'énoncé, on doit recommencer les comparaisons de tous les
    # éléments du tableau n-1
    #
    n = len(l)
    for j in range(0, n-1):
        # on compare chaque element de la liste avec le suivant, en commencant par le premier
        # attention que il faut s'arreter avant le dernier element de la liste. En effet,
        # l'avant-dernier est comparé avec le dernier... -> cfr indice "i" utilisé pour accéder
        # à l'élément...
        for i in range(0, n-1):  # attention - cfr tableau en dessous
            if l[i] > l[i + 1]:
                temp = l[i + 1]
                l[i + 1] = l[i]
                l[i] = temp

    return l

# --------------------------------------------------------
print(tribulles([1,5,2,3]))

# [ 1 ,  2 ,  3 ,  4]   ^
#   0    1    2    3    |
# l[0] l[1] l[2] l[3]  l[4]

