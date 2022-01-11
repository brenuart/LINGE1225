def motCache(grille, mot):

    if((len(grille)<len(mot)) and (len(grille[0])<len(mot))):
        return False

    for l in range(len(grille)):
        for c in range(len(grille[0])-len(mot)+1):
            count=0
            for pos in range(len(mot)):
                if(grille[l][c+pos] == mot[pos]):
                    count+=1
                if(count== len(mot)):
                    return True

    for c in range(len(grille[0])):
        for l in range(len(grille)-len(mot)+1):
            count=0
            for pos in range(len(mot)):
                if(grille[l+pos][c] == mot[pos]):
                    count+=1
                if(count == len(mot)):
                    return True
    return False
