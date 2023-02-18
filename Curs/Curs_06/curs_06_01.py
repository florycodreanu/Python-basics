class Gestiune_Liste:
    lungime = None
    sortata = None
    tip_de_date = None
    lista_elemente = None

    def __init__(self, lista_elemente):
        # am definit un atribut direct in constructor
        self.lista_elemente = lista_elemente

    # [3, 5, 9, 7, 1]   [1, 5, 9, 7, 3]
    # sortare elemente prin metoda bulelor
    def bubble_sort(self):
        for i in range(len(self.lista_elemente)):
            schimbare = False
            for j in range(i+1, len(self.lista_elemente)):
                if self.lista_elemente[i] > self.lista_elemente[j]:
                    swap = self.lista_elemente[i]
                    self.lista_elemente[i] = self.lista_elemente[j]
                    # self.lista_elemente[i], self.lista_elemente[j]  = self.lista_elemente[j], self.lista_elemente[i]
                    self.lista_elemente[j] = swap
                    schimbare = True
            if schimbare == False:
                break
        self.sortata = True

    # actualizare lungime
    def calculeaza_lungimea(self):
        self.lungime = len(self.lista_elemente)

    # identificare tip de date
    def tip_date(self):
        for i in self.lista_elemente:
            print(f"Tipul de date al elemnului {i} este {type(i)}")

    # gasire element
    def gasire_element(self, elementul_cautat):
        for i in range(len(self.lista_elemente)):
            if self.lista_elemente[i] == elementul_cautat:
                return f'Am gasit elementul {elementul_cautat} in lista'
        return 'Nu am gasit elementul cautat'

    # inlocuire
    def inlocuire_element(self, element_de_inlocuit, element_care_inlocuieste):
        for i in range(len(self.lista_elemente)):
            if self.lista_elemente[i] == element_de_inlocuit:
                self.lista_elemente[i] = element_care_inlocuieste
                print(f'Elementul {element_de_inlocuit} a fost inlocuit cu {element_care_inlocuieste}')
            else:
                continue


if __name__ == "__main__":
    lista = [8, 6, 4, 0, 2]
    # Am instantiat un obiect al clasei Gestiune_Liste
    lista_numere_pare = Gestiune_Liste(lista)
    print(lista_numere_pare)
    # printeaza ob, adica adresa de memorie a elementului meu: <__main__.Gestiune_Liste object at 0x103e66800>
    print(f"Lista nesortata este: {lista_numere_pare.lista_elemente}")
    lista_numere_pare.bubble_sort()
    print(f"Lista sortata este: {lista_numere_pare.lista_elemente}")
    print(f"Este lista sortata? {lista_numere_pare.sortata}")
    lista_numere_pare.tip_date()
    print(lista_numere_pare.gasire_element(8))
    lista_numere_pare.inlocuire_element(8, 5)
    lista_numere_pare.inlocuire_element(5, 8)