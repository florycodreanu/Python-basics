"""
1. Hello World + Comentarii
- Comentariile sunt bucati de cod care trebuie sa fie ignorate de catre sistem
- In general codul pe care il scriem noi este ca un limbaj gramatical pe care sistemul trebuie sa il interpreteze
- Daca noi scriem linii care nu corespund limbajului gramatical inteles de python, atunci sistemul va fi confuz,
si ca rezultat va returna eroare
- Ca sa evitam situatia asta putem sa ne folosim de comentarii, astfel incat sa ii spunem sistemului ca nu vrem
sa ii transmitem instructiuni ci vrem sa adaugam niste note personale care nu sunt de interes pentru rulare
- Daca pun em text invalid necomentat, ni se va returna eroarea: SyntaxError: invalid syntax
Exista doua tipuri de comentarii:
1. Comentarii multi line, reprezentate de trei ghilimele simple sau duble
2. Comentarii single line, reprezentate de semnul #
Acum suntem in interiorul unui comentariu multi line
"""

# Acum sunt in interiorul unui comentariu single line
# Daca vreau sa adaug mai multe linii comentate, fiecare linie va trebui precedata de semnul #
# Scurtatura pentru comentariile single line este CTRL + / (pe windows) sau COMMAND + / (pe mac)
# Putem sa comentam mai multe randuri cu single line comment in acelasi timp daca le selectam pe toate si apoi
# folosim scurtatura pentru comentariile single line


# Exercitiu print: vom printa in consola textul "Hello World"
# orice instructiune de scriere in consola se va face prin intermediul instructiunii print
# print este o FUNCTIE cu parametrii (vom studia conceptul de functii la cursul 5)
# Avem nevoie sa scriem intre paranteze informatia pe care vrem sa o printam
# Ca sa rulam codul, putem sa dam click dreapta oriunde in program si sa apasam butonul "Run"

print("Hello world")
print("Hello world on planet 'earth' ")
print('Hello world on planet "earth" ')
print('Hello world on planet \'earth\' ')  # caracterul \ pus inaintea unui caracter cu functie specifica
# schimba comportamentul acelui caracter si il marcheaza ca fiind necesar sa fie afisat pe eccran

"""
2. Variabile
- O variabila este o adresa de memorie in care putem stoca informatii
- Adresa de memorie este reprezentata de numele variabilei
- In momentul in care incercam sa printam o variabila pe ecran, in consola, de fapt incercam sa gasim adresa de memorie 
  care poarta numele variabilei si sa scoatem informatia de acolo cu scopul afisarii
- Ca si echivalent puteti sa va ganditi ca o variabila este doar o casa aflata la o anumita adresa
- Ii spunem variabila pentru ca valoarea de la adresa de memorie pe care o reprezinta se poate schimba
Reguli de baza pentru numirea variabilelor:
1. Trebuie sa inceapa cu litera mica
2. Trebuie sa nu aiba spatii - Daca numele variabilei este format din mai multe cuvinte, atunci numele variabilei poate 
  urma formatul camelCase sau snake_case 
3. Trebuie sa nu inceapa cu numere
4. Trebuie sa nu inceapa cu caractere speciale
"""

suntLaCurs = True  # am declarat si am initializat o variabila
# declararea reprezinta alocarea adresei de memorie reprezentata de numele specificat
# initializarea reprezinta stocarea unei valori la adresa de memorie rezervata anterior

# Intrebare: putem sa declaram o variabila in python fara sa o initializam? ex: suntLaCurs
# Raspuns: Nu, pentru ca python e loosely type, adica tipul de data este definit de valoarea pe care o initializam
# Daca nu specificam valoarea, atunci sistemul nu va sti cu ce tip de data trebuie sa lucreze

# Variabilele se pot suprascriere
# suprascriere = momentul in care schimbam valoarea de la adresa de memorie identificata prin numele variabilei

print(suntLaCurs)
# Daca nu folosim variabila inainte sa o redefinim primim warning: Redeclared 'suntLaCurs' defined above without usage
# suntLaCurs = False

