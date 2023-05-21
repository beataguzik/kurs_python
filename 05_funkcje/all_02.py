"""2▹ Nie korzystając z funkcji wbudowanej min(), napisz funkcję
znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c). """

def minimum_of(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c


#glowny kod
x = minimum_of(100, 25, 0)
print(x)

y = minimum_of(9, 5, 545)
print(y)