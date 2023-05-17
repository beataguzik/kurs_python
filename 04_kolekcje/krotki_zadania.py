# #3
#
# """3▹ Stwórz krotkę liczb całkowitych. Poproś użytkownika o
#  podanie dowolnej liczby.
# Jeśli liczba znajduje się na krotce wyswietl jej indeks."""
#
#
# my_tuple = (3, 4, 5, 11, 34, 14, 2)
#
# num = int(input('Podaj liczbe do sprawdzenia->'))
#
# if num in my_tuple:
#     # podaj index tego elementu
#     print('Jest w krotce!')
#     print(f'Numer {num} pod indexem ->', my_tuple.index(num))
# else:
#     print('Nie ma w krotce')


"""1▹ Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi).
 Następnie rozpakuj tę krotkę na pojedyńcze zmienne. Wykorzystaj zmienne do wyświetlenia f-stringa,
  tak by mogło powstać zdanie np. “Mój pies, rasy border collie wabi się Dyzio”."""
# #1
my_tuple2 = ('kot', 'dachowiec', 'Pirat')
my_tuple1 = ('mój', 'to', 'nazywa się')

mt2 = list(my_tuple2)
mt1 = list(my_tuple1)

print(mt1[0], mt2[0],mt1[1], mt2[1], mt1[2], mt2[2],)


"""2▹ Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je."""



#2

mt3 = (3, 4, 4)
list_mt3 = list(mt3)
print(sorted(list_mt3))


for i in count >= 2:
    count = mt3.count(i)
    print(count)


