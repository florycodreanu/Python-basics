# Exercițiul 1
"""
- Afișeaz-o
- Inversează ordinea folosind slicing și suprascrie această listă.
- Printează varianta actuală (inversată).
- Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea.
 Nu trebuie să o suprascrii în acest caz deoarece metoda face asta automat.
- Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.
"""
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(f'Lista note_muzicale este: {note_muzicale}')
note_muzicale = note_muzicale[::-1]
print(f'Varianta actuala a listei note_muzicale este :{note_muzicale}')
note_muzicale.reverse()
print(f'Lista finala este: {note_muzicale}')

# Exercitiul 2
"""
De câte ori apare ‘do’?
"""
nr_aparitii = note_muzicale.count('do')
print(f'\nNota do apare de : {nr_aparitii} ori')

# Exercitiul 3
"""
Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Găsește 2 variante să le unești într-o singură listă.
"""
lista_1 = [3, 1, 0, 2]
lista_2 = [6, 5, 4]
b = lista_1.copy()  # Am copiat lista pentru a pastra listele initiale nemodificate
a = lista_1 + lista_2
print(f'\nVarianta clasica de concatenare a celor doua liste: {a}')
b.extend(lista_2)
print(f'O alta varianta de unire a celor doua liste este functia extend: {b}')

# Exercitiul 4
"""
● Sortează și afișază lista generată la exercițiul anterior.
● Sterge numărul 0 folosind o funcție.
● Afișaza iar lista.
"""
a.sort()
print(f'\n {a}')
a.remove(0)
print(a)

# Exercitiul 5
"""
Folosind un if verifică lista generată la exercițiul 3 și afișază:
● Lista este goală.
● Lista nu este goală.
"""

if len(a) == 0:
    print('\n Lista este goala')
else:
    print('\n Lista nu este goala.')

# Exercitiul 6
'''Folosește o funcție care să șteargă lista de la exercițiul 3.'''
a.clear()
print(f'\n {a}')

# Exercitiul 7
'''Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.'''
if len(a) == 0:
    print('\nLista este goala')
else:
    print('\nLista nu este goala.')

# Exercitiul 8
"""Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)"""
dict1 = {
    "Ana": 8,
    "Gigel": 10,
    "Dorel": 5}
print(f'\nElevii (cheile) din dictionar sunt: {dict1.keys()} ')

# Exercitiul 9
"""Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie"""
print(f'\nAna a luat nota {dict1["Ana"]}. \nGigel a luat nota {dict1["Gigel"]}. \nDorel a luat nota {dict1["Dorel"]}.')

# Exercitiul 10
"""Dorel a făcut contestație și a primit 6
● Modifică nota lui Dorel în 6
● Printează nota după modificare"""
dict1.update({"Dorel": "6"})
print(f'\nNota lui Dorel dupa contestatie este: {dict1.get("Dorel")}')

# Exercitiul 11
"""Gigel se transferă din clasă
● Căuta o funcție care să îl șteargă
● Vine un coleg nou. Adaugă Ionică, cu nota 9
● Printează noii elevi"""
dict1.pop("Gigel")
dict1["Ionica"] = 9
print(f'\n{dict1}')

# Exercitiul 12
"""Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
● Adaugă în zilele_sapt ‘luni’
● Afișeaza zile_sapt"""
luni = {'dec', 'ian', 'luni', 'vineri'}
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(f'\n{zile_sapt}')  # Nu se intampla nimic, deoarece valorile nu se repeta!

# Exercitiul 13
"""Folosește un if și verifică dacă:
● Weekend este un subset al zilelor din săptămânii.
● Weekend nu este un subset al zilelor din săptămânii."""
if weekend.issubset(zile_sapt):
    print('\nWeekend este un subset al zilelor săptămânii.')
else:
    print('\nWeekend nu este un subset al zilelor din săptămânii.')

# Exercitiul 14
"""Afișează diferențele dintre aceste 2 seturi."""
print(f'\nDiferenta dintre zile_sapt si weekend este:\n {zile_sapt.difference(weekend)} ')
# Daca incercam invers ne va returna un set gol.

# Exercitiul 15
"""Afișază intersecția elementelor din aceste 2 seturi."""
print(f'\nElementele care se regasesc in ambele seturi:\n{zile_sapt.intersection(weekend)}')