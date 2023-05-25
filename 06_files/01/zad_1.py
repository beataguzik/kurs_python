import random

# with open('cytaty.txt', 'r', encoding='utf-8') as fopen:
    # for line in fopen:
    #     print('Quote of the day is:')
    #     print('********************')
    #     cytat = fopen.readlines()
    #     losowy_cytat = random.choice(cytat)
    #     print(losowy_cytat.strip())
    #     print('********************')



#albo
import random

def get_content():
    new_file = input('podaj nazwę pliku z cytatami (bez txt): ')
    with open(f'{new_file}.txt', encoding='utf-8') as fopen:
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
    quotes = get_content()
    quote = random.choice(quotes)
    show(quote)

main()