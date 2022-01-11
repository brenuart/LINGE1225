
def predict(lst, mot):
    counts = {}

    for i in lst:
        words = i.split(" ")

        for j in range(len(words) - 1):
            # Est-ce que le mot courant est celui qu'on cherche?
            if words[j] == mot:
                motSuivant = words[j+1]

                # On incremente le compteur pour le mot suivant
                if motSuivant not in counts:
                    counts[motSuivant] = 1
                else:
                    counts[motSuivant] += 1

    return counts

# --------------------------------------------------------------------

lst = [
    "bonjour, j'écris un message",
    "un message a été écrit",
    "un oiseau est venu se poser sur un arbre"
]
print(predict(lst, "un"))


cas_particuliers = [
    # gotcha: le "mot" est suivi par le "mot"...
    "un un deux",

    # gotcha: le mot recherché est à la fin
    "trois deux un",

    # Remarque de l'énoncé:
    #   pour faciliter le problème, il n'y a pas d'espace au début ni à la fin des phrases
    #
    # Je vois pas trop en quoi cela causerait problème ??
    " un espace au début et un autre à la fin "
]
print(predict(cas_particuliers, "un"))
