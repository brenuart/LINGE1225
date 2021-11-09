def verifierMul(l, n):
    # on itere sur les elements de la liste "l" -> "x" vaut tour à tour chaque element de la liste "l"
    # du premier au dernier, dans l'ordre
    for x in l:
        # -- debut de bloc
        if not isMultipleOf(x, n):   # equivalent à:  if isMultipleOf(x, n) == False
            return False  # Sortie de fonction avec comme résultat False
                          # Les instructions suivantes ne sont PAS exécutées
        # -- fin de bloc

    # On arrive ici seulement après avoir terminé la boucle for, pour autant qu'on ne soit pas
    # sorti avant (cfr. "return"...)
    return True


# Fonction qui détermine si "x" est un multiple de "n".
# return True is x est un multiple de n
# return False otherwise
def isMultipleOf(x, n):
    if n == 0:
        return True

    if x % n == 0:
        return True
    else:
        return False


# Pour rappel:
#   not False == True
#   not True == False
#
# Donc, si isMultiple(x,n) retourne False, la condition:
#
#    if not isMultiple(x,n)...
#
# est équivalente à
#
#    if not False...
#
# donc équivalente à
#
#    if True...
#
# et donc le bloc de code qui suit le IF est exécuté.