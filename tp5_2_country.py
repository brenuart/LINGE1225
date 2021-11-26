
def get_country(l, name):
    for country in l:
        if country["City"] == name:
            return country["Country"]

    return False

# ------------

l = [
    { "City": "Bruxelles", "Country": "Belgium" },
    { "City": "Berlin",    "Country": "Germany" },
    { "City": "Paris",     "Country": "France" }
]

print(get_country(l, "Bruxelles"))
print(get_country(l, "Londre"))
