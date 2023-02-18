# Exercitiul 1
# Variavila = adresa de memorie in care se stocheaza diferite tipuri de informatii

# Exercitiul 2

s = 'Flori'
i = 26
f = 52.5
b = True

# Exercitiul 3

print(f'Variabila s este tip: {type(s)}')
print(f'Variabila i este tip: {type(i)}')
print(f'Variabila f este tip: {type(f)}')
print(f'Variabila b este tip: {type(b)}')

# Exercitiul 4

f = round(f)
print(f'variabila f reinitializata este acum tip: {type(f)} si are valoarea {f}')

# Exercitiul 5

print('Variabila "s" este ' + str(type(s)) + ' si are valoarea ' + s)
print(f'Variabila "i" este este {type(i)} si are valoarea {i}')
print(f'Variabila "f" are acum valoarea {f} si este {type(f)}')
print(f'Variabila "b" este de tip {type(b)} si returneaza valoarea {b}')

# Exercitiul 6

nume = input("Introduceti numele dumneavoastra: ")
prenume = input("Introduceti prenumele: ")
print('Numele complet are ' + str(len(nume+prenume)) + ' caractere')

# Exercitiul 7

lungime = float(input("Lungime = "))
latime = float(input("Latime = "))
print('Aria dreptunghiului este ' + str(2*lungime+2*latime))

# Exercitiul 8

prop = 'Coral is either the stupidest animal or the smartest rock'
print(f'Cuvantul cautat apare de:  {prop.count("the")} ori')

# Exercitiul 9
# Inlocuirea cuvantului "the" cu THE si afisarea noii propozitii.

print(prop.replace('the', 'THE'))

# Exercitiul 10
assert prop.isnumeric() == True, "Eroare sirul nu contine doar numere"
print("Sirul contine doar numere")