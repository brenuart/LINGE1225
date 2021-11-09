# Première idée: on prends chaque caractère de str1 un par un et on vérifie si il est inclu dans str2...
#
def anagramme(str1, str2):
    for c in str1:
        if contains(str2, c) == False:
            return False

    return True

# verifie que str contient le caractère "charToContain"
def contains(str, charToContain):
    for c in str:
        if c == charToContain:
            return True
    return False


# -------------------------------------------------------------------------------------------

# Alternative: use "in" to check substring is included in fullstring, eg
#    if substring in fullstring:
#
def anagramme2(str1, str2):
    for c in str1:
        if not c in str2:
            return False
    return True


def anagramme3(str1, str2):
    # doivent être de même longueur
    if len(str1) != len(str2):
        return False

    # doivent être différents
    if str1 == str2:
        return False

    # verifie que chaque char de str1 se trouve dans str2
    for c in str1:
        if not c in str2:
            return False

    return True


print(anagramme3("maire", "aimer"))
print(anagramme3("maire", "aimer"))
print(anagramme3("maire", "maire"))
