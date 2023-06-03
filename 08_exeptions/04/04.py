"""Oblicz średnią arymetyczną z kilku liczb.
Liczby będą podane przez użytkownika po przecinku.
Napisz funkcję, która przyjmie wartości i wyświetli średnią.
Program powinen być odporny na błędy użytkownika.
 Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku."""

def save_file_error(err):
    with open('err.txt', 'a') as file:
        file.write(err + '/n')

def main():
    numbers = input('podaj kilka liczb oddzielonych przecinkiem: ')
    list_of_numbers = numbers.split(',')

    try:
        list_of_numbers = [float(x) for x in list_of_numbers]
        mean_of_numbers = sum(list_of_numbers) / len(list_of_numbers)
        print('srednia wynosi: ', mean_of_numbers)
    except ValueError as e:
        err = 'błąd wartości' + str(e)
        save_file_error(err)

if __name__ == '__main__':
    main()