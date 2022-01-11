# (BRE) Attention !
# Les arguments de la méthode sont nommés "a" et "b" et non "j1" et "j2" comme dans l'énoncé de la question.
# De plus, la méthode déclare deux variables locales "j1" et "j2"...
# Attention donc lors de la lecture: "j1" et "j2" ne CORRESPONDENT PAS aux "j1"/"j2" de l'énoncé!!!
#
# Par ailleurs, cette implémentation est inutilement complexe - cfr commentaires ci-dessous.
# Une version "simplifiée" sur base des commentaires est donnée ci-dessous (méthode "bataille_reviewed()")
#
def bataille(a,b):
    j1 = []
    j2 = []
    cj1 = []
    cj2 = []
    win=1
    tas=[[],[]]

    # Copie la liste des cartes des deux joueurs

    # (BRE) Pourquoi faire une telle copie? Elle n'est absolument pas nécessaire!
    # Sauf éventuellement pour changer la valeur de l'AS et lui donner 14 de manière à ce qu'il soit supérieur à
    # toutes les autres cartes... Et encode! Dans le cas présent cette modification se fait directement dans les
    # tableaux a[] et b[] donnés en arguments et pas dans les copies....

    for i in range(len(a[0])):
        # Change la valeur de l'as
        if a[0][i] == 1:
            a[0][i]=14

        if(b[0][i] == 1):
            b[0][i]=14

        j1.append(a[0][i])
        j2.append(b[0][i])
        cj1.append(a[1][i])
        cj2.append(b[1][i])

    while (len(j1)!=0 and len(j2)!=0):
        c1 = j1[0]
        c2 =j2[0]
        a1 = cj1[0]
        a2 =cj2[0]

        if ((c1 > c2) or ((c1 == c2) and (a1 < a2))):
            j1.append(c1)
            j1.append(c2)
            cj1.append(a1)
            cj1.append(a2)

        if ((c1 < c2) or ((c1 == c2) and (a1 > a2))):
            j2.append(c1)
            j2.append(c2)
            cj2.append(a1)
            cj2.append(a2)

        # (BRE) Deux "IF"... ?
        # Le premier teste la condition pour que la carte du joueur1 soit gagnante.
        # Le second teste la condition pour que la carte du joueur2 soit gagnante.
        # Pourquoi ce second test? Il me semble suffisant de dire que si joueur1 n'est pas gagnant alors c'est
        # joueur2 qui gagne... Donc un IF ... ELSE ...
        #
        #   if ((c1 > c2) or ((c1 == c2) and (a1 < a2))):
        #       j1.append(c1)
        #       j1.append(c2)
        #       cj1.append(a1)
        #       cj1.append(a2)
        #   else:
        #       j2.append(c1)
        #       j2.append(c2)
        #       cj2.append(a1)
        #       cj2.append(a2)

        j1.pop(0)
        j2.pop(0)
        cj1.pop(0)
        cj2.pop(0)

    if(len(j1)==0):
        win=2
        tas[0]=j2
        tas[1]=cj2
    else:
        tas[0]=j1
        tas[1]=cj1

    return win, tas


# -----------------------

# Version revue de l'implémentation ci-dessus. Cette version suit la même logique... mais peut-être un peu
# plus "lisible"...

def bataille_reviewed(j1, j2):
    # Remplacer les cartes AS (1) par la valeur 14 de manière à ce que sa valeur soit toujours plus grande que les
    # autres cartes. De cette manière, déterminer si une carte est supérieur à une autre revient a comparer leur role.

    for i in range(len(j1[0])):
        # Change la valeur de l'as
        if j1[0][i] == 1:
            j1[0][i] = 14

        if (j2[0][i] == 1):
            j2[0][i] = 14

    while len(j1[0]) != 0 and len(j2[0]) != 0:
        carte1   = j1[0].pop(0)
        couleur1 = j1[1].pop(0)
        carte2   = j2[0].pop(0)
        couleur2 = j2[1].pop(0)

        if ((carte1 > carte2) or ((carte1 == carte2) and (couleur1 < couleur2))):
            j1[0].append(carte1)
            j1[1].append(couleur1)
            j1[0].append(carte2)
            j1[1].append(couleur2)
        else:
            j2[0].append(carte1)
            j2[1].append(couleur1)
            j2[0].append(carte2)
            j2[1].append(couleur2)

    if (len(j1[0]) == 0):
        return 2, j2
    else:
        return 1, j1
