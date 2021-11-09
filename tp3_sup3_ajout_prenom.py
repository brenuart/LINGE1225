# Première approche...
# ... qui ne fonctionne pas (cfr. explications)

def ajoutPrenom1(liste, prenom):
    # La liste est triée par ordre alphabétique, on peut donc la parcourir à partir du début et s'arrêter
    # dès que l'élément qui s'y trouve est plus grand que celui qu'on cherche, càd "prenom".
    # Il suffit alors d'ajouter "prenom" dans la liste juste avant celui sur lequel on s'est arrêté.
    #
    # Pour rappel, les strings peuvent être comparées via les opérateurs >, >=, <, <=:
    #   "a" < "b"     ("a" est avant "b" dans l'alphabet)
    #   "az" > "aa"   (on commence par comparer les deux premiers caractères, si ils sont les mêmes,
    #                  on compare les suivants, etc)
    #   "a" < "aa"    (les deux sont identiques sur la "première" partie, la second chaine de caractère étant plus
    #                  longue, elle est considérée comme étant "plus grande" au sens de la comparaison)


    for prenomDeLaListe in liste:
        # Est-ce le prénom qu'on cherche...
        if prenomDeLaListe == prenom:
            # ... dans ce cas, rien à faire (rien à ajouter à la liste)
            return

        # Est-ce plus "grand" (càd plus loin dans l'ordre alphabétique) que "prenom"...
        if prenomDeLaListe > prenom:
            # ... on ajoute prenom dans la liste juste avant

# ------>
# ------>     Oui, mais... comment faire? On ne connait pas la position courante dans la liste (juste la valeur de
# ------>     l'élément sur lequel on se trouve). Il nous manque l'index... le "for" n'est pas bon.
# ------>
            print("Ooops, ca va pas marcher!")

#
# Seconde approche ;-)
#
# Cette fois on va itérer sur les élements de la liste via leur indice...
#
def ajoutPrenom2(liste, prenom):
    # La liste est triée par ordre alphabétique, on peut donc la parcourir à partir du début et s'arrêter
    # dès que l'élément qui s'y trouve est plus grand que celui qu'on cherche, càd "prenom".
    # Il suffit alors d'ajouter "prenom" dans la liste juste avant celui sur lequel on s'est arrêté.
    #
    # Pour rappel, les strings peuvent être comparées via les opérateurs >, >=, <, <=:
    #   "a" < "b"     ("a" est avant "b" dans l'alphabet)
    #   "az" > "aa"   (on commence par comparer les deux premiers caractères, si ils sont les mêmes,
    #                  on compare les suivants, etc)
    #   "a" < "aa"    (les deux sont identiques sur la "première" partie, la second chaine de caractère étant plus
    #                  longue, elle est considérée comme étant "plus grande" au sens de la comparaison)

    for i in range(len(liste)-1):
        prenomDeLaListe = liste[i]

        # Est-ce le prénom qu'on cherche...
        if prenomDeLaListe == prenom:
            # ... dans ce cas, rien à faire (rien à ajouter à la liste)
            return

        # Est-ce plus "grand" (càd plus loin dans l'ordre alphabétique) que "prenom"...
        if prenomDeLaListe > prenom:
            # ... on ajoute prenom dans la liste juste avant
            liste.insert(i, prenom)

            # ... et on peut s'arrêter
            return

        # Dans les autres cas, on laisse la boucle for continuer jusqu'à ce que tous les éléments de la liste aient
        # été traités ou qu'une des conditions ci-avant soit remplie.


    # Si on atteint ce point, c'est que la boucle for est terminée et que le "prenom" n'a pas été trouvé ET qu'aucun
    # des prénoms de la liste n'est "plus grand". "prenom" doit donc être ajouté à _la fin_ de la liste (cfr. ordre
    # alphabétique)
    liste.append(prenom)


# Cette fonction ajoute le prenom dans la liste si nécessaire et affiche la liste des prénoms.
#
def ajoutPrenomAndPrint(liste, prenom):
    ajoutPrenom2(liste, prenom)
    print(liste)


ajoutPrenomAndPrint(["Alice", "Lisa", "Luca"], "Antoine")
ajoutPrenomAndPrint(["Alice", "Lisa", "Luca"], "Zoro")
ajoutPrenomAndPrint(["Alice", "Lisa", "Luca"], "Alice")
ajoutPrenomAndPrint([], "Alice")