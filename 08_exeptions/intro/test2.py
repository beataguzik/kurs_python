def my_function():
    # return 0 /10 -> zero div
    # return int('aaaa') -> value error
    # return "aaa" + 3 #-> type error
    # x = 10
    # my_list = [1,2]
    # return my_list[x]
    raise ValueError('wiadomosc') # -> pokazuje bład

def main():
    try:
        my_function()
    except ValueError as e:
        # handle ValueError exception
        print("Błąd wartosci", e)

    except (TypeError, ZeroDivisionError) as e:
        print('☀️ ->', e)

    finally::
        print('zawsze działam')

    print('🌞🌞🌞' * 10)

if __name__ == "__main__":
    main()