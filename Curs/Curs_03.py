"""
Structurile de date reprezinta adrese de memorie care stocheaza mai multe valori
Exista patru tipuri de structuri:
- liste
- tupluri
- seturi
- dictionare
"""


"""
1. Liste = structuri de date ordonate multitype (ATENTIE!!! DOAR IN PYTHON SUNT MULTITYPE) ordonate,
care permit duplicate si respectiv adaugarea si stergerea de elemente
"""

"""
Declararea unei liste = alocarea unui spatiu de memorie care sa poarte numele listei
# O lista poate sa fie declarata initial cu elemente sau fara
Declararea unei liste se face prin numele listei si un set de paranteze patrate
"""

# 1. Declarare lista cu elemente de tip string
lista_studenti_prezenti_astazi = ["max", "vlad", "andreea", "andrei", "cezar"]

# 2. Declarare lista cu elemente multitype
lista_multitype = ["string", 12, True, 15.75]

# 3. Declarare lista goala
lista_animalute = []
print(f"Lungimea listei este: {len(lista_studenti_prezenti_astazi)}")

"""
Accesarea elementelor din lista - se poate face pe baza de index pentru 
ca lista este ordonata
"""
print(f"Primul student din lista este {lista_studenti_prezenti_astazi[0]}")

"""
Functii care se pot folosi impreuna cu listele
Pentru a vedea care sunt toate functiile ce se pot folosi in legatura cu o lista punem:
numele listei urmat de caracterul "."
"""
# 1. Functia index -> care returneaza pozitia exacta a elementului in lista
print(f"Pozitia lui Max este: {lista_studenti_prezenti_astazi.index('max')}")
# Pe baza indexului putem sa accesam elementele din lista.

modifica_student_in_grupa = "max"
intro_student_in_grupa = "anton"
adauga_student_in_grupa = "marian"
adauga_student_la_pozitie = "maria"
lista_studenti_prezenti_astazi[lista_studenti_prezenti_astazi.index("max")] = intro_student_in_grupa
lista_studenti_prezenti_astazi.append(adauga_student_in_grupa)
lista_studenti_prezenti_astazi.insert(2, adauga_student_la_pozitie)

# 2. Functii pentru adaugare
# 2.a Functia append -> Este o functie care adauga elemente la final
lista_animalute.append("Catel")
lista_animalute.append("Pisica")
print(f"Lungimea dupa append a listei goale este {len(lista_animalute)}")
lista_animalute.append("Porcusor de Guineea")
print(f"Lista curenta este {lista_animalute}")

# 2.b Functia insert -> Este o functie care adauga un element la o anumita pozitie
lista_animalute.insert(1, "Hamster")
lista_animalute.insert(2, "Sinsila")
print(f"Lista de animalute care include si hamsterul si sinsila este {lista_animalute}")

# 3. Functii pentru stergere elemente:
# 3.a Functia remove -> Este folosita pentru a sterge elemente pe baza valorii lor
lista_animalute.remove("Hamster")

# 3.b Functia pop -> Este folosita pentru a sterge elemente pe baza indexului lor
lista_animalute.pop(0)
print(f"Lista dupa stergere prin remove si pop este {lista_animalute}")

# 4. Functia count -> numara de cate ori apare un anumit element in lista
print(f"Sinsila apare in lista de {lista_animalute.count('Sinsila')}")

# 5.Functia extent -> Adauga elementele din lista din paranteze la o a doua lista
lista_animalute.extend(lista_studenti_prezenti_astazi)
print(f"Lista rezultata este {lista_animalute}")

# 6.Functia copy -> creeaza o copie a unei liste
print(lista_animalute.copy())
print(f"Lista initiala este {lista_animalute}")

# 7. Functia sort -> sorteaza elementele in ordine alfabetica in functie de codul ASCII:
# https://infoas.ro/lectie/90/codul-ascii-tabel-complet
lista_animalute.sort()
print(lista_animalute)

