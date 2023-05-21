"""6▹ Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji."""


import random
# słownik wygrany: przegrany

WINNERS = {
    'k': ('n', 'j'),
    'n': ('p', 'j'),
    'p': ('k', 's'),
}
CORRECT_VALUES = ['k', 'n', 'p', 'j', 's']

def get_comp_choice():
    return random.choice(CORRECT_VALUES)


def get_user_choice():
    while True:
        user_choice = input("""Podaj wartość:
                    k - kamień
                    n - nożyce
                    p - papier 
                    j - jaszczurka
                    s - Spock
        -> """)

        if user_choice in CORRECT_VALUES:
            break #return user_choice
        else:
            print('Nieprawidłowa wartość')
            print("--- spróbuj jeszcze raz! ---")

    return user_choice

def show_result(comp, user):
    if comp == user:
        print('Remis')
    elif comp in WINNERS[user]:
        print('Wygrana użytkownika')
    else:
        print('Wygrywa komputer')


def main():
    while True:
        comp = get_comp_choice()
        user = get_user_choice()
        print("-------WYBORY --------")
        print(f'komputer -> {comp} vs user -> {user}')
        show_result(comp, user)

        ply_again = (input("gramy jeszcze raz? t/n"))

        if ply_again.upper() == "N":
            break


main()