def trouver_paires(no_telephones):
    paires = [] # liste qui contiendra les paires

    #
    # (BRE) Bien que cette solution fonctionne correctement elle présente un gros soucis de performance si le
    # dictionnaire no_telephones contient beaucoup d'entrées. En effet, supposons que le dictionnaires contiennent
    # 100 entrées, le "if" imbriqué dans les deux boucles "for" sera exécuté 100*100 = 10.000 fois. Le nombre
    # d'exécution est donc proportionnel au CARRE de la taille du dictionnaire (1000 entrées -> 1.000.000 d'exécutions)
    #
    # Dans ce cas, une approche telle que celle proposée dans /EXAMEN_Moyen_Telecom.py est préférable. Cette dernière
    # est d'ailleurs comparable à la stratégie adoptée pour la méthode "moyenne_menages()" ci-dessous...
    #

    for personneA, numA in no_telephones.items():
        for personneB, numB in no_telephones.items():
            if (numA == numB) and (personneA != personneB) and ([personneA, personneB] not in paires) and ([personneB, personneA] not in paires):
                paires.append([personneA, personneB])
                print([personneA, personneB])
    return paires

def moyenne_menages(no_telephones):
    # Partie 2: calcule le nombre moyen de personnes associées à un même numéro de téléphone
    nbr_personnes = {} # dictionnaire qui contiendra les nombres de personnes associées à chaque numéro de téléphone
    for personneA, numA in no_telephones.items():
        if numA in nbr_personnes:
            nbr_personnes[numA] += 1
        else:
            nbr_personnes[numA] = 1

    somme = 0
    for num in nbr_personnes:
        somme += nbr_personnes[num]
    moyenne = somme/len(nbr_personnes)

    return moyenne
