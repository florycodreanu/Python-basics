""" TEMA BONUS LA BONUS (rasplata ca ati fost cuminti): de la tema 2 - bonus
rezolvati exercitiul cu zarul cu while, astfel incat sa ii oferiti utilizatorului trei incercati de a ghici numarul
contor: ghicit - false
iteratia 1:
if numar ghicit:  Ai ghicit. Felicitari! Numarul ales de tine e corect. ghicit = true
if numar mai mic: Ai ales un numar mai mic. Mai ai doua incercari
if numar mai mare: Ai ales un numar mai mare. Mai ai doua incercari
iteratia 2:
if numar ghicit:  Ai ghicit. Felicitari! Numarul ales de tine e corect. ghicit = true
if numar mai mic: Ai ales un numar mai mic. Mai ai o incercare
if numar mai mare: Ai ales un numar mai mare. Mai ai doua incercare
iteratia 3:
if numar ghicit: Ai ghicit. Felicitari! Numarul ales de tine e corect
la final de while, in afara while-ului evaluam contorul.
if true: Jocul s-a terminat. esti premiant
if false: Ai pierdut. Ai ales x dar a fost y
"""
import random

dice_roll = random.randint(1, 6)
ghicit = False
nr_incercari = 3
while nr_incercari > 0:
    numar = int(input('Ghiceste cat s-a dat cu zarul: '))
    if nr_incercari != 1:
        if numar == dice_roll:
            print('Ai ghicit. Felicitari! Numarul ales de tine este corect!')
            ghicit = True
            break
        elif numar < dice_roll:
            print(f'Ai ales un numar mai mic! Mai ai {nr_incercari-1} sanse!')
        else:
            print(f'Ai ales un numar mai mare! Mai ai {nr_incercari-1} sanse!')
    else:
        if numar == dice_roll:
            print('Ai ghicit. Felicitari! Numarul ales de tine este corect!')
            ghicit = True
            break
        elif numar < dice_roll:
            print(f'Ai ales un numar mai mic! Mai ai {nr_incercari-1} sanse!')
        else:
            print(f'Ai ales un numar mai mare! Mai ai {nr_incercari-1} sanse!')
    nr_incercari = nr_incercari - 1
if ghicit:
    print('Jocul s-a terminat. Esti premiant')
else:
    print(f"Ai ales {numar} dar a fost {dice_roll}")

"""
1. alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
"""
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)
print(f'Lista numere pare: {numere_pare}'
      f'\nLista numere impare : {numere_impare}'
      f'\nLista numere pozitive: {numere_pozitive}'
      f'\nLista numere negative{numere_negative}')

"""
2. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
"""
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(len(alte_numere)):
    for j in range(i + 1, len(alte_numere)):
        if alte_numere[i] > alte_numere[j]:
            swap = alte_numere[i]
            alte_numere[i] = alte_numere[j]
            alte_numere[j] = swap
print(f'Lista numere ordonate: {alte_numere}')

"""
3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr
Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!
"""
numar_secret = random.randint(1, 30)
numar_ghicit = None
while numar_ghicit is None:
    nr = int(input('Ghiciti numarul intre 1 si 30: '))
    if nr < numar_secret:
        print('Numarul secret este mai mare.')
    elif nr > numar_secret:
        print('Numarul secret este mai mic.')
    else:
        print('Felicitari! Ai ghicit numarul!')
        break

# """
# 4. Alege un număr de la tastatură
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# """
x = int(input('Introduceti un numar: '))
for i in range(1, x+1):
    print(f'{str(i)*i}')
    i += 1

"""
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
"""
tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]]
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta este: {tastatura_telefon[i][j]}')