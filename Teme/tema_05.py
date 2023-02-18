# Exercitiul 1
# Functie care calculeaza si returneaza suma a doua numere


def suma_a_doua_numere():
    x = int(input("Introduceti primul numar :"))
    y = int(input("Introduceti al doilea numar: "))
    suma = x + y
    return suma


print(f'Suma celor doua numere este:{suma_a_doua_numere()}')

# Exertitiul 2
# Functie care returneaza TRUE pt nr par si FALSE pt nr impar


def par_impar():
    numar = int(input("Introduceti numarul pentru verificare: "))
    if numar % 2 == 0:
        return True
    else:
        return False


print(f'Numarul este par/impar? \ntrue = par \nfalse=impar \n{par_impar()}')

# Exercitiul 3
# Functie care returneaza nr de caractere din numele complet


def total_car():
    nume = input("Introduceti numele de familie: ")
    prenume_1 = input("Introduceti primul prenume:")
    prenume_2 = input("Introduceti al doilea prenume daca exista:")
    return len(nume + prenume_1 + prenume_2)


print(f'Numarul total de caractere al numelui tau este: {total_car()}')

# Exercitiul 4
# Functie care returneaza aria dreptunghiului


def aria_dreptunghiului():
    lungime = float(input("Introduceti lungimea dreptunghiului:"))
    latime = float(input("Introduceti latimea dreptunghiului:"))
    aria = lungime * latime
    return aria


print(f'Aria dreptunghiului este: {aria_dreptunghiului()}')


# Exercitiul 5
# Functie care returneaza aria cercului


def aria_cercului():
    r = float(input("Introduceti raza cercului:"))
    aria = r * r * 3.14
    return aria


print(f'Aria cercului este:{aria_cercului()}')

# Exercitiul 6
# Functie care returneaza daca un caractere se gaseste sau nu intr-un string dat


def gasire_caracter():
    string = input("introduceti stringul de la tastatura:")
    x = input("Introduceti caracterul care doriti sa fie gasit: ")
    if x.lower() in string.lower():
        return True
    else:
        return False


print(f'S-a gasit caracterul cautat? {gasire_caracter()}')


# Exercitiul 7
# returneza caracterele mici si mari


def lower_upper():
    string = input("Introduceti o propozitie/un sir de caractere/un cuvant: ")
    chr_up = 0
    chr_low = 0
    for i in string:
        if i.isupper():
            chr_up += 1
        elif i.islower():
            chr_low += 1
    print(f'Numarul de caractere mari este: {chr_up}')
    print(f'Numarul de caractere mici este: {chr_low}')


lower_upper()

# Exercitiul 8
# Functie care primeste o lista de nr si returneaza lista nr pozitive
lista = [4, 6, -9, -23, -40, 56, -7, 96, 2019, 2021]


def lista_nr_poz(li):
    lista_finala = []
    for nr in li:
        if nr > 0:
            lista_finala.append(nr)
    return lista_finala


print(lista_nr_poz(lista))


# Exercitiul 9
# Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.


def numere():
    x = int(input("Introduceti primul numar: "))
    y = int(input("Introduceti al doilea numar: "))
    if x > y:
        print(f'Primul numar {x} este mai mare decat al doilea numar {y}')
    elif x < y:
        print(f'Al doilea numar {y} este mai mare decat primul {x}')
    else:
        print("Numerele sunt egale.")


numere()

# Exercitiul 10
# Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False

set_numere = {7, 8, 26, 15, -9, -87, 46}


def seturi_numere(set_nr, nr):
    if nr in set_nr:
        print("Nu am adaugat numarul in set. Acesta exista deja.")
        return False
    else:
        set_nr.add(nr)
        print("Am adaugat numarul nou in set.")
        return True


print(seturi_numere(set_numere, 2019))
print(seturi_numere(set_numere, 8))