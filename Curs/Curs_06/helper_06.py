from math import sqrt

from Curs_06.curs_06_01 import Gestiune_Liste

lista = [1, 5, 3, 9, 1, 0, -3, 5, -10, 15, 172345832]
obiect_lista_1 = Gestiune_Liste(lista)
# Pentru a accesa orice element din interiorul unei clase (atribut sau metoda)
# avem nevoie de un obiect instantiat din clasa respectiva
print(obiect_lista_1.lista_elemente)
print(Gestiune_Liste.lista_elemente)
print(sqrt(9))