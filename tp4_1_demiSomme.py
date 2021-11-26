
def demiSomme(l):
    somme = [0] * len(l)

    for i in range(len(l)):
        ligne = l[i]

        if len(ligne) != len(l):
            return "None"

        for j in range(i, len(ligne)):
            somme[i] += ligne[j]

    return somme

# -----------------------------

def test(input, expected):
    actual = demiSomme(input)

    print("demiSomme(", input, ") => ", actual)

    if actual != expected:
        print("Erreur! Expected: ", expected)

test([[1,3,5], [2,7,3], [9,1,8]], [9,10,8])
test([[1], [1,2], [1,2,3]], "None")