# 8. Functia reverse -> modifica pozitia elementelor in ordine inversa
lista_animalute.reverse()
print(f"Lista dupa reverse este: {lista_animalute}")

# 9. Functia clear sterge toate elementele din lista
lista_animalute.clear()
print(f"Lista animalute dupa clear este: {lista_animalute}")

print(f"Prima litera a numelui max este {lista_studenti_prezenti_astazi[0][0]}")

"""
2. Tupluri
Tuplurile reprezinta structuri de date care stocheaza elemente ordonate pe baza de index
si care nu se pot modifica de-a lungul timpului - immutabile (immutable) -> care inseamna ca
dupa crearea tuplului, nu vom mai putea modifica elemente in interiorul lui
Declararea tuplurilor se face prin numele tuplului urmat de un set de paranteze rotunde
"""

# declararea unui tuplu:
echipa_sah = ("max", "vlad", "andreea", "andrei", "cezar")

# accesarea unui element dintr-un tuplu:
print(f"Al treilea membru al echipei de sah este: {echipa_sah[2]}")

# Functii care se pot folosi cu tuplurile:
# 1. Functia count -> numara de cate ori apare un element in lista
print(f"Echipa de sah este format din {echipa_sah.count('andreea')} fete cu numele \"Andreea\"")
# \ se numeste caracter escape

# Alt exemplu pentru caracterul escape
print('Suntem la curs,\nne place extrem de mult,\no iubim pe Gabriela maxim \nsi o bagam in buzunar la interviu')
# \n caracterul escape pentru endline

# 2. Functia index -> arata pozitia la care se afla un anumit element
print(f"Pozitia lui Cezar in lista este {lista_studenti_prezenti_astazi.index('cezar')}")

"""
Seturi
Seturile reprezinta structuri de date NEORDONATE (adica nu sunt identificabile prin index). 
In general seturile pot sa fie modificate cu scopul de a adauga sau sterge elemente, dar nu pot fi modificate cu 
scopul de a schimba valoarea de la o anumita pozitie
Declararea unui set se face print intermediul numelui setului si a unei perechi de acolade
"""

set_pisici = {"tom", "silvester", "garfield", "katia", "kedi"}

# Accesarea elementelor din set
# 1. prin intermediul unei structuri repetitive (foreach)
for pisica in set_pisici:
    print(pisica)

# 2. Prin intermediul operatorului in
print("tom" in set_pisici)

# Functii care pot fi folosite cu seturile
# 1. Functia pop
# set_catei = {}
# set_pisici.pop()
# print(f"Set pisici dupa pop este: {set_pisici}")
# set_catei.pop()  -> returneaza TypeError: pop expected at least 1 argument, got 0 -> pentru ca setul de catei este gol

# 2. Functia remove sterge un element din lista in functie de valoare
set_pisici.remove("tom")
print(f"Set pisici dupa eliminarea lui tom este {set_pisici}")

set_pisici_moderne = {"tom", "silvester", "garfield", "katia", "kedi", "jinx"}

# 3. Functia subset verifica daca un set este o parte dintr-un alt set, sau o subdiviziune a unui set
print(f"Vrem sa stim daca setul pisici este un subset al pisicilor moderne {set_pisici.issubset(set_pisici_moderne)}")

# 3. Functia add adauga un nou element in set
set_pisici.add("jinx")
print(f"Setul de pisici dupa adaugarea lui Jinx este {set_pisici}")

# Daca incercam sa adaugam un duplicat, sistemul NU VA DA EROARE, dar nici nu va adauga elementul
set_pisici.add("garfield")
print(f"Setul dupa incercarea de readaugare a lui garfield este {set_pisici}")

# 4. Functia intersection returneaza un subset care contine toate elementele prezente in ambele seturi
print(f"Intersectia dintre cele doua seturi este: {set_pisici.intersection(set_pisici_moderne)}")

