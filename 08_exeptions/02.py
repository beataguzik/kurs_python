""" Utwórz dowolną krotkę zawierającą kilka wartości np. 10.
 Pozwól użytkownikowi podać dowolny index oraz wartość.
Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd"""


def main():
    my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print('krotka przed zmianą: ', my_tuple)

    try:
        user_index = int(input('podaj nr indeksu: '))
        user_value = input('podaj wartość do zmiany: ')
        if user_index <0 or user_index >= len(my_tuple):
            raise IndexError('podano zly nr indeksu')

        my_list = list(my_tuple)
        my_list[user_index] = user_value
        my_tuple2 = tuple(my_list)
        print('krotka po zmianach: ', my_tuple2)

    except ValueError:
        print('podana wartość jest zła.')
    except IndexError as e:
        print(str(e))

if __name__ == '__main__':
    main()