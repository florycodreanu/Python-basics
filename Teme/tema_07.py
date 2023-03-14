from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    pi = 3.14

    @abstractmethod
    def aria(self):
        pass

    @classmethod
    def descrie(cls):
        print('Cel mai probabil am colturi!')


class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        return self.__latura * self.__latura

    @property
    def latura(self):
        pass

    @latura.getter
    def latura(self):
        return self.__latura

    @latura.setter
    def latura(self, latura):
        self.__latura = latura

    @latura.deleter
    def latura(self):
        self.__latura = None


class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        pass

    @raza.getter
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, raza):
        self.__raza = raza

    @raza.deleter
    def raza(self):
        self.__raza = 0

    def aria(self):
        aria_cercului = self.pi * self.__raza * self.__raza
        return aria_cercului

    def descrie(self):
        print(f'Eu nu am colturi')


patrat = Patrat(5)
patrat.descrie()
print(f'Latura este : {patrat.latura}')
print(f'Aria patratului este {patrat.aria()}')
patrat.latura = 8
print(f'Noua latura dupa schimbare este: {patrat.latura}')
del patrat.latura
print(f'Am sters valoarea laturii care acum este: {patrat.latura}')

print('\n ============================== \n')

cerc = Cerc(5)
cerc.descrie()
print(f'Raza este : {cerc.raza}')
print(f'Aria cercului este {cerc.aria()}')
cerc.raza = 8
print(f'Noua raza dupa schimbare este: {cerc.raza}')
del cerc.raza
print(f'Am sters valoarea laturii care acum este: {cerc.raza}')


# lik github - https://github.com/florycodreanu/QAA
