"""Zadania:


    2 Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.

    3 Do zmiennej quote przypisz zdanie:

    „Honesty is the first chapter in the book of wisdom.”, a następnie:

   - Policz wszystkie znaki w napisie

   - Nie modyfikując zmiennej wyświetl słowo wisdom

   - Wyświetl tylko pierwszą połowę tekstu

   - Wyświetl tylko kropkę

   - Wyświetl od połowy tylko co trzecią literę cytatu

   - Wyświetl ‘Hnsyi h is hpe ntebo fwso.’

   - Wyświetl cały cytat odwrotnie

    -Zamień wisdom na słowo friendship

    4 Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:

    -Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.

   - Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich

   - Połącz dane w jeden ciąg book za pomocą spacji

   - Policz liczbę wszystkich znaków w napisie book

   5 Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok. Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.

   6 Przekopiuj zawartość import this do zmiennej.

import this

   - Policz liczbę wystąpień słowa better.

   - Usuń z tekstu symbol gwiazdki

   - Zamień jedno wystąpienie explain na understand

   - Usuń spacje i połącz wszystkie słowa myślnikiem

  -  Podziel tekst na osobne zdania za pomocą kropki

Więcej: formatowanie ciągów znaków - string formatting

i po polsku formatowanie napisów

   7 Stwórz dwie dowolne zmienne przechowujące wartość liczbową i tekstową. Użyj funkcji format(), by wyświetlić zdanie zawierające te wartości.
"""


#2

s1="lato"
s2= " zima"
print(s1 +s2)
s3="wiosna"
print(s1[0:2]+s2+s1[2:4]+s3)

#3

quote="(„Honesty is the first chapter in the book of wisdom.”)"
print(len(quote))
print(quote[44:52])
print(quote[:26])
print(quote[52])
print(quote[26:]+quote[::3])
print(quote[::2])

quote2=quote[::-1]
print(quote2)

print(quote.replace("wisdom", "friendship"))

#4

print("podaj tytuł książki:")
title=str(input())
print("podaj nazwisko autora:")
author=str(input())
print("podaj liczbę stron:")
number_of_pages=(input())

print(title.isalnum())
print(author.isalnum())
print(number_of_pages.isdigit())

title = title.capitalize()
author = author.capitalize()
print(title, author)

title = title.replace(" ", "").replace(",","").replace("-","").replace(".","")
print(title)

print(len(title))


#5?
print("wpisz dowolne zdanie:")
message=(input())
print(message==message[::-1])


