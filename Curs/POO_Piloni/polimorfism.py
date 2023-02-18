from Curs_05.curs_05_functii import fotbalisti_pe_echipe
"""
polimorfism prin functii cu un numar indefinit de argumente
"""


def suma_numere_indef(*args):
    suma = 0
    for numar in args:
        suma += numar
        return suma


suma_numere_indef(5, 6, 7, 8, 9)
suma_numere_indef(5, 6, 7)
suma_numere_indef(5, 6, 7, 8, 9, 10, 11, 12, 13)


def afiseaza_fotbalisti(**kwargs):
    for key, value in kwargs.items():
        for key_inner, value_inner in value.items():
            print(f"La echipa {key} joaca: ")
            for key_jucator, value_jucator in value_inner.items():
                print("Detalii jucator", f"{key_jucator}:{value_jucator}", sep=" - ", end=",")
            print("\n--------------------------------")


afiseaza_fotbalisti(**fotbalisti_pe_echipe)


"""
polimorfism prin functii cu un parametri initializati cu valoare default
"""


def calculeaza_pret_bilet(varsta, season, clasa, price, nr_child=0):
    discount = 0
    if varsta > 65:
        discount = 0.15
    else:
        if nr_child > 0:
            discount = 0.1
    if season == 'iarna':
        discount += 0.1
    if clasa == 1:
        tax = 0.03
    else:
        tax = 0.01
    price = price - price * discount + price * tax
    return price


calculeaza_pret_bilet(68, "iarna", 1, 100)
calculeaza_pret_bilet(35, "iarna", 1, 100, 1)


"""
polimorfism prin aceeasi functie cu acelasi numar de parametri dar in clase diferite
"""


class America:
    limba = "Engleza"
    drapel = "American"
    imn = "Imnul americii"

    def printeaza_limba(self):
        print(f"Limba care se vorbeste in america este {self.limba}")


class Romania:
    limba = "Romana"
    drapel = "tricolor"
    imn = "desteapta-te romane"

    def printeaza_limba(self):
        print(f"Limba care se vorbeste in romania este {self.limba}")


obiect_america = America()
obiect_romania = Romania()
obiect_romania.printeaza_limba()
obiect_america.printeaza_limba()