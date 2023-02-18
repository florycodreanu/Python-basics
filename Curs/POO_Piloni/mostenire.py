class Animale:
    sunet = None
    culoare = None
    specie = None
    rasa = None
    varsta = None
    sunet_somn_mancare = None
    greutate = None
    culoare_ochi = None

    """
    Exista doua tipuri de constructori:
    - constructor explicit - cel pe care il definim noi in interiorul clasei 
    - constructor implicit - cel care este definit in python by default si care este apelat automat de catre sistem
    atunci cand nu exista un constructor explicit definit
    """

    def dormi(self):
        print(f"Acum dorm: {self.sunet_somn_mancare}")

    def mareste_varsta(self):
        self.varsta += 1
        print(f"Acum am {self.varsta} ani")


pisica = Animale()
pisica.sunet = "miau"
pisica.culoare = "portocaliu"
pisica.varsta = 2
pisica.sunet_somn_mancare = "prrrrrr"
pisica.dormi()
pisica.mareste_varsta()


class Pisica(Animale):
    vaneaza_soareci = None
    toarce = "Da"
    aterizeaza_in_picioare = "Da"
    detin_om = "Da"
    noua_vieti = "Da"

    def toarce_sa_ceri_mancare(self):
        if self.toarce == "Da":
            self.sunet_somn_mancare = "prrrrrr"
            print(self.sunet_somn_mancare)


pisica_mostenitoare = Pisica()
pisica_mostenitoare.toarce_sa_ceri_mancare()