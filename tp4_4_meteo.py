
def meteo(coordinates, temperatures):
    # hypothese: les deux matrices sont de même tailles et carrées
    size = len(coordinates)
    result = [[0 for i in range(size)] for j in range(size)]

    for i in range(size):
        for j in range(size):
            coord = coordinates[i][j] # coord est donc une liste de 2 items - des paires x,y
            x = coord[0]
            y = coord[1]
            result[x][y] = temperatures[i][j]

    return result

# ------------------------------------------------

coords = [
    [ [1,0], [0,1] ],
    [ [1,1], [0,0] ]
]
temperatures = [
    [20, 18],
    [17, 16]
]

print(meteo(coords, temperatures))