# 5. Functia differente returneaza un subset care contine toate elementele care se afla in setul de la care se pleaca,
# dar nu si in setul dat ca parametru
print(f"Diferenta intre set_pisici_moderne si set_pisici este {set_pisici_moderne.difference(set_pisici)}")
print(f"Diferenta intre set_pisici si set_pisici_moderne este {set_pisici.difference(set_pisici_moderne)}")

# 6. Functia superset verifica daca un set contine toate elementele dintr-un alt set + altceva
print(f"Aflam daca set_pisici_moderne este un superset pt set_pisici: {set_pisici_moderne.issuperset(set_pisici)}")

# 7. Functia union returneaza o combinatie intre doua seturi diferite
print(f"Uniunea intre cele doua liste este: {set_pisici.union(set_pisici_moderne)}")

# 8. Functia clear -> sterge toate elementele din set
set_pisici.clear()
print(f"Setul dupa functia clear este {set_pisici}")

"""
Dictionare -> Seturi de date ordonate stocate in perechi cheie:valoare
Cheile trebuie sa fie unice, dar valorile se pot repeta
Situatie acceptata:
"varsta":"25",
"numarPrieteni":25
Situatie neacceptata:
"numarPrieteni":"1",
"numarPrieteni":25
Declararea dictionarelor se face pe baza acoladelor
"""

# Declarare dictionar
fotbalisti = {
    "Gica Hagi": 10,
    "Cristiano Ronaldo": 7,
    "Adrian Mutu": 10,
    "Kilian Mbape": 9,
    "Karim Benzema": 5,
    "Lionel Messi": 3,
    "Jordi Alba": 2,
    "Alvaro Morata": 6
}

# Accesare elemente dictionar
print(f"Numarul de pe tricoul lui ronaldo este: {fotbalisti.get('Cristiano Ronaldo')}")
print(f"Numarul de pe tricoul lui ronaldo este: {fotbalisti['Karim Benzema']}")

# Adaugare elemente in dictionar
fotbalisti["Henry"] = 15
fotbalisti["Anton Tatarusanu"] = 12
fotbalisti["Cristian Chivu"] = 8
print(f"Dictionarul curent este {fotbalisti}")
print(f"Dictionarul curent este {fotbalisti.items()}")


# Accesarea cheilor din dictionar
print(f"Fotbalistii din lista sunt {fotbalisti.keys()}")

# Accesarea valorilor din dictionar
print(f"Numerele de pe tricoul fotbalistilor din lista sunt {fotbalisti.values()}")

# Actualizarea elementelor din dictionar
fotbalisti.update({"Henry": "10"})
print(f"Noul numar de pe tricoul lui Henry este {fotbalisti.get('Henry')}")
fotbalisti["Cristian Chivu"] = 6
print(f"Noul numar de pe tricoul lui Chivu este {fotbalisti.get('Cristian Chivu')}")

# Dictionare imbricate (dictionar in dictionar)
fotbalisti_pe_echipe = {
    "Barcelona": {
        "Dica": {
            "Nume complet": "Nicolae Dica",
            "Varsta": 45,
            "Numar Tricou": 10
        },
        "Banel": {
            "Nume complet": "Banel Nicolita",
            "Varsta": 47,
            "Numar Tricou": 3
        },
        "Dukadam": {
            "Nume complet": "Helmut Dukadam",
            "Varsta": 65,
            "Numar Tricou": 7
        }
    }}

print(f"Numarul de tricou al lui Dica este: {fotbalisti_pe_echipe['Barcelona']['Dica']['Numar Tricou']}")

# Functia pop poate fi folosita pentru a elimina un element dintr-un dictionar
fotbalisti.pop("Kilian Mbape")
print(f"Fotbalistii dupa eliminarea lui Mbape: {fotbalisti}")
print(f"\n {fotbalisti_pe_echipe}")

# print("\n" + fotbalisti_pe_echipe)
print(fotbalisti_pe_echipe)
fotbalisti_pe_echipe.popitem()
print(fotbalisti_pe_echipe)