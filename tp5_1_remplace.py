
def remplace(message, abbreviation):
    # split (decoupe) du message en mots -> separateur = blanc (" ")
    words = message.split(" ")

    phrase = ""
    for w in words:
        if w in abbreviation:
            phrase += abbreviation[w]
            phrase += " "  # les blancs sont des séparateurs -> ils ne font donc pas partie des mots
                           # et il faut les rajouter entre chaque mot

    # suppression du blanc "en trop" à la fin de la nouvelle phrase
    phrase = phrase.rstrip()

    return phrase

# -------

abbreviation= {
    'slt': 'salut!',
    'cmt': 'comment',
    'cv': 'ca va?',
    'tfq': 'tu fais quoi?'
}

print(remplace("slt cmt cv tfq aujourd'hui", abbreviation))