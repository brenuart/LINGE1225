
def message(lst):
    senderRecords = []

    for msg in lst:
        record(senderRecords, msg[0], msg[1])

    return senderRecords

def record(senderRecords, sender, receiver):
    senderRecord = findOrCreateSender(senderRecords, sender)

    if receiver in senderRecord:
        senderRecord[receiver] += 1
    else:
        senderRecord[receiver] = 1


def findOrCreateSender(senders, sender):
    for s in senders:
        if s["Auteur"] == sender:
            return s

    s = {
            "Auteur": sender
        }
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