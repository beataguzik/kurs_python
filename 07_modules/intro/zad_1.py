""" Stwórz moduł, który będzie przechowywał funkcję
obliczającą bmi.py. Zaimportuj module do pliku fitmeter.py.
Nowy plik będzie informował użytkownika o jego aktualnym BMI i na
podstawie wyniku (niedowaga, nadwaga, otyłość) sugerował zmiany w
stylu życia pobierane z odpowiedniego pliku.

    Utwórz plik bmi.py zawierający metodę obliczania bmi.

    Metoda zwraca wartości: niedowaga, waga normalna, nadwaga, otyłość.

    Utwórz 4 pliki .txt zawierające porady.

    Utwórz plik fitmeter.py, który zaimportuje moduł bmi.

    fitmeter.py pobierze wagę i wzrost pacjenta i przekaże do odpowiedniej funkcji z modułu bmi.

    Na podstawie zwróconej wartości fitmeter.py wyświetli odpowiednie porady dla pacjenta.
"""


def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        answer = read_from_file('Underweight.txt')
    elif bmi < 25:
        answer = read_from_file('Normal.txt')
    elif bmi < 30:
        answer = read_from_file('Overweight.txt')
    else:
        answer = read_from_file('Obese.txt')
    return answer


def read_from_file(filename):
    with open(filename) as f:
        lines = f.read()
        return lines


