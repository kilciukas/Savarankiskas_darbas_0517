# Sukurti funkciją, kuri priimtų sąrašą tuple elementų, kiekvienas tuple sudarytas iš 2 elementų - stringo ir sąrašo int skaičių.
# Funkcija turi grąžinti sąrašą tuple elementų, kurie sudaryti iš 2 reikšmių: stringo ir skaičių vidurkio:
# Pvz: į funkciją paduodamas sąrašas: [("apple", [1, 2, 3]), ("banana", [4, 5, 6]), ("orange", [7, 8, 9])],
# turi būti grąžinamas: [("apple", 2.0), ("banana", 5.0), ("orange", 8.0)]
# Panaudoti sukurtą funkciją su kokiomis norite reikšmėmis ir atspausdinti funkcijos rezultatus
from statistics import mean
def tvarkyti_sarasa(sarasas):
    tuple_sarasas2 = []
    for elementas in sarasas:
        stringas = elementas[0]
        skaiciai = elementas[1]
        if type(stringas) == str:
            tuple_sarasas2.append(stringas)
        if type(skaiciai) == list:
            tuple_sarasas2.append(mean(skaiciai))
    print(tuple_sarasas2)

tuple_sarasas = [ ("apple", [1, 2, 3]), ("banana", [4,5,6]), ("orange", [7,8,9]), ("bulvė", [10, 50, 20]), ("kriaušė", [1, 0, 5]) ]
tvarkyti_sarasa(tuple_sarasas)