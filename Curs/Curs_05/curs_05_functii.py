"""
Functiile reprezinta o modalitate prin care sa reutilizam cod.
Functiile sunt definite prin intermediul keyword-ului def
Corpul functiei, la fel ca si la structurile alternative (if) si structurile repetitive (while, for, for each)
este marcat printr-o indentatre fata de marginea fisierului definita functiei si respectiv corpul functiei sunt
delimitate de caracterul ":"

Atentie! O functie intotdeauna va fi definita si apelata cu paranteze, indiferent daca are parametri sau nu.
In caz contrar sistemul va crede ca este o variabila
Parametri = templetizarea viitoarelor valori care pot fi trimise de catre utilizator de la tastatura (definitie)
Argumente = valorile efective care sunt trimise de utilizator de la tastatura	(apelare)
Apelarea unei functii inseamna scrierea numelui functiei impreuna cu argumentele aferente moment in care sistemul cauta
adresa de memorie reprezentata de numele functiei, extrage codul de la acea adresa de memorie si il executa
"""
# Functie simpla fara return si fara parametri
# Exercitiu 1: Functie care sa printeze pe ecran propozitia "Hello World"


def say_hello_world():
    print("Hello world")
    print("I am so excited to be here")
    print("Este vineri si suntem plini de chef de curs")


if __name__ == "__main__":
    say_hello_world()


def hai_sa_ne_prezentam():
    nume = input("Te rugam sa introduci numele ")
    varsta = int(input("Te rugam sa introduci varsta "))
    print(f"Te numesti {nume} si ai varsta de {varsta} ani")
    print(f"Varsta ta va creste peste 2 ani si va deveni: {varsta+2}")


# hai_sa_ne_prezentam()

# Functie simpla fara return si cu parametri


def say_hello(nume_persoana):
    print(f"Hello {nume_persoana}")


# nume = input("Te rugam sa introduci numele ")
# say_hello(nume)


def calculeaza_suma_a_doua_numere(nr_1, nr_2):
    suma = nr_1 + nr_2
    print(f"Suma celor doua numere este: {suma}")


if __name__ == "__main__":
    calculeaza_suma_a_doua_numere(5, 7)
"""
hardcodare (hardcoding) = scrierea valorilor efective in cod
"""


def inmultirea_a_doua_numere(nr_1, nr_2):
    print(f"Inmultirea a doua numere este: {nr_1 * nr_2}")

# a,b = input("Introduceti numerele: ").split()
# inmultirea_a_doua_numere(int(a),int(b))
# exemplu split:
# text_de_separat = "Ana are mere, pere si prune"
# print(text_de_separat.split(sep="e"))

# Aici s-a aplicat conceptul de polimorfism


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

# varsta = int(input("Va rugam sa introduceti varsta "))
# season = input("Va rugam sa introduceti anotimpul de calatorie ")
# clasa = int(input("Va rugam sa introduceti clasa la care calatoriti: 1 / 2 "))
# price = int(input("Va rugam sa introduceti pretul biletului "))
# pret_bilet = 0


if __name__ == "__main__":
    pret_1 = calculeaza_pret_bilet(64, "iarna", 1, 30, 2)
    pret_2 = calculeaza_pret_bilet(67, "vara", 2, 45)
    suma_castigata_din_vanzari = pret_1 + pret_2
    print(suma_castigata_din_vanzari)

# nr_calatori_iulie = 10
# suma_pret = 0
# for i in range(0,11):
# 		if varsta <= 65:
# 				nr_copii = int(input("Va rugam a introduceti numarul de copii"))
# 				pret_bilet = calculeaza_pret_bilet(varsta, season, clasa, price, nr_copii)
# 				print(f"Calatorul curent a achizitonat un pachet turistic in valoare de {pret_bilet} lei")
# 		else:
# 				pret_bilet = calculeaza_pret_bilet(varsta, season, clasa, price)
# 				print(f"Calatorul curent a achizitonat un pachet turistic in valoare de {pret_bilet} lei")
# 		suma_pret += pret_bilet

# while result.next():
# 		if varsta <= 65:
# 				nr_copii = int(input("Va rugam a introduceti numarul de copii"))
# 				pret_bilet = calculeaza_pret_bilet(varsta, season, clasa, price, nr_copii)
# 				print(f"Calatorul curent a achizitonat un pachet turistic in valoare de {pret_bilet} lei")
# 		else:
# 				pret_bilet = calculeaza_pret_bilet(varsta, season, clasa, price)
# 				print(f"Calatorul curent a achizitonat un pachet turistic in valoare de {pret_bilet} lei")
# 		suma_pret += pret_bilet

"""
Notiuni testare manuala:
In general exista mai multe compartimentari ale tipurilor si tehnicilor de testare
Tehnicile de teste se impart in doua categorii generale:
1. Testare statica (review, analiza statica)
2. Testare dinamica (blackbox testing, whitebox testing)
a) blackbox testing -testare fara acces la cod (testare frontend, testare de interfata)
- equivalence partitioning
- boundary value analysis
- state transition testing
- use case testing
- decision table
b) whitebox testing - testare cu acces la cod (testare backend)
- statement coverage
- decision coverage
"""

# functii cu args  - sunt folosite atunci cand vrem sa definim functii cu un numar indefinit de parametri


def suma_liste_indef(*args):
    suma = []
    for numar in args:
        suma = suma + numar
    return suma


def suma_numere_indef(*args):
    suma = 0
    for numar in args:
        suma += numar
    return suma

# print(suma_numere_indef(1,2))
# print(suma_numere_indef(1))
# print(suma_numere_indef(1,567,890,54678902,34594387263748596584))


if __name__ == "__main__":
    lista1 = [1, 3, 5, 7, 9]
    lista2 = [0, 2, 4, 6, 8]
    print(suma_numere_indef(*lista1))
    print(suma_numere_indef(*lista1, *lista2))
    print(suma_numere_indef(1, 3, 5, 7, 9, 0, 2, 4, 6, 8))
    print(suma_liste_indef([1, 3, 5, 7, 9], [0, 2, 4, 6, 8]))
    print(suma_liste_indef(lista1, lista2))
# suma_numere_indef(1,3,5,7,9) # trebuie sa se intample
# suma_numere_indef([1,3,5,7,9]) # nu trebuie sa se intample

# lista_numere = [5,7,9]

# functii cu kwargs - sunt folosite pentru a a parcurge dictionare

fotbalisti_pe_echipe = {
    "Barcelona": {
        "Dica": {
            "Nume complet": "Nicolae Dica",
            "Varsta": 45,
            "Numar Tricou": 10},
        "Banel": {
            "Nume complet": "Banel Nicolita",
            "Varsta": 47,
            "Numar Tricou": 3},
        "Dukadam": {
            "Nume complet": "Helmut Dukadam",
            "Varsta": 65,
            "Numar Tricou": 7}
        }}


def afiseaza_fotbalisti(**kwargs):
    for key, value in kwargs.items():
        for key_inner, value_inner in value.items():
            print(f"La echipa {key} joaca: ")
            for key_jucator, value_jucator in value_inner.items():
                print("Detalii jucator", f"{key_jucator}:{value_jucator}", sep=" - ", end=",")
            print("\n--------------------------------")


if __name__ == "__main__":
    afiseaza_fotbalisti(**fotbalisti_pe_echipe)
# fotbalisti_pe_echipe["Barcelona"]["Dukadam"]


def schimba_elemente(a, b):
    # swap = a
    # a = b
    # b = swap
    # print(a,b)
    a, b = b, a
    print(a, b)


if __name__ == "__main__":
    schimba_elemente(14, 12)