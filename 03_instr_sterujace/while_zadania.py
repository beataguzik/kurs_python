"""                 Zadania:

1) Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach. Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.

    C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit

Napisz rozwiązanie zarówno z użyciem pętli while jak i for.

2) Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5). Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie."""


#1

fahr = 0

while fahr <= 200:
    celc = round(5 / 9 * (fahr - 32), 2)
    print(f"temp {fahr} F -> {celc} C")
    fahr += 20

#2


numb2 = 5
while True:
    numb1 = int(input("odgadnij moją liczbę w przedziale 0-20:"))
    if numb1 != numb2:
        print("zle, spróbuj jeszcze raz")
        continue
    elif numb1 == numb2:
        print("brawo - zgadłeś")
        break
