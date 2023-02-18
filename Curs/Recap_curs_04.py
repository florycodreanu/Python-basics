"""
WHILE
Ce este? - Structura repetitiva care executa o serie de instructiuni atata timp cat o conditie este adevarata
Cand se foloseste? - De regula folosim while atunci cand avem de evaluat o conditie
care nu stim exact cat timp va fi adevarata
Componentele unei structuri repetitive de tip while:
- declararea variabilei de control a structurii repetitive (daca este nevoie)
- inceputul structurii repetitive (while)
- instructiuni care sa se execute atunci cand conditia este indeplinita
- modificarea variabilei de control in urma executarii instructiunilor
- cuvant cheie de control al structurii repetitive (break sau continue) daca este necesar
"""
"""
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
"""
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# In cazul exercitiul astuia oricare din structurile repetitive sunt ok
# Parcurgere cu while:
i = 0
while i < len(masini):
    print(f"Masina mea preferata este: {masini[i]}")
    i += 1

"""
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
"""

# optiunea 1: cu for
for i in range(len(masini)):
    if masini[i] == "Mercedes":
        print("Am gasit masina dorita de dumneavoastra")
        break
    print(f"Am gasit masina {masini[i]}. Mai cautam")

# optiunea 1: cu while
i = 0
gasit = False
while i < len(masini) and gasit == False:
    if masini[i] == "Mercedes":
        print("Am gasit masina dorita de dumneavoastra")
        gasit = True
        break
    else:
        print(f"Am gasit masina {masini[i]}. Mai cautam")
        i += 1

curatat_oceane = False
procent_incarcare_macara = int(input("Introduceti procentul de incarcatura a macaralei "))
while curatat_oceane == False:
    if procent_incarcare_macara < 5:
        print("Yeeey, am terminat treaba")
        curatat_oceane = True
    else:
        print("Mai avem de munca. Continua sa cureti")
        procent_incarcare_macara = int(input("Introduceti procentul de incarcatura a macaralei"))

"""
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
"""

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for i in range(len(alte_numere)):
    if alte_numere[i] % 2 == 0 and alte_numere[i] > 0:
        numere_pare.append(alte_numere[i])
        numere_pozitive.append(alte_numere[i])
    elif alte_numere[i] % 2 == 0 and alte_numere[i] < 0:
        numere_pare.append(alte_numere[i])
        numere_negative.append(alte_numere[i])
    elif alte_numere[i] % 2 != 0 and alte_numere[i] > 0:
        numere_impare.append(alte_numere[i])
        numere_pozitive.append(alte_numere[i])
    else:
        numere_impare.append(alte_numere[i])
        numere_negative.append(alte_numere[i])

print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)