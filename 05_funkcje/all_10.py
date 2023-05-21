"""10▹ Stwórz grę wisielec “bez wisielca”.

    Komputer losuje wyraz z dostępnej w programie listy wyrazów.

    Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)

    Użykownik podaje literę.

    Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat:

            “Trafione!” oraz napis ze znanymi literami.

    W przeciwnym wpadku pokaż komunikat:

            “Nie trafione, spróbuj jeszcze raz!”.

    Możesz ograniczyć liczbę prób do np. 10.
"""

import random
from os import system, name

lista_slow_do_zgadywania = ['tablica', 'kredka', 'landrynka', 'kot']


def wybierz_slowo(lista_slow):
    wylos_slowo = random.choice(lista_slow)

    return wylos_slowo

def tablica_do_str(tablica):
    str1 = ''

    for i in tablica:
        str1 += i + ' '
    return str1

def sprawdz_input(input_g):
    if (input_g == ""):
        print("nie podales litery")
    elif(len(input_g)>1):
        print('podales wiecej niz 1 litere')


def zgadnij_slowo(slowo):
    odpowiedz_gracza = []
    for i in slowo:
        odp_gracza.append('_')

    zycia = 10

    while(zycia > 0):
        print('masz jeszcze ' +str(zycia) +' żyć.')
        print('slowo do zgadniecia : ' + tablica_do_str(odpowiedz_gracza))
        print('podaj literkę: ')
        input_g = input().upper()

        sprawdz_input(input_g)

    print(slowo)
    print(odpowiedz_gracza)


#######################################################################################
lista = ['tablica', 'kredka', 'landrynka', 'kot']
haslo = str(lista[random.randint(0, len(lista)-1)])
tablica = list(haslo)

#tabl.sluzy do wyswietl ___
for i in range(len(haslo)):
    tablica[i] = '_'

#zmienna ile szans
zycia = 10

# petla while - zgadywanie liter
while zycia > 0:
    print('')
    print('zostalo jeszcze', zycia, 'żyć.')
    print('')
    print(' '.join(tablica))
    print('  ')

    #uzytk podaje litere
    print('podaj litere: ')
    litera = input()
    #jest
    if litera in haslo:
        for i in range(len(tablica)): #zmiana podkr na odgad litere
            if(haslo[i] == litera):
                tablica[i] = litera
#spr czy zgadniete cale
        if ''.join(map(str,tablica)) == haslo:
            print('')
            print('zostalo jeszcze', zycia, 'żyć.')
            print('')
            print(' '.join(tablica))
            print('  ')
            print('wygrales')
            break
    #nie ma
    else:
        zycia -= 1


