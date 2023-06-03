""" Wróć do pierwszego zadania z lekcji o plikach,
zmodyfikuj go tak, aby to użytkownik podawał nazwę pliku z
cytatami. Pamiętaj, by użytkownik po wykonaniu błędnej akcji
(np. literówki w nazwie pliku) miał możliwość poprawić swój błąd."""



import random
def get_content():
    while True:
        filename = input('Podaj nazwe pliku (bez rozszerzenia txt)')
        try:
            with open(f'{filename}.txt') as fopen:
                content = fopen.readlines()
                return content
        except FileNotFoundError:
            print('nie ma takiego pliku, spróbuj jeszcze raz')


def show(quote):
    txt, author = quote.split(' - ')
    print('Quote of the day is:')
    print()
    width = 70
    print('*' * width)
    print(txt.center(width))
    print(author.strip().center(width))
    print('*' * width)


def main():
    quotes = get_content()
    quote = random.choice(quotes)
    show(quote)

main()