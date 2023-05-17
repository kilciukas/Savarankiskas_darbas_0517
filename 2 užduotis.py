# Sukurti funkciją, kuri priimtų tuple ir grąžintų kitą tuple, tik su pašalintais dublikatais. Eiliškumas elementų turi išlikti toks pats:
# Pvz: jeigu funkcija priima (1, 2, 3, 4, 3, 2, 1) tuple, tai turėtų grąžinti (1, 2, 3, 4)
# Pvz: jeigu funkcija priima (‘a’, ‘d’, ‘g’, ‘h’, ‘i’, ‘q’, ‘q’, ‘h’, ‘d’) tuple, tai turėtų grąžinti (‘a’, ‘d’, ‘g’, ‘h’, ‘i’, ‘q’)
# Paduoti tuple į funkciją (reikšmes sugalvokite patys) ir išspausdinti funkcijos rezultatą

def pasalinti_dublikatus(list):
    sarasas_unique = []
    for element in list:
        if not element in sarasas_unique:
            sarasas_unique.append(element)
    print(tuple(sarasas_unique))

tuple_sarasas = (10, 5, 6, 10, 1, 1, 30, 2, 5, "a", "c", "a", 100, 10, 1)
pasalinti_dublikatus(tuple_sarasas)
