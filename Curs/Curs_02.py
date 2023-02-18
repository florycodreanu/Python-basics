import math
"""
1. SLICING
Slicing inseamna o modalitate prin care putem extrage bucati dintr-un string
Slicing se face pe baza de range care este compus din urmatoarele elemente:
- pozitie de start - implicit o sa fie 0 - > adica se printeaza de la inceput
- pozitie de end - implicit o sa fie finalul stringului
- pas (adica cate caractere sa sara sistemul) - implicit o sa fie pas de 1 - adica se va printa fiecare caracter
In orice string caracterele sunt identificabile prin intermediul unui index
La slicing nu se ia in considerare capatul superior al intervalului
        Daca specificam intervalul [1:4] se vor printa caracterele de la pozitia 1 pana la pozitia 3
        In general prima pozitie dintr-un string se afla la indexul 0
"""

# Text de utilizat:
import re

poezie = "Ana are mere si, este vesela pentru ca este luni"

# Exercitiu 1: Extrageti toate caracterele de la inceput pana la sfarsit, cu specificarea pozitiei
print(poezie[0:len(poezie)])
# Exercitiu 2: Extrageti toate caracterele de la inceput pana la sfarsit, folosind pozitia implicita
print(poezie[:])
# Exercitiu 3: Extrageti toate caracterele de la inceput pana la sfarsit, alegand caracterele din 2 in 2
print(poezie[0:len(poezie):2])
print(poezie[::2])
# Exercitiu 4: Extrageti toate caracterele de la pozitia 5 pana la pozitia 13 inclusiv
print(poezie[5:14])
# Exercitiu 5: Extrageti ultimele 3 caractere de la final
print(poezie[len(poezie)-3:len(poezie)])
print(poezie[-3:])
# Exercitiu 6: Printam string-ul in ordine inversa
print(poezie[::-1])

"""
Metode ce pot fi utilizate cu string-uri
"""
print(poezie.split(sep=","))  # metoda split este o metoda care sparge string-ul pe bucati
# rezultatul va fi o lista de elemente
# split-ul se va face la fiecare cuvant
print(poezie.replace('A', 'm'))
print(poezie.upper().replace('A', 'm'))
print(poezie.index("A"))  # returneaza prima pozitie a caracterului specificat intre paranteze
print(poezie.index("a"))  # returneaza prima pozitie a caracterului specificat intre paranteze
print(poezie.find('a'))  # Face acelasi lucru ca functia index
print(poezie.isnumeric())  # Verifica daca toata caracterele dintr-un string sunt numere
str_numeric = '136802'
str_numeric_v1 = 'Ana are 3 mere'
print(str_numeric.isnumeric())
print("-----------------")
print(re.search(r'\d', str_numeric_v1))
print(poezie.count("t"))  # Numara de cate ori apare caracterul din paranteze in string
# Diferenta intre isDigit(), isNumeric(), isDecimal():
# https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-python
string_capitalize = 'ana are mere si, este vesela pentru ca este luni'
print(string_capitalize.capitalize())  # marcheaza prima litera cu litera mare
print(poezie.startswith("Ana"))
print(poezie.endswith("luni"))

"""
2. OPERATORI
Operatori sunt elemente prin intermediul carora putem efectua operatii cu variabilele
Operatorii pot fi de patru tipuri:
- De atribuire - Sunt operatori prin care putem sa salvam o valoare intr-o variabila
- Aritmetici - Sunt operatori prin care putem efectua operatii matematice
- De comparare - Sunt operatori prin care putem sa comparam valoarea a doua variabile
- Logici - Sunt operatori cu care putem efectua conditii compuse
Atribuire = proces prin care salvam informatii la adresa de memorie identificata cu un nume al unei variabile,
indiferent de tipul de date al acesteia. Atribuirea initiala se numeste initializare

Operatorii de asignare sunt: = , += , -= , *= , /=
"""

# A. ASSIGNMENT OPERATORS
# A.1 -> operatorul = -> atribuie o noua valoare unei variabile
# Exemple:
valoare_produs = 53  # am atribuit valoare 53 variabilei valoare_produs
print(f"Valoarea initiala a produsului este {valoare_produs}")
valoare_produs += 7  # la valoarea anterioara se adauga valoarea 7, iar rezultatul final este suprascris in variabila
# este echivalentul instructiunii valoare_produs = valoare_produs + 7
print(f"Valoarea dupa adunare cu operatorul += a produsului este {valoare_produs}")
valoare_produs -= 7  # din valoarea anterioara se scade valoarea 7, iar rezultatul final este suprascris in variabila
print(f"Valoarea dupa scadere cu operatorul -= a produsului este {valoare_produs}")
valoare_produs *= 2  # valoarea anterioara se va inmulti cu 2, iar rezultatul final este suprascris in variabila
print(f"Valoarea dupa inmultire cu operatorul *= a produsului este {valoare_produs}")
valoare_produs /= 2  # valoarea anterioara se va imparti la 2, iar rezultatul final este suprascris in variabila
print(f"Valoarea dupa impartire cu operatorul *= a produsului este {valoare_produs}")

