def merge(lst1, lst2):
    result = []

    pos1 = 0 # indice de l'element suivant à prendre dans lst1
    pos2 = 0 # indice de l'element suivant à prendre dans lst2

    while pos1 < len(lst1) and pos2 < len(lst2):
        if lst1[pos1] <= lst2[pos2]:
            result.append(lst1[pos1])
            pos1 += 1
        else:
            result.append(lst2[pos2])
            pos2 += 1

    if pos1 < len(lst1):
        result += lst1[pos1:]

    if pos2 < len(lst2):
        result += lst2[pos2:]

    return result

# --------------------------------------------------------

print(merge([1,3,5], [3,4]))
