#1  Utwórz dowolną krotkę, w której elementy mogą się
# powtarzać.
# Przekształć ją w set.


krotka = (1, 2, 3, 3, 2)
krotka_w_set = set(krotka)
print(krotka_w_set)

#2▹ Utwórz listę L_test = [1, 2, 3, 4], krotkę T_test = (1, 2, 3, 4) oraz set S_test = {1, 2, 3, 4}.
# Jakie metody dostępne dla typu list nie będą działać dla typów tuple i set?

L_test = [1, 2, 3, 4]
T_test = (1, 2, 3, 4)
S_test = {1, 2, 3, 4}

# nie zadziała metoda insert, remove or sort ?


#3 Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem
# elementów o parzystym indeksie z pierwszej krotki,
# a oraz nieparzystych elementów z drugiej.
# Przekształć powstałą listę w set.

krot1 = (1, 5, 52, 7, 4, 5)
krot2 = (20, 21, 22, 23, 24, 25)

lista_krot = list(krot1[::2] + krot2[1:: 2])

print(lista_krot)

lista_w_set = set(lista_krot)
print(lista_w_set)