# B. ARITHMETIC OPERATORS
# B.1 OPERATORUL + (ATENTIE! daca este aplicat pe numere, va face suma numerelor
# daca este aplicat pe string, va face concatenare)
nr_1 = 5
nr_2 = 10
print(f'Suma este {nr_1 + nr_2}')  # esta echivalentul metodei sum(nr_1,nr_2)
str_1 = "Ana"
str_2 = " mere"
print(f'String-urile concatenate sunt: {str_1 + str_2}')
print(f'String-urile concatenate sunt: {str_1}' + " " + str_2)

# B.2 OPERATORUL -
nr_1 = 10
nr_2 = 6
print(f'Diferenta intre cele doua numere este: {nr_1 - nr_2}')

# B.3 OPERATORUL *
print(f"Inmultirea celor doua numere este: {nr_1 * nr_2}")

# B.3 OPERATORUL /
print(f"Impartirea celor doua numere este: {nr_1 / nr_2}")  # ATENTIE! operatorul impartire returneaza rezultat float

# B.4 OPERATORUL % (MODULO)
print(f"Restul impartirii lui {nr_1} la {nr_2} este {nr_1 % nr_2}")

# B.4 OPERATORUL // (FLOOR DIVISION) -> taie zecimalele din rezultatul float
print(f"Rezultatul intreg al impartirii lui {nr_1} la {nr_2} este {nr_1 // nr_2}")
print(f"Rezultatul intreg al impartirii lui {nr_1} la {nr_2} este " + str(int(nr_1 / nr_2)))

# B.5 OPERATORUL ** -> (RIDICAREA LA PUTERE)
print(f"{nr_1} ridicat la puterea {nr_2} este {nr_1 ** nr_2}")
nr_radical = 36
print(f"Radical din 36 este {math.sqrt(36)}")
# nu exista operator pentru square root. Functia sqrt returneaza numar zecimal

# C. COMPARISON OPERATORS
# C.1 OPERATORUL == (ATENTIE!!! A nu se confunda cu operatorul de atribuire "=")
# operatorii de comparatie returneaza un rezultat boolean
nr_1 = 5
nr_2 = 6
print(nr_1 == nr_2)

# C.2 OPERATORUL <=
print(nr_1 <= nr_2)

# C.3 OPERATORUL >=
print(nr_1 >= nr_2)

# C.4 OPERATORUL <
print(nr_1 < nr_2)

# C.5 OPERATORUL >
print(nr_1 > nr_2)

# C.5 OPERATORUL !=
print(nr_1 != nr_2)

# D. OPERATORII LOGICI (AND OR NOT)
# NOT > AND > OR
nr_2 = 6
nr_1 = 7
print(nr_1 > nr_2 or nr_1 == nr_2)  # nr_1 > nr_2 = FALSE  nr_1 == nr_2 = FALSE => FALSE
print(nr_1 > nr_2 or nr_1 < nr_2)   # nr_1 > nr_2 = FALSE  nr_1 < nr_2 = TRUE => TRUE
print(nr_1 > nr_2 and nr_1 < nr_2)  # nr_1 > nr_2 = FALSE  nr_1 < nr_2 = TRUE => FALSE
print(not nr_1 > nr_2 and nr_1 < nr_2)  # not nr_1 > nr_2 = FALSE nr_1 < nr_2  = FALSE -> FALSE AND FALSE = FALSE
print(not (nr_1 > nr_2 and nr_1 < nr_2))
# nr_1 > nr_2 = TRUE  nr_1 < nr_2 = FALSE  - TRUE AND FALSE = FALSE -> NOT FALSE  = TRUE


