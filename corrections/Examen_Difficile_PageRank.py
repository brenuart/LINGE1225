def ProbabilityMatrix(A):
    P = []
    temp=[]
    D = OutdegreeVector(A)
    for i in range(len(A)):
        for j in range(len(A[0])):
            temp.append(A[i][j]/D[i])
        P.append(temp)
        temp=[]
    return P

def produitMatriceVecteur(A,d):
    if len(A[0]) != len(d):
        return 0
    else:
        c = [0 for i in range(len(d))]
        for i in range(len(A)):
            for k in range(len(A[0])):
                c[i] += A[i][k]*d[k]
        return c

def PageRankScore(A):
    P = ProbabilityMatrix(A)
    Pt = Transpose(P)
    score = normalize(IndegreeVector(A))
    diffscore = 1
    oldscore=[]
    while (diffscore > 0.000001):
        oldscore=score
        score =  produitMatriceVecteur(Pt,oldscore)
        diffscore = 0
        for i in range(len(score)):
            diffscore = diffscore + abs(score[i]-oldscore[i])
    return score
