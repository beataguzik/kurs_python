print("podaj ile litrów paliwa spala auto na 100km:")
consumption=float(input())
print("podaj jaki dystans chcesz pokonać:")
distance=float(input())
print("cena 1l paliwa:")
price=float(input())
cost=(distance/100)*consumption*price



print("Koszt trasy to:",cost)


