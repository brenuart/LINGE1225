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

    # Rappel: 3 // 2 -> division entière de 3 par 2, résultat: 1
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


    # Alternative
    #
    # La méthode "nouvelleHeure()" ci-dessus ne fonctionnera pas correctement si "nbseconde" est négatif. L'énoncé
    # original du problème n'indique d'ailleurs pas clairement que "nbseconde" est _toujours_ positif. C'est donc
    # peut-être un cas dont il faut tenir compte.
    #
    # La méthode ci-dessous fonctionne dans tous les cas: positifs et négatifs - donc ajout et soustraction de secondes
    # au temps stocké dans l'objet Reveil.
    #
    def nouvelleHeure2(self, nbseconde):
        # On transforme le temps courant en secondes
        timeInSeconds = self.heure * 3600 + self.minute * 60 + self.seconde

        # On ajoute les seconds demandées
        timeInSeconds += nbseconde

        # On transforme le total de secondes en heure, minute et seconde.
        self.heure = timeInSeconds // 3600 # 3600 secondes par heure --> nb heure == division entière par 3600
        timeInSeconds -= self.heure * 3600 # on enlève le nombre de secondes correspondants aux heures, il ne reste
                                           # donc que des minutes et des secondes...

        self.minute = timeInSeconds // 60
        timeInSeconds -= self.minute * 60

        self.seconde = timeInSeconds

        # Il reste le cas particulier des heures qui pourraient être supérieures à 23 après l'ajout des "nbseconde"
        if self.heure > 23:
            self.heure = self.heure % 24


    # (ne fait pas partie de l'exerice)
    # Petite astuce pour pouvoir faire un print(<date>) de manière "lisible"
    def __str__(self):
        return "{0}:{1}:{2}".format(self.heure, self.minute, self.seconde)

# -------------------------------

r = Reveil(8, 20, 55)
r.nouvelleHeure2(3723)
print(r)
