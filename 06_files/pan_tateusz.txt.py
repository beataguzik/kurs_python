#otwieranie pliku txt w python, trzeba zapamietac o zamkcieciu (close)

f = open("pan_tadeusz.txt")
print(f.readline())
f.close()
print('---------------------------------')



# albo tak i to juz zamyka plik samo
with open("pan_tadeusz.txt", encoding='utf-8') as zawartosc:
    print(zawartosc.readline())
print('---------------------------------')


#otwiera całośc i pozakuje takie samo format jak w pliku,
# a readlines() pokaze wszystko razem
# filename = 'pan_tadeusz.txt'
#
# with open(filename, 'r') as f:
#   content = f.read()
#   print(content)
#
# #################################
#
# try:
#     with open('pan_tadeusz.txt', 'x') as file:
#         file.write('hello')
# except FileExistsError:
#     print('plik juz istnieje')