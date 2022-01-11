def trouver_paires(no_telephones):
    paires = [] # liste qui contiendra les paires
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
