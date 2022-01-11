def bataille(a,b):
    j1 = []
    j2 = []
    cj1 = []
    cj2 = []
    win=1
    tas=[[],[]]

    # Copie la liste des cartes des deux joueurs
    for i in range(len(a[0])):
        # Change la valeur de l'as
        if a[0][i] == 1:
            a[0][i]=14

        if(b[0][i] == 1):
            b[0][i]=14

        j1.append(a[0][i])
        j2.append(b[0][i])
        cj1.append(a[1][i])
        cj2.append(b[1][i])

    while (len(j1)!=0 and len(j2)!=0):
        c1 = j1[0]
        c2 =j2[0]
        a1 = cj1[0]
        a2 =cj2[0]

        if ((c1 > c2) or ((c1 == c2) and (a1 < a2))):
            j1.append(c1)
            j1.append(c2)
            cj1.append(a1)
            cj1.append(a2)

        if ((c1 < c2) or ((c1 == c2) and (a1 > a2))):
            j2.append(c1)
            j2.append(c2)
            cj2.append(a1)
            cj2.append(a2)

        j1.pop(0)
        j2.pop(0)
        cj1.pop(0)
        cj2.pop(0)

    if(len(j1)==0):
        win=2
        tas[0]=j2
        tas[1]=cj2
    else:
        tas[0]=j1
        tas[1]=cj1

    return win, tas
