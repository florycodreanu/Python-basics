"""
Structuri repetitive = modalitati prin care putem sa executam o serie de statementuri (instructiuni)
de mai multe ori pana cand o anumita conditie nu mai este indeplinita
while = structura repetitiva, folosita atunci cand executam un set de instructiuni pe baza de conditie explicita
for = structura repetitiva care este folosita atunci cand vrem sa executam un set de instructiuni pe baza de range
for each = structura repetitiva care este folosita atunci cand vrem sa iteram prin elementele unei structuri de date
"""

""""
while = structura repetitiva care instruieste sistemul sa execute un set de instructiuni]
    atata timp cat o conditie este adevarata

Componentele unui while sunt:
1. instructiune de initializare a contorului (optional - doar daca se foloseste contor)
2. inceputul iteratiei (while)
3. conditia de iteratie
4. blocul de cod care sa se execute
5. instructiunea de incrementare a contorului / modificare a conditiei pentru a controla iteratia
"""

# Exercitiu 1: Vreau sa ii printez pe cei 101 dalmatieni pe ecran
i = 1
while i <= 101:
    print(f"Dalmatianul curent este: {i}")
    i += 1

# Exercitiu 2: vreau sa calculez suma tuturor numerelor de la 1 la 10
j = 1
suma = 0
while j <= 10:
    suma += j
    j += 1
else:
    print(f"Suma calculata printata din else este: {suma}")
# breakpoint = modalitate prin care putem sa anuntam sistemul ca trebuie sa opreasca executarea codului
# la o instructiune specifica
print(f"Suma calculata este: {suma}")

lista_studenti_incantati_de_while_for_a_while = ["marian", "andreea", 'andrei', "max", "ana", "maria"]
# Exercitiu 3: vreau sa printez pe ecran toti studentii din lista
s = 0
while s in range(len(lista_studenti_incantati_de_while_for_a_while)):
    print(f"Studentul curent este: {lista_studenti_incantati_de_while_for_a_while[s]}")
    s += 1

while s < len(lista_studenti_incantati_de_while_for_a_while):
    print(f"Studentul curent este: {lista_studenti_incantati_de_while_for_a_while[s]}")
    s += 1

"""
for = structura repetitiva care instruieste sistemul sa execute 
    un set de instructiuni atata timp cat un contor se afla intr-un range
componentele unui for:
1. contor de iteratie
2. range (start - optional <default 0>, end - obligatoriu, pas de incrementare- optional <> default 1)
3. set de instructiuni de executat				
"""

print("----------------FOR----------------")

# Exercitiu 1: Vreau sa ii printez pe cei 101 dalmatieni pe ecran -> cu start si pas default
# instructiune java: for(i = 0; i<=101; i++)
# instructiune python: for i in range(102)
for i in range(1, 102):
    print(f"Dalmatianul curent (bobita sau altcineva) este {i}")

# Exercitiu 2: Vreau sa calculez suma tuturor numerelor pare de la 0 la 10
# varianta 1 - cu if
suma = 0
for i in range(0, 11):
    if i % 2 == 0:
        print(f"Numarul {i} este par")
        suma += i
print(f"Suma numerelor pare cu if este {suma}")

suma_fara_if = 0
# varianta 2 - fara if
for i in range(0, 11, 2):
    print(f"Numarul {i} este par")
    suma_fara_if += i
print(f"Suma numerelor pare fara if este {suma_fara_if}")

print("EXERCITIU INTRO TO PROGRAMMING")
for i in range(1, 20, 3):
    print(i)

lista_studenti_confuzi_din_cauza_for = ["anton", "marta", "magda", "anastasia"]
# Exercitiu 3: Printarea studentilor din lista
for i in range(len(lista_studenti_confuzi_din_cauza_for)):
    index_curent = i
    print(f"Studentul curent este: {lista_studenti_confuzi_din_cauza_for[i]}")

# Exercitiu 4: Vrem sa il inlocuim pe anton cu marin:
for i in range(len(lista_studenti_confuzi_din_cauza_for)):
    if lista_studenti_confuzi_din_cauza_for[i] == "anton":
        lista_studenti_confuzi_din_cauza_for[i] = "marin"
print(f"Lista dupa update este: {lista_studenti_confuzi_din_cauza_for}")

"""
for each este o modalitate prin care putem sa iteram printr-o structura de date prin parcurgerea elementelor
Componentele unui foreach
1. Variabila / variabilelel de iteratie
2. structura pe care o parcurgem
3. instructiunile pe care sa le executam
"""

