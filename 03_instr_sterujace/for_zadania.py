<<<<<<< HEAD
"""Zadania:

    Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry. Wyświetl nazwę właśnie spakowanego przedmiotu, po ostatnim przedmiocie pokaż informację: “Great, we are ready!”

    Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać. Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.

    Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników. Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

    Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8)."""




#1


items = ["headphones", "phone", "water"]

for i in items:
    print(i)
    print("Great, we are ready!")



#2
print("Przepis na jajecznicę: \n Składniki:")

items = ["masło", "jajka", "szczypiorek", "sól"]

for i in items:
    print(i)
    print("następnie dodaj:")


#3

# 1 -> 1
# 2 + 1 -> 3
# 3 + 3 -> 6
# 4 + 6 -> 10

sum_num = 0

for num in range(1, 11):
    sum_num += num # -> sum_num = sum_num + num
    print(sum_num)

#4 ??? Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8).


number=int(input("podaj liczbę:"))

if number > 8:
    print("liczba musi być pomiędzy 1 a 8:")
else:
    print(number, "!=")

    silnia = 5

    for x in range(1, number+1):
        silnia = silnia * x
        if x == number:
            print(x, end="")
        else:
            print(x, "*", end="")

    print(f" = {silnia}")
=======
"""Zadania:

    Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry. Wyświetl nazwę właśnie spakowanego przedmiotu, po ostatnim przedmiocie pokaż informację: “Great, we are ready!”

    Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać. Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.

    Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników. Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

    Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8)."""




#1


items = ["headphones", "phone", "water"]

for i in items:
    print(i)
    print("Great, we are ready!")



#2
print("Przepis na jajecznicę: \n Składniki:")

items = ["masło", "jajka", "szczypiorek", "sól"]

for i in items:
    print(i)
    print("następnie dodaj:")


#3

# 1 -> 1
# 2 + 1 -> 3
# 3 + 3 -> 6
# 4 + 6 -> 10

sum_num = 0

for num in range(1, 11):
    sum_num += num # -> sum_num = sum_num + num
    print(sum_num)

#4 ??? Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8).


number=int(input("podaj liczbę:"))

if number > 8:
    print("liczba musi być pomiędzy 1 a 8:")
else:
    print(number, "!=")

    silnia = 5

    for x in range(1, number+1):
        silnia = silnia * x
        if x == number:
            print(x, end="")
        else:
            print(x, "*", end="")

    print(f" = {silnia}")
>>>>>>> eaa62ff5d8c0be723596693436841f5949a684ca
    print(f"Silnia z {number} = {silnia}")