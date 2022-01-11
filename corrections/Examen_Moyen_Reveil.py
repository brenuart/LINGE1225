class Reveil:
    def __init__(self, heure,minute,seconde):
        self.__heure=heure
        self.__minute=minute
        self.__seconde=seconde

    def getHeure(self):
        return self.__heure

    def getMinute(self):
        return self.__minute

    def getSeconde(self):
        return self.__seconde

    def nouvelleHeure(self,nbseconde):
        #Transforme les secondes en heure, minute et seconde
        heure, minute, seconde,reste=0,0,0,0
        heure = nbseconde // 3600
        reste = nbseconde % (3600)
        minute = reste // 60
        seconde = reste % 60

        # On additionne d'abord les secondes
        self.__seconde += seconde

        # On vérifie de ne pas avoir 60 secondes ou de les dépasser
        if self.__seconde >= 60:
            self.__seconde-=60
            minute+=1

        # On additionne ensuite les minutes
        self.__minute += minute
        if self.__minute >= 60:
            self.__minute-=60
            heure+=1

        #On termine avec les heures
        self.__heure += heure
        if self.__heure >= 24:
            self.__heure=self.__heure-(self.__heure//24)*24
