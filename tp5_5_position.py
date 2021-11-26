
def position(lst, lettre):
    positions = {}

    for mot in lst:
        pos = 0
        for c in mot:
            if c == lettre:
                recordPosition(positions, mot, pos)
            pos += 1

    return positions


def recordPosition(positions, mot, pos):
    if pos not in positions:
        positions[pos] = []

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