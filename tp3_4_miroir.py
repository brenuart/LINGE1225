def miroir(mot):
    result = ""
    for c in mot:
        result = c + result
    return result


# Pour le fun... la même chose mais pour une liste -> il s'agit donc de créer une nouvelle liste
# inverse de la liste "l" donnée comme argument à la fonction
#
# Voici ce qui se passe à l'exécution:
#       l (liste originale)   result
# ------------------------------------
# i=0   [10,20,30,40,50]      []
# i=1   [10,20,30,40,50]      [10]
# i=2   [10,20,30,40,50]      [20, 10]
# i=3   [10,20,30,40,50]      [30, 20, 10]
# etc
def listeInverse(l):
    result = []
    for i in range(0, len(l)-1]:
        result[len(l)-i] = l[i]

    # ou bien...
    #for i in l:
    #    result.insert(i, 0)

    return result


# --------------------------------------------------------
print(miroir("Tp3 LINGE1225"))
