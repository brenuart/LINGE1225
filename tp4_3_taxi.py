
def payeTaxi(M,P):
    totalPrice = 0
    maxPrice = 0
    courseLaPlusChere = 0

    for course in M:
        d = distance(course[1], course[2], course[3], course[4])
        print(d)
        price = prix(d, P)

        totalPrice += price

        if price > maxPrice:
            maxPrice = price
            courseLaPlusChere = course[0] # le numéro de la course est dans le premier élément...

    return [totalPrice, courseLaPlusChere]


def prix(distance, prixParKm):
    return distance * prixParKm

def distance(xa,ya,xb,yb):
    return abs(xb-xa) + abs(yb-ya)

# -----------------------------

m1 = [
    [1, -6, -3, 3, -5],
    [2, 1, 9, -1, 4],
    [3, 2, 3, 1, 3],
    [4, 2, -4, -5, -10]]

print(payeTaxi(m1, 9)) # [288, 4]
print(payeTaxi(m1, 5)) # [160, 4]
print(payeTaxi([], 9)) # [0,0]