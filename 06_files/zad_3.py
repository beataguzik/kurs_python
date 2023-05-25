def get_content():
    new_file = input('podaj nazwę pliku z cytatami (bez txt): ')
    with open(f'{new_file}.txt', encoding='utf-8') as fopen:
        content = fopen.readlines()
    return content


def main():
    quotes = get_content()
    for id in range(5):
        print(quotes[id])



main()
