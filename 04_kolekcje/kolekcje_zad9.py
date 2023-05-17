"""9▹ 5 użytkowników poproś o podanie 4 przedmiotów szkolnych,
sprawdź czy przedmioty powtarzają się na listach. Wyświetl najpopularniejszy przedmiot.
(Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi,
drukowanymi lub zaczynając od dużej litery)"""


n1= input("1 użytkowniku, podaj 4 przedmioty szkolne: ")
n2= input("2 użytkowniku, podaj 4 przedmioty szkolne: ")
n3= input("3 użytkowniku, podaj 4 przedmioty szkolne: ")
n4= input("4 użytkowniku, podaj 4 przedmioty szkolne: ")
n5= input("5 użytkowniku, podaj 4 przedmioty szkolne: ")
list_1 = [n1 + n2 + n3 + n4 + n5]
list_2 = list_1.replace(" ", "").replace(",","").replace("-","").replace(".","")
list_2 = list_2.lower()
list_2 = list_2.sorted()

print("wybrane przedmioty lista: ", list_2)
most_popular = max(set(list_2), key = list_2.count)
print("najbardziej popularny przedmiot to: ", most_popular)
