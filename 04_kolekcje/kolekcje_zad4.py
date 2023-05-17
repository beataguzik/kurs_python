# 1.
"""Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10,
wypełnioną wynikami mnożenia wiersz × kolumna."""

list_1 = range(1, 11)
list_2 = range(1, 11)

for a in list_1:
    for b in list_2:
        print(a, "*", b, "=", a*b)