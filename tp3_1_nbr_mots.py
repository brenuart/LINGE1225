# Première approche naïve: il suffit de compter les blancs...
#
def nbr_mots1(mot):
    count = 0
    for c in mot:
        if c == " ":
            count += 1
    return count


# Ca marche pas -> on peut avoir plusieurs blancs consécutifs...
# On a donc besoin de savoir si le caractère courant est dans un mot ou pas.
# -> selon la définition, un mot est une suite de caractère encadrés par un ou plusieurs blancs
# -> dit autrement, un mot est une suite de caractère non blanc

def nbr_mots2(mot):
    count = 0
    dansUnMot = False

    for c in mot:
        # Si c'est un blanc, on est pas dans un mot...
        if c == " ":
            dansUnMot = False

        # Le caractère est donc dans un mot, on augmente le compteur de mot seulement si on n'était pas déjà dans
        # un mot (on vient de passer d'un blanc à un non blanc)
        elif not dansUnMot:   # dansUnMot == False
            dansUnMot = True
            count += 1

    return count


# Un autre idée - plus simple/intuitive sans doute: on détecte les transitions "blanc" -> "lettre".
# Cette transition indique donc le début d'un _nouveau_ mot... il suffit de compter le nombre de transitions.
#
def nbr_mots3(mot):
    count = 0
    previous = " "

    for c in mot:
        # si le char n'est pas un blanc mais que le précédent l'était - alors on est au début
        # d'un nouveau mot, on augmente donc le compteur de mots
        if c != " " and previous == " ":
            count += 1

        # le char précédent devient le char courant
        previous = c

    return count



# Correctif "officiel" de l'exercise.
# bof bof....
#
def nbr_mots_correctif(phrase):
    is_char = False
    x = " "
    compteur = 0

    for i in range(len(phrase)):
        x = phrase[i]
        if x != " ":
            is_char = True
        elif is_char == True:
            compteur += 1
            is_char = False

    # Ah ben oui... maintenant ils ont un problème si il n'y a aucun blanc dans la phrase!
    # Et en plus, ils ont oublié le cas où la phrase serait vide - il manquait la ligne suivante:
    if len(phrase) > 0:
        x = phrase[len(phrase)-1]   # phrase[-1]
        if x != " ":
            compteur += 1

    return compteur


# ----------------------------------------------------------------------------

nbr_mots = nbr_mots3

print(nbr_mots("Ceci est une chaine de caractères"))
print(nbr_mots("Ceci"))
print(nbr_mots(" "))
print(nbr_mots(" a     b  "))
print(nbr_mots(""))