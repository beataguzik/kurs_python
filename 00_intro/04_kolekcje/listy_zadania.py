#1
"""1▹ Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę
w góry.
Elementy na liście posortuj alfabetycznie, a następnie wyświetl."""


list=['telefon', 'woda', 'plecak', 'kanapka']
list.sort(
)
print(list)
for elem in list:
    print(elem, "!")
#2

"""2▹ Pobierz od użytkownika 10 liczb,
wyświetl tylko te, które są nieparzyste."""


list=(input("podaj 10 cyfr po spacji:"))

list=list.split()
sorted(list)
print(list[0::2])

#3
"""3▹ Dla podanej przez użytkownika liście liczb całkowitych
sprawdź
czy pierwszy i ostatni element są takie same."""

#1 opcja
arr=input("podaj słowa po spacji:")
arr=arr.split()
print(arr)
print(arr[0])
print (arr[-1])
if arr[0] == arr[-1]:
    print('takie same')
else:
    print('nie są takie same')

#2opcja
arr=[]
num=int(input('ile chcesz podac elem:'))
for _ in range(num):
    item=input('podaj element:')
    arr.append(item) #dodaje kolejne elementy
    print(arr)

#4
"""Pobierz od użytkownika parzystą listę elementów.
 Sprawdź czy 2 środkowe elementy są takie same. """


list2=input("podaj 4 różne cyfry po spacji:")
list2=list2.split()
print(list2)
print(list2[1])
print(list2[2])
if list2[1] == list2[2]:
    print("dwa srodkowe elementy są takie same")
else:
    print("dwa srodkowe elementy nie są takie same")





#5

people = [
    ['Dorota', 'Wellman', 'dziennikarka'],
    ['Adam', 'Małysz', 'sportowiec'],
    ['Robert', 'Lewandowski', 'piłkarz'],
    ['Krystyna', 'Janda', 'aktorka']
]

# for row in people:
#     # print(row[0], row[1], '-', row[2])
#     print(" - ".join(row))

print('---------')

for row in people:
    for id, elem in enumerate(row):
        if id == 1:
            print(elem, end=" - ")
        else:
            print(elem, end=" ")
    print()

