
def estMagique(mat):
    # taille du carré
    size = len(mat)

    # verifier que c'est un carré
    for l in range(size):
        if len(mat[l]) != size:
            return False

    # calcul des sommes
    sommeLignes = [0] * size
    sommeColonnes = [0] * size
    sommeDiagonale1 = 0
    sommeDiagonale2 = 0

    for l in range(size):
        sommeDiagonale1 += mat[l][l]
        sommeDiagonale2 += mat[size-l-1][size-l-1]

        for c in range(size):
            sommeLignes[l] += mat[l][c]
            sommeColonnes[c] += mat[l][c]

    if sommeDiagonale1 == sommeDiagonale2 and sommeLignes == sommeColonnes:
        return True
    else:
        return False

# -----------------------------

def test(input, expected):
    actual = estMagique(input)

    print(input, " => ", actual)

    if actual != expected:
        print("Erreur! Expected: ", expected)


test([[4,9,2],[3,5,7],[8,1,6]], True)
test([[4,9,2],[1,2],[1]], True)