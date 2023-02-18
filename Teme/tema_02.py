# Exercitiul 1
"""
- Un if...else este o structura decizionala prin care codul poate trece daca indeplineste conditiile de pe ramura
respectiva;
- Un if else are doua ramuri daca se indeplineste conditia de pe prima ramura (if) codul merge pe aceea ramura,
iar daca nu va merge pe cea de-a doua ramura (else)
"""

# Exercitiul 2
x = int(input('Introduceti un numar intreg: '))
if x >= 0:
    print(f'Numarul {x} este natural.')
else:
    print(f'Numarul {x} nu este natural.')

# Exercitiul 3
x = int(input('Introduceti un numar intreg: '))
if x > 0:
    print(f'Numarul {x} este pozitiv.')
elif x == 0:
    print(f'Numarul este neutru.')
else:
    print(f'Numarul {x} este negativ')

# Exercitiul 4
if x >= -2 and x <= 13:
    print(f'Numarul {x} este cuprins in intervalul -2 si 13.')
else:
    print(f'Numarul {x} nu este cuprins in intervalul -2 si 13.')

# Exercitiul 5
x = int(input('Introduceti un numar intreg: '))
y = int(input('Introduceti un numar intreg: '))
if x > y:
    d = x - y
else:
    d = y - x
if d < 5:
    print(f'Diferenta numerelor este {d} si este < 5 ')
else:
    print(f'Diferenta numerelor este {d} si nu este mai mica decat 5 ')

# Exercitiul 6
x = int(input('Introduceti un numar intreg: '))
if not 5 < x < 27:
    print('Numarul nu este cuprins in intervalul 5 si 27 ')
else:
    print('Numarul este in intervalul 5 si 27.')

# Exercitiul 7
x = int(input('Introduceti un numar intreg: '))
y = int(input('Introduceti un numar intreg: '))
if x == y:
    print(f'Numarul x={x} este egal cu numarul y={y}.')
elif x > y:
    print(f'Numarul x={x} este mai mare ca numarul y={y}.')
else:
    print(f'Numarul x={x} este mai mic ca numarul y={y}.')

# Exercitiul 8
x = int(input('Introduceti latura 1 a triunghiului: '))
y = int(input('Introduceti latura 2 a triunghiului: '))
z = int(input('Introduceti latura 3 a triunghiului: '))
if x == y == z:
    print('Triunghiul este echilateral deoarece laturile sunt egale.')
elif x == y or y == z or x == z:
    print('Triunghiul este isoscel deoarece are doua laturi egale.')
else:
    print('Triunghiul este oarecare, deoarece laturile sunt diferite.')

# Exercitiul 9
lit = input('Introduceti o litera de la tastatura: ')[:1]
if lit == 'a' or lit == 'e' or lit == 'i' or lit == 'o' or lit == 'u' or lit == 'ă' or lit == 'î' or lit == 'â':
    print(f'Litera {lit} reprezinta o vocala. ')
else:
    print(f'Litera {lit} reprezinta o consoana')

# Exercitiul 10
nota = float(input('Introduceti nota de  la 0 la 10: '))
if 0 <= nota <= 4:
    print(f'Nota in sistem romanesc este: {nota} si corespunde notei: "F" ')
elif 4 < nota <= 6:
    print(f'Nota in sistem romanesc este: {nota} si corespunde notei: "E" ')
elif 6 < nota <= 7:
    print(f'Nota in sistem romanesc este: {nota} si corespunde notei: "D" ')
elif 7 < nota <= 8:
    print(f'Nota in sistem romanesc este: {nota} si corespunde notei: "C" ')
elif 8 < nota <= 9:
    print(f'Nota in sistem romanesc este: {nota} si corespunde notei: "B" ')
elif 9 < nota <= 10:
    print(f'Nota in sistem romanesc este: {nota} si corespunde notei: "A" ')
else:
    print('Nota introdusa nu este corecta!')