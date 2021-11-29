
def remplace(message, abbreviation):
    # split (decoupe) du message en mots -> separateur = blanc (" ")
    words = message.split(" ")

    decoded = ""  # message décodé avec les abbréviations remplacées par leur correspondant
    for word in words:
        if word in abbreviation:
            word = abbreviation[word]

        decoded += word + ' ' # les blancs sont des séparateurs -> ils ne font donc pas partie des mots et il faut les rajouter entre chaque mot

    return decoded

# -------

abbreviation= {
    'slt': 'salut!',
    'cmt': 'comment',
    'cv': 'ca va?',
    'tfq': 'tu fais quoi?'
}

print(remplace("slt cmt cv tfq aujourd'hui", abbreviation))