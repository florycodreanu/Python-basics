# Exercitiul 1
"""1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while."""

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
print('FOR')
for i in range(len(masini)):
    print(f'Masina mea preferata este: {masini[i]}')
print('\nFor each')
for masina in masini:
    print(f'Masina mea preferata este: {masina}')
print('\nWhile')
m = 0
while m < len(masini):
    print(f'Masina mea preferata este: {masini[m]}')
    m += 1

# Exercitiul 2
"""Folosește un for else. In for
- Modifică elementele din listă astfel încât să fie scrie cu majuscule,exceptând primul și ultimul.
În else:
- Printează lista."""

for j in range(1, len(masini)-1):
    masini[j] = masini[j].upper()
print(f'\nLista de masini este:\n{masini} \n')

# Exercitiul 3
"""Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam."""
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
k = 0
while k < len(masini):
    if masini[k] == 'Mercedes':
        print("Am gasit masina dorita de dumneavoastra!")
        break
    print(f'Am gasit masina {masini[k]}. Mai cautam!')
    k += 1
print('Ne bucuram ca v-am putut ajuta!\n')

# Exercitiul 4
"""Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:mFolosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
- Printează S-ar putea să vă placă mașina x."""
for auto in masini:
    if auto == 'Trabant' or auto == 'Lăstun':
        continue
    print(f'S-ar putea sa va placa masina {auto}.')

# Exercitiul 5
"""Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
● Printează Modele vechi: x.
● Modele noi: x."""
masini_vechi = []
for mv in range(len(masini)):
    if masini[mv] == 'Lăstun' or masini[mv] == 'Trabant':
        masini_vechi.append(masini[mv])
        masini[mv] = 'Tesla'
print(f'\nModele vechi: {masini_vechi}')
print(f'Modele noi: {masini}\n')

# Exercitiul 6
"""
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă."""
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
buget = 15000
for key, pret in pret_masini.items():
    if pret <= buget:
        print(f'Pentru un buget de pana in {buget} euro puteti alege masina: {key}')

# Exercitiul 7
"""numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count)."""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
nr_aparitii = 0
for i in range(len(numere)):
    if numere[i] == 3:
        nr_aparitii += 1
print(f'\nNumarul 3 apare de {nr_aparitii} ori.')

# exercitiul 8
"""Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum)."""
suma = 0
for numar in numere:
    suma += numar
print('\n',suma)

# Exercitiul 9
"""Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max)."""
maxi = numere[0]
for j in range(1, len(numere)):
    if numere[j] > maxi:
        maxi = numere[j]
print(f'\nCel mai mare numar este : {maxi}')

# Exercitiul 10
"""Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă."""
lista_neg = []
for numar in numere:
    if numar > 0:
        lista_neg.append(-numar)
    else:
        lista_neg.append(numar)
print(f'\n{numere} , \n{lista_neg}')