
def message(lst):
    # "senderRecords" est une liste qui contient des "Dictionnaires" (des "Map") ayant la structure suivante:
    #
    #   {
    #     "Auteur": <le nom de l'expéditeur du message>,
    #     <dest1>: <le nombre de message envoyé au destinataire "dest1"> (un entier),
    #     <dest2>: <le nombre de message envoyé au destinataire "dest2"> (un entier),
    #     ...
    #     <destN>: <le nombre de message envoyé au destinataire "destN"> (un entier),
    #   }
    #
    senderRecords = []


    # On parcours tous les messages...
    #
    for msg in lst:
        sender = msg[0]
        receiver = msg[1]

        # On recherche le "senderRecord" (le Dictionnaire) qui correspond au "sender" dans la liste (et on le crée
        # si il n'existe pas encore - càd la première fois qu'on rencontre un message envoyé par ce "sender")
        #
        senderRecord = findOrCreateSenderRecord(senderRecords, sender)

        # On augmente de +1 le nombre de message envoyé par ce "sender" vers le "receiver". Si c'est la première fois
        # que ce sender envoie au receiver, il faut créer une nouvelle entrée dans le dictionnaire.
        #
        if receiver in senderRecord:
            senderRecord[receiver] += 1
        else:
            senderRecord[receiver] = 1

    # On a parcouru tous les messages - la liste "senderRecords" contient les dictionnaires qu'on veut renvoyer
    # comme résultat...
    #
    return senderRecords


# Parcours de la liste "senders" à la recherche du "senderRecord" (dictionnaire) dont la clé "Auteur" est égale au
# "sender" passé en argument. Si aucun dictionnaire n'est trouvé pour le "sender", un nouveau est créé et ajouté à la
# liste.
#
def findOrCreateSenderRecord(senders, sender):
    for s in senders:
        if s["Auteur"] == sender:
            return s

    s = { "Auteur": sender }
    senders.append(s)

    return s


# ------
lst = [
    # From,      To
    ["Grumpy",   "Garfield"],
    ["Grumpy",   "Lucifer"],
    ["Lucifer",  "Grumpy"],
    ["Garfield", "Grumpy"],
    ["Garfield", "Grumpy"],
    ["Garfield", "Grumpy"]
]

print(message(lst))