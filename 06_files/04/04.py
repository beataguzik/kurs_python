#Wyświetl 3 losowe cytaty

import random

def get_content():
    with open('cytaty.txt', encoding='utf-8') as fopen:
        content = fopen.readlines()

    return content


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
    quotes_1 = get_content()
    quotes_2 = get_content()
    quote = random.choice(quotes_1 + quotes_2)
    show(quote)

main()