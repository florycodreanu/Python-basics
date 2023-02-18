from abc import abstractmethod, ABC


class Gradinita(ABC):
    # daca toate metodele din clasa sunt abstracte, atunci clasa va fi interfata
    # daca doar parte din metodele din clasa sunt abstracte, atunci clasa va fi clasa abstracta
    # daca noi marcam o metoda ca si abstracta si nu o implementam in clasa copil, vom primi o eroare:
    # TypeError: Can't instantiate abstract class Gradinita_privata with abstract method activitati
    @abstractmethod
    def joaca(self):
        raise NotImplementedError  # am instruit sistemul sa returneze eroare specifica daca metoda nu este implementata

    def somn(self):
        pass

    @abstractmethod
    def activitati(self):
        pass


class GradinitaPrivata(Gradinita):
    nr_copii = 0
    adresa = None
    orar = None

    def joaca(self):
        print("Copiii alearga")

    def activitati(self):
        print("Copiii se cultiva")


class GradinitaPublica(Gradinita):
    nr_copii = 0
    adresa = None
    orar = None

    def joaca(self):
        print("Copiii sar coarda")

    def activitati(self):
        print("Copiii canta")


obiect_gradi_privata = GradinitaPrivata()
obiect_gradi_publica = GradinitaPublica()
obiect_gradi_privata.joaca()
obiect_gradi_privata.activitati()
obiect_gradi_publica.joaca()
obiect_gradi_publica.activitati()

"""
Test plan = document creat la inceputul procesului de testare care contine informatii generale despre
        felul in care se va desfasura testarea
Unele tool-uri de test management au denumit functionalitatea de grupare a testelor in functie de 
obiective cu numele de Test Plan
"""