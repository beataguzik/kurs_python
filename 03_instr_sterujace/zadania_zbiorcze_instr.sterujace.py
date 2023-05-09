"""Zadania podsumowujące całość:

1▹ Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście.

2▹ Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych. Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

3▹ W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.

Ważne

Przed zadaniami 4 i 5 zapoznaj się z dokumentacają modułu random. Na początku pliku musisz dodać:

import random

Szczególnie zwróć uwagę na funkcje random.randint(), random.randrange() i random.choice().

4▹ Napisz grę - kamień (k) / papier (p) / nożyce (n).

        Użytkownik podaje jedną z 3 figur.

        Komputer losuje jedną z 3 figur.

        Sprawdź kto wygrał tę rundę.

        Zmień kod tak, by użytkownik mógł podac liczbę rund.

        Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.

        Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

5▹ Stwórz grę ciepło zimno.

        Komputer losuje liczbę z zakresu od 1 do 100.

        Użytkownik podaje swój traf.

        Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.

        Jeśli użytkownik zgadnie wygrywa gracz.

        Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.
"""



#1

name = input('podaj imiona: ')
name_list = name.replace(" ", "").split(',')
for step in name_list:
    print('Hello ', step)


#2

tekst = input('wpisz dowolny tekst: ')
print(tekst[1::2])

############
tekst = input('wpisz dowolny tekst: ')
for x in tekst:
    print(tekst[1::2])
    break


#3

txt = input('Give me any text with any characters ->')

lower_letters = 0
upper_letters = 0
digits = 0
other_chars = 0

for char in txt:
    if char.isupper():
        upper_letters += 1
    elif char.islower():
        lower_letters += 1
    elif char.isdigit():
        digits += 1
    else:
        other_chars += 1

print("lower letters:", lower_letters)
print("upper letters:", upper_letters)
print("digits:", digits)
print("other:", other_chars)


#4


import random

counter = int(input("ile chcesz rund?"))

print(counter)

player = input("wybierz: 'p'apier, 'k'amień, 'n'ożyce?")
list = ['p', 'k', 'n']
comp = random.choice(list)

print(comp)

if player == "p" and comp == "p":
    print(f"ja dałem :{comp}")
    print("remis")

elif player == "k" and comp == "k":
    print(f"ja dałem :{comp}")
    print("remis")

elif player == "n" and comp == "n":
    print(f"ja dałem :{comp}")
    print("remis")


elif player == "p" and comp == "k":
    print(f"ja dałem :{comp}")
    print("wygrałeś")


elif player == "p" and comp == "n":
    print(f"ja dałem :{comp}")
    print("przegrałeś")


elif player == "k" and comp == "p":
    print(f"ja dałem :{comp}")
    print("przegrałeś")

elif player == "k" and comp == "n":
    print(f"ja dałem :{comp}")
    print("wygrałeś")


elif player == "n" and comp == "p":
    print(f"ja dałem :{comp}")
    print("wygrałeś")

elif player == "n" and comp == "k":
    print(f"ja dałem :{comp}")
    print("przegrałeś")


print(input('gramy dalej? tak/nie :'))
answear = ["tak", "nie"]

if answear == "tak":
    print("gramy dalej")


if answear == "nie":
    print("dzieki za gre!")




#6

import random

player = int(input("Odgadnij moją liczbę od 1 do 100: "))
komp = random.randint(1, 100)
while True:
    if player > komp:
        print("zimno")
        continue
    if player < komp:
        print("ciepło")
        continue
    elif player == komp:
        print("zgadłes")
        break

print("liczba komputera to:", komp)





