import random
# 1. Verifica dacă x are minim 4 cifre (x e int).

x = int(input('Introduceti un numar intreg: '))
if x/1000 >= 1 or -x/1000 >= 1:
    print('Numarul contine cel putin 4 cifre')
else:
    print('Numarul contine mai putin de 4 cifre')

# 2. Verifică dacă x are exact 6 cifre.
x = int(input('Introduceti un numar intreg: '))
if x < 0:
    x = -x
if len(str(x)) == 6:
    print('Numarul are exact 6 cifre')
else:
    print('Numarul nu are exact 6 cifre ')

# 3. Verifica daca x este numar par sau impar
x = int(input('Introduceti un numar intreg: '))
if x % 2 == 0:
    print('Numarul este par!')
else:
    print('Numarul este impar')

# 4.Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre ele
x = int(input('Introduceti un numar intreg: x = '))
y = int(input('Introduceti un numar intreg: y = '))
z = int(input('Introduceti un numar intreg: z = '))
if x > y and x > z:
    print(f'Variabila x = {x} este cea mai mare!')
elif y > x and y > z:
    print(f'Variabila y = {y} este cea mai mare!')
elif z > x and z > y:
    print(f'Variabila z = {z} este cea mai mare!')
else:
    print('Numerele sunt egale.')

# 5. x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca triunghiul este valid sau nu
x = int(input('Introduceti un unghiul x = '))
y = int(input('Introduceti un unghiul y = '))
z = int(input('Introduceti un unghiul z = '))
if x > 0 and y > 0 and z > 0 and x + y + z == 180:
    print('Triunghiul este valid')
else:
    print('Triunghiul nu este valid')

# 6.Avand stringul: 'Coral is either the stupidest animal or the smartest rock' citește de la tastatura un număr x
# de tip int și afișează stringul fără ultimele x caractere.
prop = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Introduceti cate caractere sa taiem x = '))
print(prop[0:len(prop)-x])

# 7.Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format din primele 5 caractere
# + ultimele 5
prop = 'Coral is either the stupidest animal or the smartest rock'
uniune = prop[0:5] + prop[-5:len(prop)]
print(uniune)

# 8.același string de la exercițiul 6, salvează într-o variabila și afiseaza indexul de start al cuvântului rock
# Folosind aceasta variabila + slicing,afișează tot stringul pana la acest cuvant.
# Output asteptat: 'Coral is either the stupidest animal or the smartest '
prop = 'Coral is either the stupidest animal or the smartest rock'
index = prop.index("rock")
print(f'Indexul cuvantului \"rock\" este : {index}')
print(f'Rezultat : {prop[:index]}!')

# 9.Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se
# va folosi un assert. Atentie: se dorește ca programul sa fie case insensitive, adica 'apA'
# e acceptat ca un string in care primul si ultimul caracter este la fel
prop = input('Introduceti un string: ')
assert prop.casefold()[0] == prop.casefold()[-1], 'Caracterele nu sunt identice'
print('Caracterele sunt identice!')

# 10. Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare
numere = '0123456789'
print(f'Numerele pare sunt: {numere[::2]}')
print(f'Numerele impare sunt: {numere[1::2]}')

""" 11. Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept inputuri urmatoarele
informatii:
 a.Varsta b.Insotit de mama c.Insotit de tata d.Pasaport e.Act permisiune mama f.Act permisiune tata
# Conditii de imbarcare:
1.Daca pers are varsta peste 18 ani si are pasaport
2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
3. Daca are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune scrisa de la celalat parinte
Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate
variantele care crezi ca ar trebui testate. Genereaza scenarii de testare cu expected results si
apoi ruleaza codul pentru a verifica daca expected results sunt egale cu actual results.
"""
varsta = int(input('Introduceti varsta: '))
pass_valid = input('Aveti pasaport valid? Da/Nu: ')

if varsta >= 18 and pass_valid.capitalize() == 'Da':
    print('Va puteti imbarca! Calatorie placuta!')
elif varsta < 18 and pass_valid.capitalize() == 'Da':
    parinti = input('De cine este copilul insotit? Mama, Tata sau Ambii parinti?: ')
    if parinti.capitalize() == 'Ambii parinti':
        print('Va puteti imbaraca! Calatorie placuta!')
    elif parinti.capitalize() == 'Tata':
        permisiune_mama = input('Aveti permisiune de la mama? Da/Nu: ')
        if permisiune_mama.capitalize() == 'Da':
            print('Va puteti imbaraca! Calatorie placuta!')
        else:
            print('Ne pare rau, nu va puteti imbarca!')
    elif parinti.capitalize() == 'Mama':
        permisiune_tata = input('Aveti permisiune de la tata? Da/Nu: ')
        if permisiune_tata.capitalize() == 'Da':
            print('Va puteti imbaraca! Calatorie placuta!')
        else:
            print('Ne pare rau, nu va puteti imbarca!')
    else:
        print('Ne pare rau, nu va puteti imbarca!')
else:
    print('Ne pare rau, nu va puteti imbarca!')

"""
Scenarii posibile:
1. Adult peste 18 ani, pasaport valid ==> Va puteti imbaraca! Calatorie placuta!
2. Adult peste 18 ani, pasaport invalid ==> Ne pare rau, nu va puteti imbarca!
3. Copil cu pass valid si ambii parinti ==> Va puteti imbaraca! Calatorie placuta!
4. Copil cu pass valid - un parinte - permisiunea celuilalt existenta ==> Va puteti imbaraca! Calatorie placuta!
5. Copil cu pass valid - un parinte - permisiunea celuilalt parinte lipsa ==> Nu se poate imbarca!
6. Copil cu pass valid fara parinti ==> Nu se poate imbarca
7. Copil fara pasaport valid ==> Nu se poat imbarca 
"""

"""
12.Joc de noroc
- Cauta pe net si vezi cum se genereaza un numar random
- Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll.
Numarul salvat va fi generat random cu metoda gasita in online
- Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator
- Verifica si afiseaza daca utilizatorul a ghicit numarul
- Vor exista 3 optiuni care vor trebui tratate:
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari! Ai ales x si zarul a fost y
"""

dice_roll = random.randint(1, 6)
numar = int(input('Ghiceste cat s-a dat cu zarul: '))
if numar < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {numar} si a fost {dice_roll}')
elif numar > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {numar} si a fost {dice_roll}')
else:
    print(f'Ai ghicit! Felicitari! Ai ales {numar} si a fost {dice_roll}')