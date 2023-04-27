# #1
#
# """Poproś użytkownika o podanie liczby.
#  Sprawdź czy liczba podana przez użytkownika jest
#  podzielna przez 3 bez reszty i wyświetl komunikat
#  “Twoja liczba jest podzielna przez 3”.
# """
#
# number=float(input("podaj liczbę:"))
# if number % 3 == 0:
#     print("podzielna przez 3")
# else:
#     print("nie podzielna przez 3"
#           )
# #2
#
# """Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
#  Jeśli suma jest większa niż 100, wyświetl wynik,
#  w przeciwnym wypadku wyświetl “Koniec”."""
#
#
# number1=float(input("podaj pierwsza liczbę :"))
# number2=float(input("podaj drugą liczbę :"))
# if number1+number2 >100:
#     print(number1+number2)
# else:
#     print("Koniec")
#
#
#
#
# #3
#
# """Stwórz skrypt, który przyjmuje 3 opinie
# użytkownika o książce. Oblicz średnią opinię o
#  książce. W zależności od wyniku dodaj komunikaty.
#  Jeśli uzytkownik ocenił książkę na ponad
#   7 - bardzo dobry, ocena 5-7 przeciętna,
# 4 i mniej - nie warta uwagi."""
#
#
# txt1 = int(input("podaj ocenę 1 w skali 1-10:"))
# txt2 = int(input("podaj ocenę 2 w skali 1-10:"))
# txt3 = int(input("podaj ocenę 3 w skali 1-10:"))
# srednia=(txt1+ txt2 + txt3)/3
#
# if srednia>=7 :
#     print("very good")
# elif srednia >=4 :
#     print("not interesting")
# else:
#     print("bad")
#
#
# #4
#
# """Utwórz zmienną przechowującą dowolny ciąg znaków.
#  Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz
#  czy zawiera literę a. Jeśli zawiera, wszystkie litery a podmień
# na z i wyświetl powstały napis. """
#
# number3="123456abc"
# if len(number3) < 5:
#     print('mniej niż 5 znaków')
# elif len(number3) >5:
#     print("więcej niż 5 znaków")
# print(number3.replace("a", "z"))
# # if not number3("a"):
# #     print("zawiera a")
# # else:
# #     print("nie zawiera a")
#
#
#
#
#
# #5
#
# '''Stwórz zmienną password. Hasło powinno
# składać z liter i cyfr, zwierać conajmniej
# 1 małą literę, 1 dużą literę i mieć długość
#  conajmniej 8 znaków. Poinformuj użytkownika,
#  jeśli wpisane hasło jest nie poprawne.
#  Wyświetl różne komunikaty
#  w zależności od rodzaju błędu.'''
#
#
# password = "haslooooooO1"
#
# # jesli za krótkie
# if len(password) < 8:
#     print('Password too short')
# # jesli nie ma cyfry
# if password.isalnum() and password.isalpha():
#     print('Password needs at least one digit')
# # jesli nie ma litery
# if password.isalnum() and password.isdigit():
#     print('Password needs at least one letter')
# # jesli nie ma małej litery
# if password.islower():
#     print('Password needs at least 1 upper letter')
#
# # jeśli nie ma dużej litery
# if password.isupper():
#     print('Password needs at least 1 lower letter')
#
# print(f'super [not] secure password here -> {password}')
#
#
#
# #6 Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą
# # przez programistę wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.
#
#
# txt= float(input("odgadnij mój numer od 1 do 100: "))
# txt2=5
# if txt == txt2 :
#     print("Brawo zgadłeś!")
# else:
#     print("Spróbuj jeszcze raz!")
#
#
# #7  Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
# # która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.
#
#
# print("podaj wagę w kg:")
# w=float(input())
# print("podaj wzrost w m:")
# h=float(input())
# BMI=w/(h ** 2)
# print("twoje BMI wynosi:",BMI)
# if BMI > 18.5 < 24.99:
#     print("waga normalna")
# elif BMI > 25.0 < 29.9:
#     print("nadwaga")
# elif BMI > 30.0 < 34.99:
#     print("nadwaga")
# elif BMI > 35.0:
#     print("otyłość")
# elif BMI < 18.49:
#     print("niedowaga")



#8  Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.


n1= int(input("podaj pierwszą liczbę: "))
n2= int(input("podaj drugą liczbę: "))
n3= int(input("podaj trzecią liczbę: "))
list = [n1, n2, n3]
list2=sorted(list)
print("posortowane liczby: ", list2)

print("największa wybrana liczba to: ", (list2[-1]))