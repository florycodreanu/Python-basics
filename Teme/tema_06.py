# 1.Clasa Cerc. Atribute: raza, culoare. Constructor pentru ambele atribute
# Metode: descrie_cerc() - va PRINTA culoarea și raza, aria() - va RETURNA aria, diametru(), circumferinta()
class Cerc:
    raza = None
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Avem un cerc de culoare: {self.culoare} si raza: {self.raza} ')

    def arie_cerc(self):
        aria = self.raza * self.raza * 3.14
        return aria

    def diametru(self):
        diametru = 2 * self.raza
        return diametru

    def circumferinta(self):
        circ = 2 * self.raza * 3.14
        return circ


print("------Ex: 1------")
cerc1 = Cerc(7, "albastru")
cerc2 = Cerc(12, "violet")
print("Cerc 1")
cerc1.descrie_cerc()
print(f'Aria cercului este: {cerc1.arie_cerc()}'
      f'\nDiametrul cercului este: {cerc1.diametru()}'
      f'\nCircumferinta cercului este: {cerc1.circumferinta()}')
print("Cerc 2")
cerc2.descrie_cerc()
print(f'Aria cercului este: {cerc2.arie_cerc()}'
      f'\nDiametrul cercului este: {cerc2.diametru()}'
      f'\nCircumferinta cercului este: {cerc2.circumferinta()}')

# 2. Clasa Dreptunghi. Atribute: lungime, latime, culoare. Constructor pentru toate atributele
# Metode: descrie(), aria(), perimetrul(), schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare.
# Puteti verifica schimbarea culorii prin apelarea metodei descrie().


class Dreptunghi:
    lingime = None
    latime = None
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie_dreptunghi(self):
        print(f'Avem un dreptungi cu lungimea {self.lungime} cm, latimea {self.latime} si culoare {self.culoare}.')

    def aria(self):
        a = self.lungime * self.latime
        return a

    def perimetru(self):
        p = 2 * (self.lungime + self.latime)
        return p

    def schimba_culoare(self, noua_culoare):
        self.culoare = noua_culoare


print("\n-----Ex. 2-----")
dreptunghi1 = Dreptunghi(12, 8, "verde")
dreptunghi2 = Dreptunghi(16, 12, "mov")
print('Dreptunghi1:')
dreptunghi1.descrie_dreptunghi()
print(f'Aria dreptunghiului este: {dreptunghi1.aria()}'
      f'\nPerimetrul dreptunghiului este: {dreptunghi1.perimetru()}')
dreptunghi1.schimba_culoare("negru")
dreptunghi1.descrie_dreptunghi()
print("\nDreptunghi 2")
dreptunghi2.descrie_dreptunghi()
print(f'Aria dreptunghiului este: {dreptunghi2.aria()}'
      f'\nPerimetrul este: {dreptunghi2.perimetru()}')
dreptunghi2.schimba_culoare("portocaliu")
dreptunghi2.descrie_dreptunghi()

# 3. Clasa Angajat. Atribute: nume, prenume, salariu. Constructor pt toate atributele
# Metode: descrie(), nume_complet(), salariu_lunar(), salariu_anual(), marire_salariu(procent)


class Angajat:
    nume = None
    prenume = None
    salariu = None

    def __init__(self, nume, prenume, salariu):
        self.prenume = prenume
        self.nume = nume
        self.salariu = salariu

    def descriere(self):
        print(f'Date angajat:\n Nume {self.nume}\n Prenume: {self.prenume}\n Salariu: {self.salariu}')

    def nume_complet(self):
        print(f'Numele complet al angajatului este : {self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariul lunar este: {self.salariu} RON')

    def salariu_anual(self):
        sal_anual = 12 * self.salariu
        return sal_anual

    def marire_sal(self, procent):
        salariu_marit = self.salariu + self.salariu*procent/100
        print(f'Dupa marirea cu {procent}% salariu angajatului este {salariu_marit}')


print("\n----Ex. 3----")
angajat1 = Angajat("Cojanu", "Florentina", 2500)
angajat2 = Angajat("Cojanu", "George", 4500)
print(f'Firma are urmatorii angajati:')
angajat1.descriere()
angajat1.nume_complet()
angajat1.salariu_lunar()
print(f'Salariul angajatului pe un an este: {angajat1.salariu_anual()}')
angajat1.marire_sal(10)
angajat2.descriere()
angajat2.nume_complet()
angajat2.salariu_lunar()
print(f'Salariul angajatului pe un an este: {angajat2.salariu_anual()}')
angajat2.marire_sal(10)


# 4. Clasa Cont. Atribute: iban, titular_cont, sold. Constructor pentru toate atributele
# Metode: afisare_sold() - Titularul x are în contul y suma de n lei, debitare_cont(suma), creditare_cont(suma)


class Cont:
    iban = None
    titular_cont = None
    sold = None

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold}')

    def debitare_cont(self, suma):
        print(f'Contul dumneavoastra a fost debitat cu suma {suma}.')
        self.sold -= suma
        print(f'Sold-ul curent este: {self.sold}')

    def creditare_cont(self, suma):
        print(f'Contul dumneavoastra a fost creditat cu suma: {suma}')
        self.sold += suma
        print(f'Soldul Curent este : {self.sold}')


print("\n----Ex.4----")
cont1 = Cont('R065BTRLRONCRT7686096', "Cojanu Florentina", 5000)
cont1.afisare_sold()
cont1.debitare_cont(1000)
cont1.creditare_cont(3000)