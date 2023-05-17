# Sukurti programą, kuri saugotų duomenis apie darbuotojus Pickle faile bei atliktų su duomenimis įvairius veiksmus:
# Sukurti funkciją, kuri sukuria darbuotoją (vardas, amžius, darbo pozicija) ir jį grąžina
# Sukurti funkciją, kuri išsaugo darbuotojus į failą (pickle)
# Sukurti funkciją, kuri užkrauna darbuotojus iš failo ir juos grąžina (pickle)
# Panaudoti sukūrimo funkciją kelis kartus su kokiomis norite reikšmėmis
# Panaudoti išsaugojimą į failą funkciją
# Panaudoti užkrovimo iš failo funkciją
# Atspausdinkite užkrautus iš failo duomenis
import pickle
darbuotoju_duomenys = []

def main():
    while True:
        print("1. Įvesti darbuotoją: ")
        print("2. Užkrauti darbuotojų duomenis")
        print("3. Išeiti")
        option = int(input("Įveskite pasirinkimą: "))
        if option == 1:
            darbuotojas()
            saugoti()
        if option == 2:
            atidaryti()
        if option == 3:
            exit()
def darbuotojas():
    darb = []
    vardas = input("Įveskite vardą: ")
    amzius = int(input("Įveskite amžių: "))
    pozicija = input("Įveskite darbo poziciją: ")
    darb.append(vardas)
    darb.append(amzius)
    darb.append(pozicija)
    darbuotoju_duomenys.append(darb)
def saugoti():
    with open("darbuotojai.pkl", "wb") as failas:
        pickle.dump(darbuotoju_duomenys, failas)

def atidaryti():
    with open("darbuotojai.pkl", "rb") as failas:
        x = pickle.load(failas)
        for elementas in x:
            print(elementas)

main()
