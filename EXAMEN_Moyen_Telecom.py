#
# Note:
#   Prendre connaissance des commentaires ajoutés à la correction proposée par les professeurs dans le fichier
#   /corrections/Examen_Moyen_Telecom.py
#

def trouver_paires(no_telephones):
    # Première étape: construction d'un dictionnaire dont les clés sont les numéros
    # de téléphone et la valeur une liste des personnes qui ont cet numéro.
    # Exemple:
    # {
    #   "000": [ "Marguerite", "Alain", "Claude_Ollier" ],
    #   "111": [ "Nathalie", "Claude_Simon" ],
    #   ...
    # }
    groupes = {}
    for name,phone in no_telephones.items():
        # si aucune entrée pour ce numéro de téléphone, alors on en crée une dont la valeur est une liste vide
        if not phone in groupes:
            groupes[phone] = []

        # ajout du nom à la liste associée à l'entre (la clé) phone.
        groupes[phone].append(name)


    # Seconde etape: créer des paires
    #
    pairs = []
    for phone,names in groupes.items():
        # "names" est donc une liste de noms... L'objectif est de créer toutes les paires possibles et les ajouter
        # dans la liste "pairs" qui contient le résultat final.
        #
        # Donc, pour une liste [1, 2, 3, 4], il faut créer les paires suivantes:
        #   [1,2], [1,3], [1,4],
        #          [2,3], [2,4],
        #                 [3,4]
        #
        for i in range(len(names)):
            for j in range(i + 1, len(names)):
                pairs.append([ names[i], names[j] ])

    return pairs



def moyenne_menages(no_telephones):
    countByPhone = {}
    for name, phone in no_telephones.items():
        if not phone in countByPhone:
            countByPhone[phone] = 1
        else:
            countByPhone[phone] += 1

    total = 0
    for phone, count in countByPhone.items():
        total += count

    return total / len(countByPhone) # attention: divide by zero if no_telephones is empty


# --------------------------------------------------------------------------
no_telephones = {
    "Marguerite_Duras":    "000",
    "Marie_Susini":        "222",
    "Alain_Robbe_Grillet": "000",
    "Claude_Olivier":      "000",
    "Nathalie_Sarraute":   "111",
    "Claude_Simon":        "111",
    "Michel_Butor":        "222",
    "JeanMarie_LeClezio":  "333"
}

print(trouver_paires(no_telephones))
print(moyenne_menages(no_telephones))