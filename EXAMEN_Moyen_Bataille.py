def bataille(j1, j2):
    # hpothese: meme nombre de carte pour les 2 joueurs

    # j1 est une liste de deux lignes:
    # - la premiere ligne contient les ROLES des cartes
    # - la seconde ligne contient les COULEURS des cartes

    # Valeur d'une carte en fonction de son role:
    #   Carte   Code   Value
    #   1 (as)  1      14
    #   2       2      2
    #   3       3      3
    #   4       4      4
    #   5       5      5
    #   6       6      6
    #   7       7      7
    #   8       8      8
    #   9       9      9
    #   10      10     10
    #   Valet   11     11
    #   Dame    12     12
    #   Roi     13     13
    # En d'autres termes, la valeur est égale au code du role sauf pour le code A (l'AS) qui gagne tout le temps.

    # Couleur par ordre décroissant:
    # - coeur   -> 1
    # - carreau -> 2
    # - trefle  -> 3
    # - pique   -> 4
    # En d'autres termes, la couleur avec le code le plus petit gagne.

    # La partie est terminée lorsqu'un des deux joueurs n'a plus de cartes

    while len(j1[0]) > 0 and len(j2[0]) > 0:
        role1 = j1[0].pop(0)
        couleur1 = j1[1].pop(0)
        role2 = j2[0].pop(0)
        couleur2 = j2[1].pop(0)

        if estGagnant(role1, couleur1, role2, couleur2):
            j1[0].append(role1)
            j1[1].append(couleur1)
            j1[0].append(role2)
            j1[1].append(couleur2)
        else:
            j2[0].append(role1)
            j2[1].append(couleur1)
            j2[0].append(role2)
            j2[1].append(couleur2)

    if len(j1[0]) > 0:
        return { "gagnant": 1, "tas": j1 }
    else:
        return { "gagnant": 2, "tas": j2 }


def estGagnant(role1, couleur1, role2, couleur2):
    valeur1 = valeurRole(role1)
    valeur2 = valeurRole(role2)

    if valeur1 == valeur2:
        return couleur1 < couleur2
    else:
        return valeur1 > valeur2

def valeurRole(role):
    if role == 1:
        return 14
    else:
        return role


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


# 4/2, 2/1, 3/4       4/1, 2/2, 3/3
# 2/1, 3/4            2/2, 3/3, 4/2, 4/1
# 3/4, 2/1, 2/2       3/3, 4/2, 4/1
# 2/1, 2/2            4/2, 4/1, 3/4, 3/3
# 2/2                 4/1, 3/4, 3/3, 2/1, 4/2
#                     3/4, 3/3, 2/1, 4/2, 2/2, 4/1