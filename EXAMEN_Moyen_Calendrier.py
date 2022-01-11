class Date:
    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def getJour(self):
        return self.jour

    def getMois(self):
        return self.mois

    def getAnnee(self):
        return self.annee

    # Les cas problématiques apparaissent quand la date courante est sur le premier du mois.
    # Il faut faire attention à:
    # - le 1/1/year -> on recule d'une année
    # - le 1/3/year -> on arrive fin février -> attention aux années bissextiles
    # - le 1/mois/year -> on arrive le 30 ou le 31 du mois précédent
    #
    def hier(self):
        if self.jour == 1:
            if self.mois == 1:
                self.annee -= 1
                self.mois = 12
                self.jour = 31
            else:
                self.mois -= 1
                if self.mois in [1, 3, 5, 7, 8, 10, 12]:
                    self.jour = 31
                elif self.mois in [4, 6, 9, 11]:
                    self.jour = 30
                elif self.mois == 2:
                    if bissextile(self.annee):
                        self.jour = 29
                    else:
                        self.jour = 28
        else:
            self.jour -= 1


    # Première implémentation "naïve"...
    #
    def demain(self):
        self.jour += 1

        if self.mois in [1,3,5,7,8,10,12] and self.jour > 31:
            self.mois += 1
            self.jour = 1

        elif self.mois in [4,6,9,11] and self.jour > 30:
            self.mois += 1
            self.jour = 1

        elif self.mois == 2 and bissextile(self.annee) and self.jour > 29:
            self.mois += 1
            self.jour = 1

        elif self.mois == 2 and not bissextile(self.annee) and self.jour > 28:
            self.mois += 1
            self.jour = 1

        if self.mois > 12:
            self.annee += 1
            self.mois = 1
            self.jour = 1

    # Amélioration de la version précédente: on se rend compte que les opérations effectuées dans les IF sont
    # toujours les mêmes...
    #
    def demain2(self):
        self.jour += 1

        if   (self.mois in [1,3,5,7,8,10,12] and self.jour > 31) \
          or (self.mois in [4,6,9,11] and self.jour > 30) \
          or (self.mois == 2 and bissextile(self.annee) and self.jour > 29) \
          or (self.mois == 2 and not bissextile(self.annee) and self.jour > 28):
            self.mois += 1
            self.jour = 1

        if self.mois > 12:
            self.annee += 1
            self.mois = 1
            self.jour = 1


    # (ne fait pas partie de l'exerice)
    # Petite astuce pour pouvoir faire un print(<date>) de manière "lisible"
    def __str__(self):
        return "{0}/{1}/{2}".format(self.jour, self.mois, self.annee)

def bissextile(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# ---------------------------------------------------

d = Date(1,3,2000)
print(d)

d.hier()
print(d)
