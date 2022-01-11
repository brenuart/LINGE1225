def maximaLocaux(tab):
        # Déclaration des variables utilisées dans la méthode
        maximaLocaux = []

        # Première boucle for: identification des maxima locaux
        # Attention : les premier et dernier éléments du tableau ne sont jamais considérés comme des maxima locaux, par simplicité
        for i in range(len(tab)-1):
            if (tab[i] > tab[i-1] and tab[i] > tab[i+1]):
                maximaLocaux.append(i)
        return maximaLocaux

def estVallee(tab, a, b):
        isVallee = True
        for i in range(a,b+1):
            # Si on a un point supérieur à la droite, ce n'est pas une vallée ==> estVallee = false
            if(tab[i] > valeurDroite(a, tab[a], b, tab[b], i)):
              isVallee = False
        return isVallee

def plusGrandeVallee(tab):
        maxLocaux = maximaLocaux(tab)
        resultat = []
        indexDebut,indexFin,longueurPlusGrandeVallee = 0,0,0
        for i in range(0,len(maxLocaux)):
            for j in range(i+1,len(maxLocaux)):
                if(estVallee(tab, maxLocaux[i], maxLocaux[j]) and abs(maxLocaux[j] - maxLocaux[i]) > longueurPlusGrandeVallee):
                    indexDebut = maxLocaux[i]
                    indexFin =  maxLocaux[j]
                    longueurPlusGrandeVallee = abs(maxLocaux[j] - maxLocaux[i])
        resultat.append(indexDebut)
        resultat.append(indexFin)
        return resultat
