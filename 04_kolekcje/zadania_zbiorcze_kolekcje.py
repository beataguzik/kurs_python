""" 1▹ Utwórz listę lists_to_dict zawierającą listy 2 elementowe.
Przekształć ją w słownik dict_from_list."""


lists_to_dict =[ ['a', 1], ['b', 2], ['c', 3]]

dict_from_list = dict(lists_to_dict)
print(dict_from_list)

"""3▹ Utwórz dowolną tablicę n x n zawierającą dowolny znak, a następnie wyświetl
jej elementy
w formie tabeli n x n. Elementy powinny być oddzielone spacją"""

n = int(input('podaj wielkość matrycy 1-10:'))

tab = [['-']*n ]*n

for row in tab:
    print(' '.join(row))


"""
5▹ W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter."""


poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

poem = poem.lower().replace(",", "").split()
counting_word = {}

for word in poem:
    if word in counting_word:
        counting_word[word] += 1
    else:
        counting_word[word] = 1

for word, counter in counting_word.items():
    print("*", word, "-", counter)



"""7▹ Usuń duplikat z podanej list i utwórz na jej bazie krotkę.
Znajdź minimalną i maksymalną liczbę w krotce."""

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 12, 194]

example_set = set(example_list)
print(example_set)

example_tuple = tuple(example_set)
print(example_tuple)

print(min(example_tuple))
print(max(example_tuple))