# Exercitiu 1: #Exercitiu 3: Printarea studentilor din lista de confuzi
for student in lista_studenti_confuzi_din_cauza_for:
    student_curent = student
    print(f"Studentul confuz curent este: {student}")

# Exercitiu 2: scoaterea lui marin din lista
for student in lista_studenti_confuzi_din_cauza_for:
    if student == "marin":
        lista_studenti_confuzi_din_cauza_for.remove(student)

print(f"Lista dupa scoaterea lui marin este: {lista_studenti_confuzi_din_cauza_for}")

# Exercitiu 3: vrem o inlocuim pe magda cu marco polo
for student in lista_studenti_confuzi_din_cauza_for:
    if student == "magda":
        lista_studenti_confuzi_din_cauza_for[lista_studenti_confuzi_din_cauza_for.index(student)] = "marco polo"

print(f"Lista dupa schimbarea martei cu marco polo este: {lista_studenti_confuzi_din_cauza_for}")

"""
Concluzie:
- for este mai util atunci cand vrem sa modificam o valoare in lista - pentru ca se acceseaza pe baza de index
- foreach este mai util atunci cand vrem sa scoatem un element din lista, pentru ca nu se calculeaza lungimea listei, 
    ci urmatorul element este accesat dinamic
"""

"""
break = statement care instruieste sistemul sa sara peste restul de iteratii ramase si sa iasa din bucla repetitiva
"""

date_plata_facturi = [1, 10, 15, 20, 25, 30]
data_plata_factura = 15
for i in range(len(date_plata_facturi)):
    print(f"Data de astazi este: {date_plata_facturi[i]}, in continuare mananaci la lumanare. Cumpara chibrituri")
    if date_plata_facturi[i] == data_plata_factura:
        print(f"Factura a fost platita in ziua de  {date_plata_facturi[i]}, nu mai mananci la lumanare")
        break

"""
continue = statement care instruieste sistemul sa sara peste iteratia curenta, nu peste celelalte iteratii
"""
# Exercitiu: vrem sa calculam suma numerelor impare
suma_1 = 0
for i in range(0, 11):
    if i % 2 == 0:
        continue
    suma_1 += i
print(f"Suma numerelor impare de la 0 la 10 este: {suma_1}")

"""
Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:
● Declară o Listă cu 5 jucători
● Schimbari_efectuate = te joci tu cu valori diferite
● Schimbari_max = 3
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea
- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișaza a intra x, a ieșit y, mai ai z schimbări
Dacă jucătorul nu e în teren:
- Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
teren’
- Afișază ‘mai ai z schimbări’
"""

lista_jucatori = ["j1", "j2", "j3", "j4", "j5"]  # "j2","j3","j4","j7","j8"
jucatori_scosi_de_pe_teren = []
lista_rezerve = ["j6", "j7", "j8"]  # "j6",
SCHIMBARI_MAX = 3
nr_schimbari_efectuate = 0  # 2
while nr_schimbari_efectuate < SCHIMBARI_MAX:
    jucator_care_iese = input("introduceti jucatorul care iese ")
    jucator_care_intra = input("introduceti jucatorul care intra ")
    if jucator_care_iese in lista_jucatori and jucator_care_intra in lista_rezerve:
        print(f"A intrat {jucator_care_intra} si a iesit {jucator_care_iese}")
        lista_jucatori.remove(jucator_care_iese)
        lista_rezerve.remove(jucator_care_intra)
        lista_jucatori.append(jucator_care_intra)
        jucatori_scosi_de_pe_teren.append(jucator_care_iese)
        nr_schimbari_efectuate += 1
        print(f"Mai aveti: {SCHIMBARI_MAX - nr_schimbari_efectuate} schimbari")
    elif jucator_care_iese not in lista_jucatori:
        print(f"Nu se poate efectua schimbarea deoarece jucătorul {jucator_care_iese} nu e în teren")
        print(f"Mai aveti: {SCHIMBARI_MAX - nr_schimbari_efectuate} schimbari")
    else:
        print(f"Nu se poate efectua schimbarea deoarece jucătorul {jucator_care_intra} nu e în lista de rezerve")

print(f"Jucatorii de pe teren la final de meci sunt: {lista_jucatori}")
print(f"Jucatorii care au fost scosi din teren sunt: {jucatori_scosi_de_pe_teren}")
print(f"Lista de rezerve la final de meci este: {lista_rezerve}")

# conditiile in care se poate efectua schimbarea sunt: jucatorul care iese este in teren,
# jucatorul care intra este in lista de rezerve
# avem mai putin de 3 schimbari efectuate

""" TEMA BONUS LA BONUS (rasplata ca ati fost cuminti): de la tema 2 - bonus,
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