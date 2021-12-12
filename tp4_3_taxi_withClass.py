
def payeTaxi(M,P):
    totalPrice = 0
    maxPrice = 0
    courseLaPlusChere = 0

    for course in M:
        d = course.distance()
        price = d * P

        totalPrice += price

        if price > maxPrice:
            maxPrice = price
            courseLaPlusChere = course.numero

    return [totalPrice, courseLaPlusChere]


class Course:
    def __init__(self, numero, xa, ya, xb, yb):
        self.numero = numero
        self.xa = xa
        self.xb = xb
        self.ya = ya
        self.yb = yb

    def distance(self):
        return abs(self.xb - self.xa) + abs(self.yb - self.ya)


# -----------------------------
m1 = [
    Course(1, -6, -3,  3,  -5),
    Course(2,  1,  9, -1,   4),
    Course(3,  2,  3,  1,   3),
    Course(4,  2, -4, -5, -10)]

print(payeTaxi(m1, 9)) # [288, 4]
print(payeTaxi(m1, 5)) # [160, 4]
print(payeTaxi([], 9)) # [0,0]

# 11
# 7
# 1
# 13