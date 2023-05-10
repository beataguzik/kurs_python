#3▹ Nie korzystając z funkcji wbudowanej max(),
# napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).


list = [1,2,3]
print(max(list))


#inaczej

def max_of_two(val1, val2):
    

def maximum_of(a, b, c):
    tmp = ''

    if a > b:
        tmp = a
    else:
        tmp = b

    if c > tmp:
        return c
    else:
        return tmp

#glowny kod
x, y, z = [5, 13, 2]
result = maxiumum_of(x, y, z)
print()