from datetime import datetime, timedelta, date
# 1. Funcție care primește o lună din an și returnează câte zile are acea luna


def calendar(month):
    luni_an = {'Ianuarie': 31, 'Februarie': 28, 'Martie': 31, 'Aprilie': 30, 'Mai': 31, 'Iunie': 30, 'Iulie': 31,
               'August': 31, 'Septembrie': 30, 'Octombrie': 31, 'Noiembrie': 30, 'Decembrie': 31}
    if month in luni_an.keys():
        return luni_an.get(month)


luna = input('Introduceti luna: ')
print(f'Nr de zile ale lunii {luna} este: {calendar(luna.capitalize())}')

"""
Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
împărțirea a două numere.
În final vei putea face:
a, b, c, d = calculator(10, 2)
● print("Suma: ", a) ● print("Diferenta: ", b) ● print("Inmultirea: ", c) ● print("Impartirea: ", d)
"""


def calculator(x, y):
    suma = x + y
    dif = x - y
    prod = x * y
    div = x / y
    return suma, dif, prod, div


nr_1 = int(input('Introduceti primul nr: '))
nr_2 = int(input('Introduceti al doilea nr: '))
a, b, c, d = calculator(nr_1, nr_2)
print('Suma:', a)
print('Diferenta: ', b)
print('Produsul:', c)
print('Impartirea', d)

"""
3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""
lista1 = [1, 3, 1, 5, 9, 7, 7, 5, 5]
lista2 = [2, 5, 8, 4, 6, 4, 8, 7, 9, 6]


def numar_aparitii(lista):
    aparitii = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }
    for i in aparitii.keys():
        for j in lista:
            if i == j:
                aparitii[i] = aparitii[i] + 1
    return aparitii


print(numar_aparitii(lista1))
print(numar_aparitii(lista2))

"""
4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
"""


def maxim(x, y, z):
    if z == x == y:
        return 'Numerele sunt egale'
    elif y >= x and y >= z:
        m = y
    elif x >= y and x >= z:
        m = x
    else:
        m = z
    return m


a = int(input('Introduceti primul numar a = '))
b = int(input('Introduceti al doilea numar b = '))
c = int(input('Introduceti al treilea numar c = '))
print(f'Maximul dintre cele trei numere este: {maxim(a, b, c)}')

"""
5. Funcție care să primească un număr și să returneze suma tuturor numerelor
de la 0 la acel număr
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
"""


def suma_nr(n):
    s = 0
    for i in range(n + 1):
        s = s + i
    return s


nr = int(input('Introduceti un numar: '))
print(f'Suma tuturor numerelor de la 0  la {nr} este: {suma_nr(nr)}')

# Exercitii optionale bonus
"""
1. Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune.
Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
"""
l1 = [1, 1, 2, 3]
l2 = [2, 2, 3, 4]


def intersect(list1, list2):
    list1 = set(list1)
    list2 = set(list2)
    return list1.intersection(list2)

print(intersect(l1, l2))

"""
2.. Funcție care să aplice o reducere de preț
Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
invalidă.
"""


def red_pret(pret, red):
    if red > 100:
        return 'Reducere invalida'
    elif red < 0:
        return 'Reducere invalida'
    else:
        pret_redus = pret - red / 100 * pret
    return pret_redus


price = float(input('Introduceti pretul: '))
sale = float(input('Introduceti reducerea: '))
print(red_pret(price, sale))

"""Funcție care să afișeze data și ora curentă din ro
(bonus: afișați și data și ora curentă din China)"""


def datasiora():
    romania = datetime.now()
    china = datetime.now() + timedelta(hours=6)
    print(f' Data si ora curenta in Romania este {romania}')
    print(f' Data si ora curenta in China este {china}')


datasiora()

""" Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
Crăciun dacă nu vrei să ne zici cand e ziua ta :)"""


def party(year):
    birthday = date(year, 2, 26)
    days_til_birthday = (birthday - date.today()).days
    print(f'Pana la ziua mea mai sunt {days_til_birthday} zile')


party(2023)