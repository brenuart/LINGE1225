def __init__(self,bac):
    self.__bac=bac

def party(self, nom):
    for i in range(len(self.__bac)):
        for j in range(len(self.__bac[0])): # (BRE) cela fait l'hypothese que toutes les rangées du bac ont la même
                                            # taille (càd la taille de la première rangée). D'un point de vue "réel"
                                            # faire une telle hypothèse semble raisonnable mais rien n'indique dans
                                            # l'énoncé que tous les éléments de la liste "bac" sont des listes de même
                                            # dimension.
                                            # Il serait donc plus prudent de tenir compte de la véritable taille de la
                                            # rangée courante en écrivant:
                                            #
                                            #      for j in range(len(self.__bac[i])):
                                            #          ...
            b=self.__bac[i][j]
            if b.getNom()==nom and b.estPleine():
                self.__bac[i][j].boire()    # (BRE) Ne serait-il pas plus simple et plus logique d'écrire:
                                            # b.boire() ?

    # (BRE) pourquoi utiliser les indices? Nous n'avons pas besoin de connaitre la position des bouteilles dans le
    # casier - on veut juste les parcourir toutes... On peut donc écrire la même boucle comme suit:
    #
    #    for rangee in self.__bac:
    #        for b in rangee:
    #            if b.getNom() == nom and b.estPleine():
    #                b.boire()
    #
    # Beaucoup plus lisible il me semble - et surtout moins de risque de faire des erreurs en "mélangeant"
    # les indices...


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
