def bataille(j1,j2):
    while len(j1[0]) != 0 and len(j2[0]) != 0:
        carte_j1 = j1[0].pop(0)
        carte_j2 = j2[0].pop(0)
        couleur_j1 = j1[1].pop(0)
        couleur_j2 = j2[1].pop(0)

        if meilleure_carte(carte_j1, carte_j2, couleur_j1, couleur_j2):
            j1[0].append(carte_j1)
            j1[1].append(couleur_j1)
            j1[0].append(carte_j2)
            j1[1].append(couleur_j2)
        else:
            j2[0].append(carte_j1)
            j2[1].append(couleur_j1)
            j2[0].append(carte_j2)
            j2[1].append(couleur_j2)

    if j1[0] == []:
        gagnant = 2
        tas_gagnant = j2
    else:
        gagnant = 1
        tas_gagnant = j2

    return gagnant,tas_gagnant

# Methode compare deux cartes et retourne TRUE si la première est gagnante
# Paramètres:
# carte1: role de la premiere carte
# carte2: role de la seconde carte
# couleur1: couleur de la premiere carte
# couleur2: couleur de la seconde carte
def meilleure_carte(carte1, carte2, couleur1, couleur2):
    if carte1 == 1 and carte2 != 1:
        return True

    if carte2 == 1 and carte1 != 1:
        return False

    if carte1 == carte2:
        if couleur1 > couleur2: # cfr. énoncé -> valeurs associées aux couleurs
            return False
        else:
            return True

    if carte1 > carte2:
        return True
    else:
        return False

# --------------------------------------------------------------------------------
j1 = [
    [4, 2, 3],
    [2, 1, 4]
]
j2 = [
    [4, 2, 3],
    [1, 2, 3]
]
print(bataille(j1,j2))
