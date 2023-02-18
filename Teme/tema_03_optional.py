"""
1. Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.
- Declara o lista cu 5 jucatori: lista_jucatori_teren
- Declara o lista cu 5 jucatori de rezerva: lista_jucatori_rezerva
- Declara o lista goala cu jucatori scosi din teren: lista_jucatori_scosi
- Schimbari_efectuate = joaca-te cu valori diferite ca sa vezi cum trec datele prin cod
- SCHIMBARI_MAX va fi o constanta cu valoarea 3
"""
import random

lista_jucatori_teren = ['j1', 'j2', 'j3', 'j4', 'j5']
lista_jucatori_rezerve = ['j6', 'j7', 'j8', 'j9', 'j10']
lista_jucatori_scosi = []
schimbari_max = 3
schimbari_efectuate = 1
schimbari_ramase = schimbari_max - schimbari_efectuate
jucator_in = random.choice(lista_jucatori_rezerve)
jucator_out = random.choice(lista_jucatori_teren)
if jucator_out in lista_jucatori_teren and schimbari_ramase > 0:
    if jucator_in in lista_jucatori_rezerve and jucator_in not in lista_jucatori_teren:
        lista_jucatori_teren.remove(jucator_out)
        lista_jucatori_scosi.append(jucator_out)
        lista_jucatori_teren.append(jucator_in)
        lista_jucatori_rezerve.remove(jucator_in)
        schimbari_ramase -= 1
        print(f'Schimbarea a fost efectuata! A intrat jucatorul {jucator_in} si a iesit jucatorul {jucator_out}. '
              f'Mai aveti {schimbari_ramase} schimbari ramase.')
elif jucator_out not in lista_jucatori_teren:
    print(f'Nu se poate efectua schimbarea deoarece {jucator_out} nu se afla in teren.')
elif schimbari_ramase == 0:
    print('Nu mai aveti schimari ramase!')
print(f'Actuala echipa este :{lista_jucatori_teren}'
      f'\nLista actuala de rezerve este: {lista_jucatori_rezerve}' 
      f'\nLista actuala de jucatori care au iesit din teren este: {lista_jucatori_scosi}')