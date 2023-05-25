"""7▹ Wisielec.
 Utwórz plik zawierający listę słów wg.
kategorii np. zwierzęta, owoce etc. (jedna linia po przecinku)

Poproś użytkownika o
podanie kategorii przed rozpoczęciemy gry.
 1 - zwierzeta
 2 - owoce
 3 - warzywa

 Następny wczytaj listę haseł do programu, wylosuj jedno hasło z listy.
 - wczytujemy linijkę 0 z pliku i dzielimy  przecinkiem,
 -powstanie lista elementów -> wylosowac z niej 1 slowo i przedstawic
  jak wisielca ---- + info o ilosci życ
 -puytac o literkę
 - jak zgadie to wstawic a jak nei odjąc zycie, jak wykozysta zycia to game over


 Rozgrywka powinna być maksymalnie intuicyjna."""


import random

def choose_category():
    categories = {
        1:"zwierzęta",
        2:'owoce',
        3:'warzywa'
    }
    print('wybierz kategorie: ')
    for category_id, category_name in categories.items():
        print(f'{category_id} - {category_name}')

    while True:
        category_choice = int(input('podaj nr kategorii: '))
        if category_choice in categories:
            return categories[category_choice]
        else:
            print('zły numer kategorii.')





def choose_word(category):
    words = {
        'zwierzęta': ['pies', 'wilk', 'glonojad'],
        'owoce': ['gruszka', 'truskawka', 'malina'],
        'warzywa': ['marchew', 'ziemniak', 'ogórek']
    }

    return random.choice(words[category])

def start_game(word):
    guessed_letters = []
    remaining_attempts = 4
    hidden_word = "_" * len(word)
    while remaining_attempts > 0:
        print(f"\n{hidden_word}")
        print(f"Pozostało Ci : {remaining_attempts} żyć.")
        letter = input("Podaj literę: ").lower()

        if letter in guessed_letters:
            print("Ta litera została już była.")
            continue

        guessed_letters.append(letter)

        if letter in word:
            new_hidden_word = ""
            for i in range(len(word)):
                if word[i] == letter:
                    new_hidden_word += letter
                else:
                    new_hidden_word += hidden_word[i]
            hidden_word = new_hidden_word

            if hidden_word == word:
                print("Brawo, zgadłeś!")
                break
        else:
            print("Zła litera.")
            remaining_attempts -= 1

            if remaining_attempts == 0:
                print("Przegrałeś! Hasło to:", word)
                break



def main():
    print("Witaj w  Wisielcu!")
    category = choose_category()
    word = choose_word(category)
    print(f'hasło z kategorii {category} to: ')
    start_game(word)



main()
