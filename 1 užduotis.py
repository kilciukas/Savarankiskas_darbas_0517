# Sukurti funkciją, kuri iš vardų sąrašo sudarytų sąrašą tik iš vardų pirmų raidžių ir tą sąrašą grąžintų:
# Pvz: paduodamas sąrašas į funkciją: [‘Jonas’, ‘Petras’, ‘Linas’], tai grąžinamas turėtų būti [‘J’, ‘P’, ‘L’]
# Paduoti vardų sąrašą į funkciją (vardus galite sugalvoti patys) ir atspausdinti funkcijos rezultatą

def vardai(list):
    raides = []
    for name in list:
        raides.append(name[0:1])
    print(raides)

x = ["Jonas", "Antanas", "Dalia", "Birutė"]
vardai(x)