
def position(lst, lettre):
    positions = {}

    # On parcours les mots de la liste...
    for mot in lst:

        # On parcours les lettres du mot...
        for i in range(len(mot)):

            # Si la lettre courante est la lettre recherchée, alors on appelle la méthode "recordPosition" qui se
            # chargera d'enregistrer le fait que la "lettre" est trouvée à la position "i" dans le mot "mot".
            #
            if mot[i] == lettre:
                recordPosition(positions, mot, i)

    return positions


def recordPosition(positions, mot, pos):
    # Ajout d'une nouvelle entrée dans le dictionnaire "positions" si nécessaire...
    if pos not in positions:
        positions[pos] = []

    # Ajout du "mot" à la liste correspondant à la position "pos"
    listeDeMots = positions[pos]
    listeDeMots.append(mot)


# ------------------

lst = ["bonjour", "bonsoir", "cours", "partir", "clavier", "souris", "tests", "ordinateur"]
print(position(lst, "e"))   # {5: ['clavier'], 1: ['tests'], 7: ['ordinateur']}
print(position(lst, "x"))   # {}
print(position([], "e"))    # {}

# Plusieurs mots avec la même position...
# ... et des mots avec plusieurs fois la lettre
print(position(lst, "o"))   # {1: ['bonjour', 'bonsoir', 'cours', 'souris'], 4: ['bonjour', 'bonsoir'], 0: ['ordinateur']}

# Et si la liste contient plusieurs fois le même mot?
# ... peut-être faudrait-il ne pas ajouter le mot "bonjour" une seconde fois dans le résultat ?
lst = ["bonjour", "bonsoir", "bonjour"]
print(position(lst, "o"))   # {1: ['bonjour', 'bonsoir', 'bonjour']}