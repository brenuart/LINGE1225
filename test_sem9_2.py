# Il s'agit de la solution à laquelle nous sommes arrivés sur papier ensemble...
#
def plus_longue_periode_croissante01(data):
    # On commence par les cas particuliers...
    #
    if len(data) == 0:
        return 0

    if len(data) == 1:
        return 1


    # A partir d'ici, on sait qu'il y a plus de 1 éléments dans la liste.
    # On va itérer à partir du second élément (indice 1) et le comparer avec le précédent...
    #
    maxSequenceSize = 0
    sequenceSize = 1 # on sait que la séquence courante est au moins de un élément (le précédent...)

    for i in range(1, len(data)):
        if data[i-1] < data[i]:
            sequenceSize += 1
        else:
            if sequenceSize > maxSequenceSize:
                maxSequenceSize = sequenceSize
            sequenceSize = 1

    # Hint: important dans le cas où la liste ne contient qu'une seule séquence toujours croissante...
    if sequenceSize > maxSequenceSize:
        maxSequenceSize = sequenceSize

    return maxSequenceSize

# -------------------------------------------
# La même chose mais en utilisant la fonction standard "max(arg1, arg2)" qui retourne le maximum des arguments
# arg1 et arg2...
#
def plus_longue_periode_croissante02(data):
    # On commence par les cas particuliers...
    #
    if len(data) == 0:
        return 0

    if len(data) == 1:
        return 1


    # A partir d'ici, on sait qu'il y a plus de 1 éléments dans la liste.
    # On va itérer à partir du second élément (indice 1) et le comparer avec le précédent...
    #
    maxSequenceSize = 0
    sequenceSize = 1 # on sait que la séquence courante est au moins de un élément (le précédent...)

    for i in range(1, len(data)):
        if data[i-1] < data[i]:
            sequenceSize += 1
        else:
            maxSequenceSize = max(maxSequenceSize, sequenceSize)
            sequenceSize = 1

    # Hint: important dans le cas où la liste ne contient qu'une seule séquence toujours croissante...
    maxSequenceSize = max(maxSequenceSize, sequenceSize)

    return maxSequenceSize


# -------------------------------------------
# Une autre manière de faire en se souvenant de l'élément précédent (lastValue)
#
def plus_longue_periode_croissante03(data):
    maxSequenceSize = 0
    sequenceSize = 0
    lastValue = 0

    for value in data:
        if sequenceSize == 0 or value > lastValue:
            sequenceSize += 1
            lastValue = value
        else:
            if sequenceSize > maxSequenceSize:
                maxSequenceSize = sequenceSize
            sequenceSize = 1

    # Hint: important dans le cas où la liste ne contient qu'une seule séquence toujours croissante... (on ne sera
    # jamais passé dans le "else" ci-dessus)
    if sequenceSize > maxSequenceSize:
        maxSequenceSize = sequenceSize

    return maxSequenceSize


# ----------------

f = plus_longue_periode_croissante02

data = [4150, 4250, 4300, 4300, 4200, 4200, 4300]
print(f(data)) # 3

data = [1, 2, 0, 3, 4, 5]
print(f(data)) # 4

# vide
data = []
print(plus_longue_periode_croissante01(data)) # 0

# un seul élément
data = [1]
print(plus_longue_periode_croissante01(data)) # 1

# liste croissante
data = [1, 2, 3]
print(plus_longue_periode_croissante01(data)) # 3
