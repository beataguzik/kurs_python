def mood():
    print("how are you?")


def my_mood(answear):
    print("my mood t:")
    print(answear)

resp = input("how AU?")
my_mood(resp)


def my_mood(answear):
    return answear * 2

resp = input("how are you?")
twiced = my_mood(resp)
print("my mood is like", twiced)


#1 Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.

def calc_area(radius):
    pi = 3.14
    area=pi*radius**2
    return area
r=int(input ("Podaj dlugosc promienia W Twoim Kole: "))
print("pole koła=:", calc_area(r))




#2▹ Napisać funkcję, która sprawdza czy liczba jest parzysta.


def number(parzysta)

#3▹ Napisać funkcję, która przyjmuje listę liczb i zwraca sumę
# wszystki elementów na liście.

def sum_elements(items):
    result = 0
    for i in items:
        result += i
    return result

summary = sum_elements([4,6,7])
print(summary)



#4▹ Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów
# (wykorzystać funkcje z pkt 2)

"""tabliczka mnozenia?
for i in range(1,10):
       for j in range(1,11):
              print(i," x ",j," = ", i*j)"""