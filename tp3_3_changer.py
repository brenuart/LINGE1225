def changer1(str):
    result = ""

    for c in str:
        if c == "r":
            result += "l"
        else:
            result += c

    return result


# Autre forme...
def changer2(str):
    result = ""

    for c in str:
        if c == "r":
            c = "l"
        result += c

    return result

# --------------------------------------------------------
print(changer2("Et ce grand dragon, cet ancien serpent"))
