"""Wywołaj błąd związany z otwarciem pliku.

    Spróbuj odczytać plik, który nie istnieje.

    Spróbuj odczytać wartość z pliku otwartym w trybie w

    Spróbuj utworzyć plik, który już istnieje w trybie x

Obsłuż w dowolny sposób każdy z powyższych błędów."""


def not_existing():
    try:
        with open("not_existing.txt", "r") as file:
            pass
    except FileNotFoundError:
        print("nie ma takiego pliku: ", file)

def existing_w():
    try:
         with open("existing_file_w.txt", "w") as file:
            file.write('treść pliku {file} to: ')
            value = file.read()
            pass
    except FileNotFoundError:
            print("Nie można odczytać pliku otwartego w trybie w.")

def existing_x():
    try:
        with open("existing_file_x.txt", "x") as file:
            pass
    except FileExistsError:
            print("Plik istnieje.")