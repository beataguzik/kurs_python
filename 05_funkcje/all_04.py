"""4▹ Napisz funkcję, która sprawdzi, czy liczba występuje w podanym
przez użytkownika zakresie. Powinna zwrócić komunikat:
“tak, liczba x znajduje się w zadanym zakresie”,
“nie, liczba x jest z poza zakresu”."""



def check_list(number, first_number, last_number):
    if number >= first_number and number <= last_number:
        return f"podana liczba {number} znajduje się w zakresie"
    else:
        return f"podana liczba {number} jest poza zakresem"


first_number = 1
last_number = 10
number = int(input("Podaj liczbę do sprawdzenia, czy jest w wyznaczonym zakresie: "))

result = check_list(number, first_number, last_number)
print(result)