class Reveil:
    def __init__(self, heure, minute, seconde):
        self.heure = heure
        self.minute = minute
        self.seconde = seconde

    def getHeure(self):
        return self.heure

    def getMinute(self):
        return self.minute

    def getSeconde(self):
        return self.seconde

    def nouvelleHeure(self, nbseconde):
        self.seconde += nbseconde
        if self.seconde > 59:
            self.minute += self.seconde // 60
            self.seconde = self.seconde % 60

        if self.minute > 59:
            self.heure += self.minute // 60
            self.minute = self.minute % 60

        if self.heure > 23:
            self.heure = self.heure % 24


    def __str__(self):
        return "{0}:{1}:{2}".format(self.heure, self.minute, self.seconde)

# -------------------------------

r = Reveil(8, 20, 55)
r.nouvelleHeure(3723)
print(r)
