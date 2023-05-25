"""Rozpoznawanie kart. Utwórz plik zawierający numery
kart kredytowych. Sprawdź dla każdej kart jej typ.
Podziel kart do plików wg typów
np. visa.txt, mastercard.txt, americanexpress.txt."""



###################################################
def get_card_number():
    with open('visa.txt', 'r') as visa, open('mastercard.txt', 'r') as mastercard, open('americanexpres.txt', 'r)                                                                               'r') as americanexpress:
        for number in visa and mastercard and americanexpress:
            card_nr = number.readlines()
            card_nr = card_nr.replace(" ", "")
            card_nr = card_nr.replace("-", "")
        return card_nr


def is_visa(card_num):
    """Function that checks visa numbers"""
    return card_num[0] == '4' and (len(card_num) == 16 or len(card_num) == 13)
    # if card_num[0] == '4' and (len(card_num) == 16 or len(card_num) == 13):
    #     return True
    # else:
    #     return False


def is_mastercard(card_num):
    """Function that checks mastercard numbers"""
    start_condition = int(card_num[0:2]) in range(51, 56) or int(card_num[0:4]) in range(2221, 2721)

    return len(card_num) == 16 and start_condition
    # if len(card_num) == 16 and start_condition:
    #     return True
    # else:
    #     return False


def is_amex(card_num):
    """Function that checks amex numbers"""
    return len(card_num) == 15 and card_num[0:2] in ('34', '37')
    # if len(card_num) == 15 and card_num[0:2] in ('34', '37'):
    #     return True
    # else:
    #     return False


def main():
    number = get_card_number()
    print('💳 :', number)

    if is_visa(number):
        print("This is Visa card number")
    elif is_mastercard(number):
        print("This is MasterCard card number")
    elif is_amex(number):
        print("This is AmericanExpress card number")
    else:
        print("Unknown card number")



main()










def split_cards_by_type(filename):
    # Wczytanie numerów kart kredytowych z pliku
    with open(filename, 'r') as file:
        card_numbers = file.readlines()

    # Tworzenie słownika, w którym klucze to typy kart, a wartości to listy numerów kart
    cards_by_type = {}

    for card_number in card_numbers:
        card_number = card_number.strip()
        card_type = get_card_type(card_number)

        # Dodawanie numeru karty do odpowiedniej listy w słowniku cards_by_type
        if card_type in cards_by_type:
            cards_by_type[card_type].append(card_number)
        else:
            cards_by_type[card_type] = [card_number]

    # Zapisywanie kart do plików wg typów
    for card_type, card_numbers in cards_by_type.items():
        type_filename = f'{card_type}.txt'

        with open(type_filename, 'w') as file:
            file.write('\n'.join(card_numbers))

        print(f'Zapisano {len(card_numbers)} kart(y) typu {card_type} do pliku {type_filename}')

# Wywołanie funkcji split_cards_by_type z podanym nazwą pliku
split_cards_by_type('numery_kart.txt')