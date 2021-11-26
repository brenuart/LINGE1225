
def predict(lst, mot):
    counts = {}

    for phrase in lst:
        recordNextWord = False
        for word in phrase.split(" "):
            if recordNextWord == True:
                incrementWord(counts, word)
                recordNextWord = False

            if word == mot:
                recordNextWord = True

    return counts


def incrementWord(counts, word):
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

# ------

lst = [
    "bonjour, j'écris un message",
    "un message a été écrit",
    "un oiseau est venu se poser sur un arbre",

    # gotcha: le "mot" est suivi par le "mot"...
    "un un deux",

    # Remarque de l'énoncé:
    #   pour faciliter le problème, il n'y a pas d'espace au début ni à la fin des phrases
    #
    # Je vois pas trop en quoi cela causerait problème ??
    " un espace au début et un autre à la fin "
]


print(predict(lst, "un"))