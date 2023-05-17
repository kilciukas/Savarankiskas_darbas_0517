# Sukurti programą, kuri nuskaitys iš .txt failo skaičius (failą kokį norite susikurkite bei užpildykite kokiais norite skaičiais),
# suskaičiuos visų skaičių vidurkį (naudojant reduce() funkciją) bei išsaugos rezultatą į kitą .txt  failą (šį failą taip pat susikurkite kokį norite).
# Taip pat, tą patį vidurkį išspausdinkit ir į terminalą.

import random
from functools import reduce
def main():
    while True:
        print("1 - Generuoti skaičių failą" "\n" "2 - Skaičiuoti vidurkį")
        option = int(input("Įveskite pasirinkimą: "))
        if option == 1:
            generuoti_skaiciu_faila()
        if option == 2:
            try:
                skaiciuoti_vidurki()
            except FileNotFoundError:
                print("Pirmiausia sugeneruokite skaičius")
                main()
def generuoti_skaiciu_faila():
    skaiciai = [random.randint(1,10) for x in range(10)]
    with open("skaiciai.txt", "w") as failas:
        for x in skaiciai:
            failas.write(str(x)+ "\n")

def skaiciuoti_vidurki():
    with open("skaiciai.txt", "r") as failas:
        nums = [float(line.strip()) for line in failas]
        avg = reduce(lambda x, y: x + y, nums) / len(nums)
        with open("vidurkis.txt", "w") as vidurkis_failas:
            vidurkis_failas.write(str(avg))
        print(avg)

main()