"""
3. Structura alternativa IF
If-ul este o structura alternativa prin intermediul careia putem sa executam 
un set de instructiuni sau un altul in functie de rezultatul evaluarii unei conditii
Componentele unui if(decizie) sunt:
- inceputul deciziei (IF)
- ramura din dreapta a deciziei (THEN) -> in python este reprezentat de primul set de instructiuni dupa ":"
- ramura din stanga a deciziei (ELSE) - executata cand conditia este evaluata ca FALSE 
    -> in python reprezinta al doilea set de instructiuni, plasate dupa semnul ":" de la else
- elif -> o situatie alternativa definita de un alt set de conditii atunci cand avem mai multe situatii posibile
In orice structura alternativa sau repetitiva, blocul de cod care trebuie executat se marcheaza cu indentare
indentare = spatiul lasat intre marginea fisierului si linia de cod
"""

"""
Exercitiu:
If a client has over 65 years, then it will be offered to him a discount of 15%.
Otherwise if the customer does not have over 65 years, if the person travels with at least one child 
                    they will have a discount of 10%
For both seniors and non seniors it will be applied an additional discount of 10% 
                    if they will travel during winter.
Also, for both seniors and non seniors it will be applied a 3% luxury fee if they 
                    will travel in the first class (in any season) 
                    or 1% handling fee otherwise.
"""

# input = informatii care trebuie citite de la tastatura si pasate in program
varsta = int(input("Va rugam sa introduceti varsta "))
season = input("Va rugam sa introduceti anotimpul de calatorie ")
clasa = int(input("Va rugam sa introduceti clasa la care calatoriti: 1 / 2 "))
price = int(input("Va rugam sa introduceti pretul biletului "))
discount = 0
if varsta > 65:
    discount = 0.15
else:
    nr_child = int(input("Va rugam sa introduceti numarul de copii "))
    if nr_child > 0:
        discount = 0.1
if season == 'iarna':
    discount += 0.1
if clasa == 1:
    tax = 0.03
else:
    tax = 0.01
price = price - price * discount + price*tax
print(discount, tax, price)

"""
pret total: 10
discount = 0.25
tax = 0.3
pret ramas: 10 - 2.5 = 7.5 + 0.3 = 7.8
"""

"""
Exista in conceptele de testare doua categorii de tehnici de testare:
- testare blackbox -> testare fara acces la cod (frontend)
- testare whitebox -> testare cu acces la cod (backend)
Tehnici de testare whitebox: 
- Statement coverage -> tehnica de testare ce arata de cate teste avem nevoie pentru a putea executa cel putin o data 
   fiecare instructiune (statement) din cod
- Decision coverage -> tehnica de testare ce arata de cate teste avem nevoie pentru a putea executa cel putin o 
   data fiecare ramura decizionala din cod
- Path coverage -> tehnica de testare ce arata de cate teste avem nevoie pentru a putea executa cel putin o data 
   toate caile posibile din cod
In general pentru tehnicile whitebox, se creeaza scheme pe baza urmatoarelor elemente logice:
- nod (start / end  (optionale) -> semicerc, input -> paralelogram, statement -> dreptunghi, decizion -> romb)
- linie -> care uneste doua noduri
Scenarii necesare pentru a avea 100% statement coverage:
- persoana peste 65 de ani care calatoreste iarna la clasa 1
- persoana sub 65 de ani cu copil care calatoreste in alt sezon decat iarna la clasa a 2-a
Scenarii necesare pentru a avea 100% decision coverage:
- persoana peste 65 de ani care calatoreste iarna la clasa 1
- persoana sub 65 de ani cu copil care calatoreste in alt sezon decat iarna la clasa a 2-a
- persoana sub 65 de ani, fara copil care calatoreste in alt sezon decat iarna la clasa a 2-a
Concluzia: 
1. Avem nevoie de 2 teste pentru a avea 100% statement coverage si de 3 pentru a avea 100% decision coverage
2. Decision coverage este mai acoperitor decat statement
statement coverage < decision coverage < path coverage < condition coverage
Test case pentru acoperirea scenariului 1 de la statement coverage si respectiv scenariului 1 de la decision coverage
Test condition = Descriere a unei functionalitati pe care o testam (Ce testam)
Test case = Descriere pas cu pas a felului in care testam o functionalitate (Cum testam)
Summary (Test Condition): Verifica faptul ca pentru o persoana peste 65 de ani care calatoreste iarna la clasa 1 
se aplica discount de 25% si taxa de 3%
Pasi de reproducere:
1. Intra in aplicatia booking
2. Cauta cazare
3. Bifeaza parametrul de varsta peste 65 de ani
4. Bifeaza anotimpul "iarna"
5. Bifeaza checkbox-ul de clasa 1
Rezultate asteptate:
Pretul final al calatorului este redus cu 25% din pretul initial 
O taxa de 3% din pretul initial este calculata
"""