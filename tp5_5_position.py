
def position(lst, lettre):
    positions = {}

    # On parcours les mots de la liste...
    for mot in lst:

        # On parcours les lettres du mot...
        for i in range(len(mot)):

            # Si la lettre courante (mot[i]) est la lettre recherchée, alors on ajoute le mot à la liste qui
            # est associée à la clé ayant comme "nom" la position courante.
            #
            if mot[i] == lettre:
                # Aucune clé pour la position courante (i) -> ajout d'une nouvelle avec une liste vide comme valeur initiale
                if i not in positions:
                    positions[i] = []

                # On ajoute le mot à la fin de la liste correspondant à la position
                positions[i].append(mot)

    return positions

# ------------------

lst = ["bonjour", "bonsoir", "cours", "partir", "clavier", "souris", "tests", "ordinateur"]
print(position(lst, "e"))   # {5: ['clavier'], 1: ['tests'], 7: ['ordinateur']}
print(position(lst, "x"))   # {}
print(position([], "e"))    # {}

# Plusieurs mots avec la même position...
# ... et des mots avec plusieurs fois la lettre recherchée
print(position(lst, "o"))   # {1: ['bonjour', 'bonsoir', 'cours', 'souris'], 4: ['bonjour', 'bonsoir'], 0: ['ordinateur']}

# Et si la liste contient plusieurs fois le même mot?
# ... peut-être faudrait-il ne pas ajouter le mot "bonjour" une seconde fois dans le résultat ?
# (non implémenté - laissé comme exercise..)
lst = ["bonjour", "bonsoir", "bonjour"]
print(position(lst, "o"))   # {1: ['bonjour', 'bonsoir', 'bonjour']}