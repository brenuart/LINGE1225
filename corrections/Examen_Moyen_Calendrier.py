class Date:
    def __init__(self, jour,mois,annee):
        self.__jour=jour
        self.__mois=mois
        self.__annee=annee
    def getJour(self):
        return self.__jour
    def getMois(self):
        return self.__mois
    def getAnnee(self):
        return self.__annee
    def hier(self):
        if(self.__jour!=1):
            self.__jour=self.__jour-1
        else:
            an=self.__annee
            jr= self.__jour
            ms= self.__mois
            if((an%4==0 and an%100 !=0) or an%400==0) and ms==3:
                self.__jour=29
                self.__mois=2
            else:
                if(ms==3 and jr==1):
                    self.__jour=28
                    self.__mois=2
                if(ms==1 and jr==1):
                    self.__jour=31
                    self.__mois=12
                    self.__annee=self.__annee-1
                if(ms==2 or ms==4 or ms==6 or ms==9 or ms==11 or ms==8):
                    self.__jour=31
                    self.__mois=self.__mois-1
                if(ms==5 or ms==7 or ms==10 or ms== 12):
                    self.__jour=30
                    self.__mois=self.__mois-1
