# with open('pan_tadeusz.txt') as fopen:
    # for line in fopen:
    #     print(line, end='*************')
#albo 1 linia
    # print(fopen.readline())

#albo to odczytywanie poki nie znajdzie znaku,bedzie pustka:
    # while True:
    #     current_line = fopen.readline()
    #     print(current_line)
    #     if current_line == '':
    #         break



#albo tak:
    #
    # for i in range(5):
    #     current_line = fopen.readline()
    #     print(current_line)

####################################################

def czytaj_plik():
    with open('pan_tadeusz.txt') as fopen:
        content_list = fopen.read()
    return content_list


def wyswietlaj_liste(content):
    print('***********')
    print(content)
    print('***********')

def main():
    fragment = czytaj_plik()
    wyswietlaj(fragment)

main()