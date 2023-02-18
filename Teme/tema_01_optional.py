# Exercitii optionale
"""
2. citește de la tastatură un string de dimensiune impară;
afișează caracterul din mijloc.
"""
text = str(input('Introduceti un string cu nr impar de caractere: '))
print(f'Caracterul din mijloc este: {text[len(text)//2]}')

"""
2. Folosind assert, verifică dacă un string este palindrom.
"""
mystr = str(input('Introduceti un cuvant: '))
inv_mystr = mystr[::-1]
assert mystr.lower() == inv_mystr.lower(), 'Cuvantul nu este palindron!'
print('Cuvantul este palindrom!')

"""
3. Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.
"""
mystr2 = str(input('Introduceti un string de doua cuvinte: '))
x, y = mystr2.split()
print(f'primul cuvat este {x}. \nAl doilea cuvant este {y}.')

"""
4.citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
"""
mystr3 = str(input('Introduceti un string: '))
x = mystr3[0]
mystr3_mod = x.lower() + mystr3[1:len(mystr3)-1].replace(x, x.upper()) + mystr3[len(mystr3)-1].lower()
print(mystr3_mod)

"""
5.citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect."""
user = str(input('Introduceti user-ul: '))
parola = str(input('Itroduceti parola: '))
print(f'Parola pentru user-ul: {user} este {"*" * len(parola)} si are {len(parola)} caractere.')