#
# Note:
#   Prendre connaissance des commentaires additionnels ajoutés au correctif du professeur.
#   Cfr fichier  corrections/Examen_Difficile_Casier_de_bieres.py
#

class Casier:
    # bac est une matrice a deux dimensions modélisant la position de chaque
    # bouteille dans le casier
    def __init__(self, bac):
        self.bac = bac

    def party(self, nom):
        # Parcours de toutes les bieres (bouteilles) du casier...
        for rangee in self.bac:
            for b in rangee:
                # ... a la recherche de celles qui portent le nom souhaité et qui ne sont pas déjà vides
                if b.getNom() == nom and b.estPleine():
                    # ... boire les bières recherchées
                    b.boire()


    def avgAlcool(self):
        nbBouteillesPleines = 0
        totalAlcool = 0

        for rangee in self.bac:
            for b in rangee:
                if b.estPleine():
                    nbBouteillesPleines += 1
                    totalAlcool += b.getAlcool()

        if nbBouteillesPleines == 0:
            return 0
        else:
            return totalAlcool / nbBouteillesPleines


    # tab est une liste de Casier
    def isStronger(self, tab):
        # Calcul du taux moyen d'alcool de _ce_ casier (càd "self")
        avgAlcoolDeCeCasier = self.avgAlcool()

        # Parcours de tous les casiers de la liste donnée en argument (tab)...
        for b in tab:
            # Comparaison du taux d'alcool du casier avec "celui-ci"
            if b.avgAlcool() >= avgAlcoolDeCeCasier:
                return False

        # Aucun des casiers de la liste n'a un taux moyen supérieur ou egal à celui-ci
        return True


    # (non demandé dans l'exercice)
    def countBouteillesPleines(self):
        total = 0
        for rangee in self.bac:
            for b in rangee:
                if b.estPleine():
                    total += 1
        return total

# ------------------------------

#
# (non demandé par l'exercice, implémenté juste pour pouvoir "essayer" le code...)
#
class Biere:
    def __init__(self, nom, alcool, pleine):
        self.nom = nom
        self.alcool = alcool
        self.pleine = pleine

    def boire(self):
        self.pleine = False

    def getNom(self):
        return self.nom

    def getAlcool(self):
        return self.alcool

    def estPleine(self):
        return self.pleine

# ------------------------------
casier1 = Casier([
    [ Biere("Jupiler", 1, True), Biere("Jupiler", 1, True), Biere("Jupiler", 1, True)],
    [ Biere("Leffe", 2, True),   Biere("Leffe", 2, True),   Biere("Leffe", 2, True)],
    [ Biere("Orval", 3, True),   Biere("Orval", 3, True)]
])

casier2 = Casier([
    [ Biere("Jupiler", 1, True), Biere("Jupiler", 1, True), Biere("Jupiler", 1, True)],
    [ Biere("Orval", 3, True),   Biere("Orval", 3, True)]
])

casier3 = Casier([
    [ Biere("Jupiler", 1, True), Biere("Jupiler", 1, True), Biere("Jupiler", 1, True)],
    [ Biere("Jupiler", 1, True), Biere("Jupiler", 1, True), Biere("Jupiler", 1, True)]
])

print("avgAlcool casier1: ", casier1.avgAlcool())
print("avgAlcool casier2: ", casier2.avgAlcool())
print("avgAlcool casier3: ", casier3.avgAlcool())
print(casier1.isStronger([casier2, casier3]))

casier1.party("Jupiler")
print("boire Jupiler, pleines: ", casier1.countBouteillesPleines())

casier1.party("Leffe")
print("boire Jupiler, pleines: ", casier1.countBouteillesPleines())

casier1.party("Orval")
print("boire Jupiler, pleines: ", casier1.countBouteillesPleines())