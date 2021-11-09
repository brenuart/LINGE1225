
def biologiste(S):
    # Plante A
    #

    # on commence au temps 0, on le fait evoluer (+1 semaine) en calculant pour chaque semaine la surface occupée
    # par la plante A. Des que la surface >= S ou est <= 0 on s'arrete.
    #
    # on fait la meême chose pour la plante B
    #
    # les deux plantes sont mortes ou on atteint la surface de l'etang S.
    # on compare les temps mis par chaque...
    # blbla

    ta = 0
    while True:
        # calcul des surfaces au moment "t"
        surfaceA = surfacePlanteA(ta)

        # est-ce qu'on peut s'arreter?
        if surfaceA >= S or surfaceA <= 0:
            break
        else:
            ta += 1


    # Plante B
    #
    tb = 0
    while True:
        # calcul des surfaces au moment "t"
        surfaceB = surfacePlanteB(tb)

        # est-ce qu'on peut s'arreter?
        if surfaceB >= S or surfaceB <= 0:
            break
        else:
            tb += 1


    if surfaceA == 0 and surfaceB == 0:
        return "impossible", ta, tb

    if surfaceA > 0 and surfaceB == 0:
        return "a", ta, tb

    if surfaceB > 0 and surfaceA == 0:
        return "b", ta, tb

    if ta == tb:
        return "egalite", ta, tb

    if ta < tb:
        return "a", ta, tb
    else:
        return "b", ta, tb


# nombre de feuilles de la plante A au temps "t"
def feuillesPlanteA(t):
    if t == 0:
        return 1
    if t < 0:
        return 0
    return 2 * feuillesPlanteA(t-1) - feuillesPlanteA(t-2)

def surfacePlanteA(t):
    return 200 * feuillesPlanteA(t)


# nombre de feuilles de la plante B au temps "t"
def feuillesPlanteB(t):
    if t == 0:
        return 1
    if t < 0:
        return 0
    return 1.7 * feuillesPlanteB(t-1) - feuillesPlanteB(t-3)

def surfacePlanteB(t):
    return 250 * feuillesPlanteB(t)


print(biologiste(0.1 * 10000))
#print(biologiste(1 * 10000)) # attention! Prend bcp de temps (à cause du calcul récursif de "feuillesPlante"...
