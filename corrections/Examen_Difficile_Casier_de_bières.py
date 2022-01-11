def __init__(self,bac):
    self.__bac=bac

def party(self, nom):
    for i in range(len(self.__bac)):
        for j in range(len(self.__bac[0])):
            b=self.__bac[i][j]
            if b.getNom()==nom and b.estPleine():
                self.__bac[i][j].boire()

def avgAlcool(self):
    total=0
    count=0
    for i in range(len(self.__bac)):
        for j in range(len(self.__bac[0])):
            b=self.__bac[i][j]
            if b.estPleine():
                total+=b.getAlcool()
                count+=1

    if count !=0:
        total=total/count
    return total

def isStronger(self,tab):
    taux=self.avgAlcool()
    for i in range(len(tab)):
        c=tab[i]
        if c.avgAlcool()>=taux:
                return False
    return True
