"""
Encapsularea este o modalitate prin care putem sa ascundem anumite atribute sau metode utilizatorului
Motivul pentru care vrem sa facem asta este:
- fie din motive de securitate
- fie pentru a controla modificarea anumitor atribute de catre utilizator]
Ex: pe un camp de varsta nu vrem sa permitem adaugarea valorilor negative)

Exista trei tipuri de restrictii numite:
- public = atributul sau metoda pot fi accesate oriunde in program
- protected = atributul sau metoda poate fi accesat in afara clasei dar nu este sugerat utilizatorului
- private = atributul sau metoda poate fi accesat si folosit doar in interiorul clasei

atributele si metodele public vor fi scrise in mod normal
atributele si metodele protected for fi precedate de caracterul "_"
atributele si metodele private for fi precedate de doua caractere "__"

Aceste restrictii vor mai fi identificate in unele limbaje de programare (java) cu numele de modificatori de acces

ATENTIE!! In java atributele si metodele private pot fi accesate doar in acelasi pachet

Pentru a putea modifica atributele de tip protected, ne folosim de conceptele de getter, setter, deleter

"""


class CasaEncapsulareSetterGetterDeleter:
    _numar_etaje = None
    numar_camere = None
    numar_bai = None
    __material_constructie = None
    suprafata = None
    an_constructie = None
    adresa = None
    clasa_energetica = None
    pret = None

    def __init__(self, numar_etaje, numar_camere, numar_bai, material_constructie, suprafata, adresa):
        self._numar_etaje = numar_etaje
        self.numar_camere = numar_camere
        if numar_bai > 2:
            print("Nu putem construi mai mult de doua bai")
        else:
            self.numar_bai = numar_bai
        self.__material_constructie = material_constructie
        self.suprafata = suprafata
        self.adresa = adresa

    def calculeaza_aprobare_numar_etaje(self):
        if self._numar_etaje > 5:
            print("Cand 1 iti spune \"esti beat\" mergi mai departe. Daca doi iti spun \"esti beat\" mergi sa te culci")
        else:
            self.aprobare = True

    def __actualizeaza_an_constructie(self, an_constructie):
        self.an_constructie = an_constructie
        return self.an_constructie

    def vinde_casa(self):
        print(f"Apartament de vanazare in zona lalelelor"
              f"Numar camere: {self.numar_camere}"
              f"Numar etaje: {self._numar_etaje}"
              f"Numar bai: {self.numar_bai}"
              f"An constructie: {self.an_constructie},"
              f"Suprafata: {self.suprafata}"
              f"Material constructie: {self.__material_constructie}")

    def get_an_constructie_dupa_actualizare(self):
        return self.__actualizeaza_an_constructie(1991)

    # getter - o modalitate prin care sa extragem valoarea atributului. nu trebuie sa aiba alt rol
    def get_materiale_constructie(self):
        return self.__material_constructie

    # setter - o modalitate prin care putem sa modificam valoarea unui atribut. nu trebuie sa aiba alt rol
    def set_materiale_constructie(self, materiale_constructie):
        self.__material_constructie = materiale_constructie

    # deleter - o modalitate prin care putem sa stergem valoarea unui atribut. nu trebuie sa aiba alt rol
    def delete_materiale_constructii(self):
        self.__material_constructie = None


if __name__ == "__main__":
    garsoniera = CasaEncapsulareSetterGetterDeleter(0, 1, 1, "beton", 40, "Strada Lalelelor 23")
    print(garsoniera._numar_etaje)
    print(garsoniera.get_materiale_constructie())

if __name__ == "__main__":
    print("===========================")


class CasaEncapsulareDecoratori:
    # decorator = elemente care modifica comportamentul unei functii
    _numar_etaje = None
    numar_camere = None
    numar_bai = None
    __material_constructie = None
    suprafata = None
    an_constructie = None
    adresa = None
    clasa_energetica = None
    pret = None

    def __init__(self, numar_etaje, numar_camere, numar_bai, material_constructie, suprafata, adresa):
        self._numar_etaje = numar_etaje
        self.numar_camere = numar_camere
        if numar_bai > 2:
            print("Nu putem construi mai mult de doua bai")
        else:
            self.numar_bai = numar_bai
        self.__material_constructie = material_constructie
        self.suprafata = suprafata
        self.adresa = adresa

    def calculeaza_aprobare_numar_etaje(self):
        if self._numar_etaje > 5:
            print("Cand unul iti spune ca esti beat mergi mai departe. Daca doi spun ca esti beat mergi sa te culci")
        else:
            self.aprobare = True

    def __actualizeaza_an_constructie(self, an_constructie):
        self.an_constructie = an_constructie
        return self.an_constructie

    def vinde_casa(self):
        print(f"Apartament de vanazare in zona lalelelor"
              f"Numar camere: {self.numar_camere}"
              f"Numar etaje: {self._numar_etaje}"
              f"Numar bai: {self.numar_bai}"
              f"An constructie: {self.an_constructie},"
              f"Suprafata: {self.suprafata}"
              f"Material constructie: {self.__material_constructie}")

    @property
    def materiale_constructie(self):
        pass

    @materiale_constructie.getter
    def materiale_constructie(self):
        return self.__material_constructie

    @materiale_constructie.setter
    def materiale_constructie(self, material_constructie):
        self.__material_constructie = material_constructie

    @materiale_constructie.deleter
    def materiale_constructie(self):
        self.__material_constructie = None


if __name__ == "__main__":
    garsoniera = CasaEncapsulareDecoratori(0, 1, 1, "beton", 40, "Strada Lalelelor 23")
    print(f"materiale de constructie returnate prin getter inainte de update: {garsoniera.materiale_constructie}")
    # apelare getter
    garsoniera.materiale_constructie = "caramida"  # setter
    print(f"materiale de constructie returnate prin getter dupa update: {garsoniera.materiale_constructie}")
    # apelare getter
    del garsoniera.materiale_constructie
    print(f"materiale de constructie returnate prin getter dupa delete: {garsoniera.materiale_constructie}")
    # apelare getter
