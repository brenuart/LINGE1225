def estAntiMagique(mat):
    # Vérifie que la matrice est carrée
    if (len(mat) != len(mat[0])):
        return False

    somme = [0 for i in range(2*len(mat)+2)]

    # Calcule la somme des diagonales
    for i in range(len(mat)):
        somme[2*len(mat)] += mat[i][i]
        somme[2*len(mat)+1] += mat[i][len(mat)-1-i]

    # Calcule la somme des lignes et des colonnes
    for i in range(len(mat)):
        for j in range(len(mat)):
            somme[i] += mat[i][j] # ligne i
            somme[len(mat)+i] += mat[j][i] # colonne i


    #Trie le vecteur score de manière croissante
    temp=0
    for i in reversed(range(1,len(somme))):
        for j in range(i):
            if(somme[j]>somme[j+1]):
                temp = somme[j]
                somme[j] = somme[j+1]
                somme[j+1] = temp

    #Vérifie que le premier élément vaut n
    if somme[0]!=len(mat):
        return False

    #Vérifie que le vecteur est bien une suite arithémique de raison 1
    for i in range(len(somme)-1):
        if(somme[i]+1 != somme[i+1]):
            return False
    return True
