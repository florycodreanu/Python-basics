"""
Exista patru piloni majori ai programarii care ne ajuta la o buna gestiune a codului si la economisire de linii de cod
1. Mostenire
- Posibilitatea unei clase de a mosteni atribute si metode definite intr-o clasa parinte
- Avantajul mostenirii este acela ca nu mai trebuie sa scriem acelasi cod de mai multe ori
- Este un concept similar cu cel al functiilor, dar implementat diferit
    - la functii - scriem functia o data si o apelam de mai multe ori
    - la mostenire scriem o clasa parinte si o trimitem ca si stramos oricator clase avem nevoie
- Mostenirea se implementeaza prin specificarea numelui clasei parinte intre paranteze langa numele clasei mostenitoare
2. Polimorfism
- Posibilitatea crearii a doua functii cu nume identic dar cu comportament diferit
- Se poate implementa atat prin crearea unor functii cu numar nedeterminat de parametri sau cu parametri initializati
cu valori implicite sau se poate implementa si prin crearea a doua functii cu acelasi nume si acelasi numar de parametri
dar in clase diferite
3. Encapsulare
- Posibilitatea ascunderii anumitor atribute si metode si restrictionarea utilizarii lor
4. Abstractizare
- Posibilitatea templetizarii anumitor metode dintr-o clasa
- Orice clasa care mosteneste o clasa abstracta va fi obligata sa implementeze un comportament definit in clasa abstract
- Exista doua forme de abstractizare:
    - cand toate metodele din clasa sunt abstracte (interfata)
    - cand doar unele metode din clasa sunt abstracte (clasa abstracta)
Metodele sunt marcate ca si abstracte prin intermediul unui decorator
Decorator este un set de instructiuni grupate sub un nume care pot sa schimbe comportamentul unei functii
@abstractmethod = este un decorator care marcheaza o functie ca fiind abstracta
@staticmethod = este un decorator care marcheaza o functie ca fiind statica
    (adica poate fi accesata prin intermediul clasei)
"""