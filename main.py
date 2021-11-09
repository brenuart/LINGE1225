from tp3_2 import *


def _max():
    n1 = int(input("Entrez le numero 1:"))
    n2 = int(input("Entrez le numero 2:"))
    n3 = int(input("Entrez le numero 3:"))

    if n1 > n2 or n1 > n3:
        max = n1
    elif n2 > n1 or n2 > n3:
        max = n2
    elif n3 > n1 or n3 > n2:
        max = n3

    max = n1
    if n2 > max:
        max = n2
    if n3 > max:
        max = n3


    if n1 == n2 or n1 == n3 or n2 == n3:
        print("Des valeurs identiques ont été introduites")

    print(max)

def calculDuMax():
    n1 = int(input("Entrez le numero 1:"))
    n2 = int(input("Entrez le numero 2:"))
    n3 = int(input("Entrez le numero 3:"))

    if n1 == n2 or n1 == n3 or n2 == n3:
        print("Des valeurs identiques ont été introduites")

    print(max(n1,n2,n3))

def triangle1(n):
    for x in range(0,n):
        for y in range(x):
            print("*", end=" ")
        print("*")

def pair(n):
    somme = 0
    for x in range(2, n, 2):
        print(x)
        somme += x
    return somme

def fibo(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

# n: épaisseur de la feuille en mm
def distance(m):
    if m < 0:
        return 0

    # distance Terre-Lune en millimètres
    distanceTerreLune = 384000 * 1000 * 1000

    # nombre de fois que la feuille est pliée
    # (on commence par 0, la feuille n’est pas pliée)
    nombreDePlis = 0

    # épaisseur (en millimètres) de la feuille pliée "nombreDePlis" fois
    # (l’épaisseur initiale est l’épaisseur de la feuille non pliée)
    epaisseur = m
    while epaisseur < distanceTerreLune:
        nombreDePlis += 1
        epaisseur *= 2

    return nombreDePlis

#print(distance(0.1))
#print(distance(-1))

