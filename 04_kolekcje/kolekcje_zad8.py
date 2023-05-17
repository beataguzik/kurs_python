"""8▹ Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych
imion żeńskich. Zapisz imiona w wersji anglojęzycznej. Dodaj wszystki listy razem.
Nowa lista powinna zawierać 100 elementów

Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach."""

france = ['Emma', 'Jade', 'Louise', 'Alice', 'Chloé', 'Lina', 'Léa', 'Rose', 'Anna', 'Mila']
spain = ['Martina', 'Julia', 'Laia', 'Lucia', 'Maria', 'Emma', 'Noa', 'Paula', 'Ona', 'Aina']
germany = ['Sophie', 'Marie', 'Maria', 'Mia', 'Sophia', 'Emma', 'Anna', 'Hannah', 'Johanna', 'Leonie']
poland = ['Anna', 'Maria', 'Katarzyna', 'Małgorzata', 'Agnieszka', 'Barbara', 'Ewa ', 'Krystyna', 'Elżbieta', 'Magdalena']
italy = ['Sofia', 'Giulia', 'Aurora', 'Alice', 'Ginevra', 'Emma', 'Giorgia', 'Greta', 'Beatrice', 'Anna']
portugese = ['Maria', 'Matilde', 'Leonor', 'Beatriz ', 'Mariana', 'Carolina', 'Ana', 'Inês', 'Sofia', 'Margarida']
hungary = ['Hanna', 'Zoé', 'Anna', 'Emma', 'Luca', 'Lena', 'Zsófia', 'Boglárka', 'Jázmin', 'Lili']
turkey = ['Elif ', 'Zeynep', 'Hiranur', 'Miray', 'Zehra', 'Ecrin', 'Azra', 'Eylül', 'Defne', 'Nehir']
danmark = ['Eva', 'Emma', 'Hanna', 'Maria', 'Ró', 'Elsa', 'Lea', 'Sofía', 'Isabella', 'Lilja']
litwa = ['Irena', 'Janina', 'Ona', 'Danutė', 'Regina', 'Aldona', 'Kristina', 'Elena', 'Marija', 'Viktorija']


list_0 =[france + spain + germany + poland + italy + portugese + hungary + turkey + danmark + litwa]

print(list_0)
for name in list_0:
       print(len(name))

#dla każdego elementu w liscie ktory wyst min 3 razu wyswietlic go w nowej liscie
#przeliczyc ile kazdy elem wystepuje
#posortowac
#wywalic wszystkie wartosci mniejsze niz3

counting_name = {}

for name in list_0:
    if name in counting_name:
        counting_name[name] += 3
    else:
        counting_name[name] = 1

print(counting_name)

for name, counter in counting_name.items():
    print("*", name, "-", counter)