suntLaCurs, imi_place_la_curs, simtCaInvat = True, "meh", "Oh Da"
# initializare multipla, adica pot sa enumar mai multe nume de variabile, si sa le dau valori in acelasi timp

print("Variabila 'suntLaCurs' este: " + str(suntLaCurs))
# Instructiunea asta va returna eroare: TypeError: can only concatenate str (not "bool") to str
# eroarea este returnata pentru ca nu putem sa concatenam o informatie de tip boolean cu o informatie de tip string
# ca sa rezolvam problema asta, avem doua solutii:
# 1. print cu formatare
# 2. type casting
print("Variabila 'imiPlace' este: " + imi_place_la_curs)
print("Variabila 'simtCaInvat' este: " + simtCaInvat)


"""
3. Tipuri de date
Un tip de data este o proprietate prin intermediul careia putem sa informam sistemul cu privire la ce tip de informatie 
        este salvat la adresa de memorie in cauza
Exista patru tipuri de date in python:
1. int = stocheaza numai numere intregi (pozitive sau negative)
2. float = stocheaza numai numere zecimale -> 2 va fi transformat in 2.0
3. boolean = stocheaza numai valori True sau False
4. string = stocheaza text de orice fel
In Java exista doua tipuri de stocare a textului:
1. cu tipul de data char (care este un tip de data primitiv) -> poate sa stocheze un singur caracter 
   - caracterul trebuie pus intre apostroafe
2. cu tipul de data String (care este un tip de data neprimitiv) -> Poate sa stocheze mai multe caractere 
   - caracterul trebuie pus intre ghilimele
In pyhton nu exista diferenta asta, adica nu avem char vs string. Indiferent daca punem textul intre ghilimele 
    sau apostroafe, tipul va fi tot string
"""

variabila_int = 123
variabila_float = 12.3  # ATENTIE! limitarea de zecimala se face cu caracterul ".", nu cu caracterul ","
variabila_bool_True, variabila_bool_false = True, False
variabila_string = "Suntem la curs"

"""
4. Funcția type() și type casting
- Functia type este o functie care returneaza tipul de data al unei variabile. 
        Analizeaza tipul de data al unei variabile si il trimite catre exterior
- Type casting inseamna o modalitate prin care putem sa schimbam tipul de data al unei variabile
        - type casting este TEMPORAR
"""

# Folosirea functiei type
print(type(variabila_string))
print(type(variabila_float))
print(type(variabila_bool_false))
print(type(variabila_bool_True))
print(type(variabila_int))

# Folosirea unui type casting
print(type(str(variabila_float)))
print(type(str(variabila_int)))
print(type(variabila_float))

variabila_float_convertita = str(variabila_float)

print(int(variabila_bool_True))
# instructiunea va printa pe ecran cifra 1 pentru ca boolean-ul True / False poate sa mai fie reprezentat
#      sub forma de 1 si 0
# print(int(variabila_string))
# instructiunea asta va returna eroare pentru ca castingul de la string la int este incompatibil:
# ValueError: invalid literal for int() with base 10: 'Suntem la curs'

print(float(variabila_int))
print(int(variabila_float))  # conversia de la float la int se face cu pierdere de date (elimina zecimalele)


"""
5. Funcția print() + concatenare + printare cu formatare
Concatentare - momentul in care vrem sa unim doua string-uri sa formam un alt string
    - concatenarea se poate face doar intre doua string-uri
    - concatenarea se face prin semnul "+" adaugat intre cele doua stringuri
    - daca incercam sa facem concatenare intre un string si un alt tip de data, vom primi eroare: 
    TypeError: can only concatenate str (not "<data type>") to str
    - ca sa rezolvam problema concatentarii intre doua tipuri de date incompatibile, avem doua solutii:
            1. type casting
            2. printare cu formatare
"""

#  1. Printare intre doua stringuri
catelulManancaPeste = "Adevarat"
catelulMuscaDacaIiFuriMancarea = "Adevarat"
variabileConcatenate = catelulManancaPeste + catelulMuscaDacaIiFuriMancarea
print("Catelul mananca peste? " + catelulManancaPeste + ". Catelul musca? " + catelulMuscaDacaIiFuriMancarea)

