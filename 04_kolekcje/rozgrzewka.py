list=[1, 4, 3, 528, 2]

#1 kopia listy
list2=a.copy
print(list2)
Zad 1
>>> arr = [3, 5, 6, 7, 9, 2 ]
>>> copy_arr = arr[ : ]
>>> print(copy_arr)
[3, 5, 6, 7, 9, 2]
>>> print(copy_arr)
[3, 5, 6, 7, 9, 2]
>>> copy_arr2 = arr.copy()
>>> copy_arr2
[3, 5, 6, 7, 9, 2]


#2 metoda posortuje elementy listy


print(list.sort())

>>> arr
[3, 5, 6, 7, 9, 2]
>>> arr.sort()
>>> arr
[2, 3, 5, 6, 7, 9]
>>> arr2 = [4, 6, 1, 5, 3, 7]
>>> sorted(arr2)
[1, 3, 4, 5, 6, 7]
>>> print(arr2)
[4, 6, 1, 5, 3, 7]
>>> arr2_sorted = sorted(arr2)
>>> print(arr2_sorted)
[1, 3, 4, 5, 6, 7]
>>> print(arr2)
[4, 6, 1, 5, 3, 7]




#3co usunie wszystko z listy i nie usunie listy

list.clear()

#4policzy wystapienie tego sam elem na liscie
list=[1,2.3,2,4,2,7,2,2]
list.count(2)



#5 suma liczb na liscie

sum(list)