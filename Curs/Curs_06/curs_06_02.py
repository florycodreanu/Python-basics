from Curs_06 import curs_06_01


class Casa:
    numar_etaje = None
    numar_camere = None
    numar_bai = None
    material_constructie = None
    suprafata = None
    an_constructie = None
    adresa = None
    clasa_energetica = None
    pret = None

    def __init__(self, numar_etaje, numar_camere, numar_bai, material_constructie, suprafata, adresa):
        self.numar_etaje = numar_etaje
        self.numar_camere = numar_camere
        if numar_bai > 2:
            print("Nu putem construi mai mult de doua bai")
        else:
            self.numar_bai = numar_bai
        self.material_constructie = material_constructie
        self.suprafata = suprafata
        self.adresa = adresa

    def calculeaza_aprobare_numar_etaje(self):
        if self.numar_etaje > 5:
            print("Cand unul iti spune: esti beat mergi mai departe. Daca doi iti spun ca esti beat mergi sa te culci")
        else:
            self.aprobare = True

    def actualizeaza_an_constructie(self, an_constructie):
        self.an_constructie = an_constructie
        return self.an_constructie

    def vinde_casa(self):
        print(f"Apartament de vanazare in zona lalelelor"
              f"Numar camere: {self.numar_camere}"
              f"Numar etaje: {self.numar_etaje}"
              f"Numar bai: {self.numar_bai}"
              f"An constructie: {self.an_constructie},"
              f"Suprafata: {self.suprafata}"
              f"Material constructie: {self.material_constructie}")


garsoniera = Casa(0, 1, 1, "beton", 40, "Strada Lalelelor 23")
apartament_2_camere = Casa(0, 2, 1, "caramida poroasa", 70, "Strada Zambilelor")
apartament_4_camere = Casa(1, 4, 2, "BCA", 130, "Strada Trandafirilor")
print(f"Garsoniera are {garsoniera.numar_camere} camere")
print(f"Garsoniera este construita din {garsoniera.material_constructie}")
print(f"Adresa garsonierei este {garsoniera.adresa}")
print(f"Apartamentul cu 2 camere are {apartament_2_camere.numar_bai} bai")
print(f"Suprafata apartamentului cu 2 camere este {apartament_2_camere.suprafata} metri patrati")
print(f"Apartamentul cu 2 camere a fost finalizata in {apartament_2_camere.actualizeaza_an_constructie(2022)}")
apartament_4_camere.pret = 150000
print(f"Pretul apartamentului cu 4 camere este {apartament_4_camere.pret} EURO")

lista = [3, 5, 9, 7, 1]
lista_noua = curs_06_01.Gestiune_Liste(lista)
lista_noua.bubble_sort()
print(f"Lista sortata este: {lista}")
print(f"Este lista sortata? {lista_noua.sortata}")