# 2. Printare intre doua tipuri incompatibile cu type casting
imi_e_foame = True
ce_fac_acum = "Sunt la curs, nu pot sa mananc"
# print("Imi e foame? " + imi_e_foame + " dar " + ce_fac_acum )
# returneaza eroare: TypeError: can only concatenate str (not "bool") to str
print("Imi e foame? " + str(imi_e_foame) + " dar " + ce_fac_acum)


# 2. Printare intre doua tipuri incompatibile cu formatare (adica marcarea var in interiorul stringului prin acolade)
imi_e_foame = True
ce_fac_acum = "Sunt la curs, nu pot sa mananc"
# print("Imi e foame? " + imi_e_foame + " dar " + ce_fac_acum )
# returneaza eroare: TypeError: can only concatenate str (not "bool") to str
print(f"Imi e foame? {imi_e_foame} dar {ce_fac_acum}")

# Alte exemple de formatare:
name = 'Johnny'
age = 55

# Formatarea inainte de python 3 se facea cu functia .format:
# Exemple:
print('Hi {}. You  are {} years old.'.format('Johnny', 55))
print('Hi {}. You  are {} years old.'.format(name, age))
print('Hi {new_name}. You  are {new_age} years old.'.format(new_name='sally', new_age=100))

"""
6. Assert
Assert este o modalitate prin care putem sa facem comparatii si sa decidem daca un rezultat este asteptat sau nu
Assert-ul poate avea patru componente:
- variabila care se compara
- operatorul de comparatie (==)
- variabila cu care se compara
- mesajul de eroare in cazul in care comparatia nu returneaza True
Comparatia tine cont de tipul de data
"""

imi_place_la_curs = True
assert imi_place_la_curs == True, "Error, error: studenti plictisiti"
print("Test passed, yeey, fac treaba buna la curs")

"""
7. Funcția input()
Functia input este o modalitate prin care putem sa introducem valori de la tastatura
Daca nu dam niciun parametru functiei, atunci nu ni se va afisa nimic pe ecran
        Optiunea asta NU este recomandata pentru ca utilizatorul nu va sti ce sa faca
Daca vrem sa dam parametri, trebuie specificati intre ghilimele sau apostroafe
By default tipul de date al unei valori date de la tastatura va fi string. 
!!! Atentie la incompatibilitati in caz de adunare 
"""
# Exercitiu: vrem sa calculam suma a doua numere date de la tastatura si sa afisam suma numerelor pe ecran
# a = int(input("introduceti primul numar "))
# b = int(input("introduceti al doilea numar "))
# print(a+b)
# a = float(input("introduceti primul numar "))
# b = input("introduceti al doilea numar ")
# print(a+b)
# instructiunea va da eroare pentru ca nu poate sa adune int si string:
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Eroarea va fi returnata pentru ca semnul "+" are o semnificatie diferita pentru int vs string
# La int inseamna adunare, la string inseamna concatenare
# a = int(input("introduceti primul numar ")) # daca introducem acum de la tastatura float, o sa returneze eroare:
# ValueError: invalid literal for int() with base 10: '15.34'


"""
avem o aplicatie bancara si vrem sa verificam daca la logare parola este corecta
Utilizatorul va fi indentificat pe baza de CNP. 
"""

parola_asteptata = "pass123"
utilizatorul_asteptat = "anton_batman"
cnp_asteptat = "5960123784521"
parola_introdusa = input("Va rugam sa introduceti parola: ")
cnp_introdus = input("Va rugam sa introduceti cnp-ul")
if cnp_asteptat == cnp_introdus:
    utilizatorul_introdus = utilizatorul_asteptat
    assert parola_asteptata == parola_introdusa, "Error:parola introdusa nu este corecta. Va rugam sa incercati din nou"
else:
    input("CNP-ul dumneavoastra nu a fost gasit, va rugam sa introduceti un utilizator")
    assert parola_asteptata == parola_introdusa, "Error:parola introdusa nu este corecta. Va rugam sa incercati din nou"