# la fonction dont on doit faire l'intégrale - elle est "donnée" comme le dit l'énoncé
#
def f(x):
    return 5


def integrale(a, b, nbPoints):
    largeur = (b - a) / nbPoints
    surfaceTotale = 0

    x = a
    while x < b:
        petiteBase = f(x)
        grandeBase = f(x + largeur)
        surface = (petiteBase + grandeBase) * largeur / 2

        surfaceTotale += surface
        x += largeur

    return surfaceTotale


print(integrale(0, 10, 500))