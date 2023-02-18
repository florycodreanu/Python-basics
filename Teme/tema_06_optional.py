from tabulate import tabulate
from datetime import date

"""
1.Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
"""


class Factura:
    seria = "CRT"
    numar_fct = None
    nume_produs = None
    cantitate = None
    pret_buc = None

    def __init__(self, numar_fct, nume_produs, cantitate, pret_buc):
        self.numar_fct = numar_fct
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def genereaza_factura(self):
        print(f'Factura seria: {self.seria} numar: {self.numar_fct}')
        print(f'Data: {date.today()}')
        col_names = ["Produs", "Cantitate", "Pret bucata", "Total"]
        tabel = [[self.nume_produs, self.cantitate, self.pret_buc, self.cantitate * self.pret_buc]]
        print(tabulate(tabel, headers=col_names, tablefmt="fancy_grid"))


produs1 = Factura(12530, "Piniata", 4, 100)
produs2 = Factura(12536, "Face painting", 20, 10)
produs1.genereaza_factura()
print("-----------------------------------------------------------------")
produs2.genereaza_factura()
print("-----------------------------------------------------------------")
produs2.schimba_cantitatea(18)
produs2.schimba_pretul(150)
produs2.schimba_nume_produs("Aranjament_masa_baloane")
produs2.genereaza_factura()

"""
2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0
"""


class Masina:
    marca = 'Audi'
    model = None
    viteza_maxima = None
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibie = {'negru', 'albastru', 'alb', 'portocaliu', 'rosu', 'galben'}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descriere(self):
        print(f'Am fabricat masina marca: {self.marca}, modelul: {self.model}.'
              f'\nPoate atinge maxim: {self.viteza_maxima} km/h, viteza actuala fiind: {self.viteza_actuala} km/h'
              f'\nCuloarea actuala este :{self.culoare}. Masina este inmatriculata? {self.inmatriculata}')

    def inmatriculare(self):
        self.inmatriculata = True
        return self.inmatriculata

    def vopseste_masina(self, culoare_noua):
        if culoare_noua.casefold() in self.culori_disponibie:
            self.culoare = culoare_noua
            print(f'Culoarea masinii este acum: {self.culoare}')
        else:
            print('Culoarea aleasa nu exista in optiuni!')

    def accelereaza(self, viteza):
        if viteza < 0:
            print('Eror, Eror!')
        elif viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = viteza
            print(f'Viteza actuala este: {self.viteza_actuala} km/h')

    def franeaza(self):
        self.viteza_actuala = 0
        return self.viteza_actuala


# masina_1 = Masina('A8', 250)
# masina_2 = Masina('Q7', 210)
# print('-----------Produs 1----------')
# masina_1.descriere()
# print('-----------Produs 1----------')
# masina_2.descriere()
# print('-----------')
# # culoare_1 = input('Va rugam introduceti culoarea dorita pentru A8: ')
# # masina_1.vopseste_masina(culoare_1)
# # culoare_2 = input('va rugam introduceti culoarea dorita pentru Q7: ')
# # masina_2.vopseste_masina(culoare_2)
# print('-----------')
# masina_1.accelereaza(200)
# masina_2.accelereaza(-200)
# print('-----------')
# print(f'Testul s-a terminat. {masina_1.marca} {masina_1.model} franeaza pana ajunge la {masina_1.franeaza()} km/h')
# print(f'Testul s-a terminat. {masina_2.marca} {masina_2.model} franeaza pana ajunge la {masina_2.franeaza()} km/h')
# print('-----------')
# print(f'Se inmatriculeaza masinile la vanzare? \n{masina_1.marca} {masina_1.model} : {masina_1.inmatriculare()}'
#       f'\n{masina_2.marca} {masina_2.model} : {masina_2.inmatriculare()}')

"""
3. Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:
● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict
"""


class TodoList:
    todo = {}

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere
        print('Taskul a fost adaugat in lista!')

    def finalizeaza_task(self, nume):
        name = nume.casefold()
        self.todo.pop(name)

    def afiseaza_todo_list(self):
        print('Task-urile de finalizat sunt:')
        for key in self.todo.keys():
            print(f' - {key}')

    def afiseaza_detalii_suplimentare(self, name_task):
        if name_task in self.todo.keys():
            print(f'Detalii task-ului {nume_task} sunt: {self.todo[nume_task]}')
        else:
            raspuns = input('Taskul nu se afla pe lista. Doriti sa il adaugam? ')
            if raspuns.capitalize() == 'Da':
                descriere_task = input('Introduceti descrierea task-ului: ')
                self.todo[name_task] = descriere_task
                print('Task-ul a fost adaugat.')
            elif raspuns.capitalize() == 'Nu':
                print('Am inteles. O zi buna! La revedere!')


print('---------------------------------------')
list_1 = TodoList()
list_1.adauga_task('curatenie', 'Sters praful plus aspirat')
list_1.adauga_task('piata', 'Lapte, oua, paine, rosii, castraveti')
list_1.adauga_task('teme', 'Mai adi de rezolvat 10 exercitii de logica')
list_1.adauga_task('invatat', 'Trebuie sa mai citesti lectiile pentru scoala')
list_1.afiseaza_todo_list()
list_1.finalizeaza_task('Teme')
list_1.finalizeaza_task('invatat')
list_1.afiseaza_todo_list()
nume_task = input('Introduceti numele task-ului cautat: ')
list_1.afiseaza_detalii_suplimentare(nume_task.casefold())