
def moyenne_mobile02(data,k):
    size = len(data)

    # not enough data
    if k > size:
        return []

    result = []
    for i in range(size-k+1):
        result.append(calculMoyenne(data, i, k))

    return result

# calcul moyenne sous sequence a partir de "pos" et longueur "k"
#
def calculMoyenne(data, pos, k):
    somme = 0
    for i in range(pos, pos+k):
        somme += data[i]

    return somme / k

# ---------------
data = [4100, 4150, 4200, 4400, 4300, 4200, 4100, 4300, 4500]
print(moyenne_mobile02(data, 3))