def maximaLocaux(tab):
    res = []

    prev = 0
    croissant = False
    for i in range(len(tab)):
        v = tab[i]
        if v >= prev:
            croissant = True
        else:
            if croissant:
                res.append(i-1)
            croissant = False

        prev = v

    return res

def estVallee(tab, xa, xb):
    ya = tab[xa]
    yb = tab[xb]

    for x in range(xa, xb+1):
        y = tab[x]
        if y > valeurDroite(xa, ya, xb, yb, x):
            return False

    return True


def valeurDroite(xa, ya, xb, yb, x):
    return ((x - xa) * (ya - yb)) / (xa - xb) + ya


def plusGrandeVallee(tab):
    # Les plus grandes vallees sont nécessairement entre les maxima locaux...
    maxima = maximaLocaux(tab)

    maxValleeX = 0
    maxValleeY = 0

    for i in range(len(maxima)):
        for j in range(i+1, len(maxima)):
            x = maxima[i]
            y = maxima[j]
            if estVallee(tab, x, y) and (length(x,y) > length(maxValleeX, maxValleeY)):
                maxValleeX = x
                maxValleeY = y

    return maxValleeX, maxValleeY

def length(x,y):
    return abs(x-y)

# ----------------------------------------------------

tab = [3, 6, 7, 10, 13, 11, 11, 12, 10, 9, 7, 5, 4, 3, 3, 4, 3, 4, 2, 1, 2]
print(maximaLocaux(tab))

print(estVallee(tab, 7, 15))

print(plusGrandeVallee(tab))