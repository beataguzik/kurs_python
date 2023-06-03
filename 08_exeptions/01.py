# 1▹ Stwórz listę składającą się z kilku elementów różnego
# typu np. [13, ‘string’, 2.45] itp. W pętli spróbuj wykonać
# dzielenie 10 przez wartość z listy.
# Złap wyjątki jakie mogą się przy tej okazji wydarzyć.


def main():
    list = [5, 'woda', 5.458, 'jak', 56, 8]


    for elem in list:
        try:
            x = 10 / elem
            print(f'dzielenie 10 przez {elem} daje wynik: {x}')
        except ZeroDivisionError:
            print('nie dzielimy przez 0')
        except TypeError:
            print(f'nie dzielimy przez slowa')


if __name__ == "__main__":
    main()
    #
    #
    # def main():
    #     candidates = [13, "string", 2.45, 0, True, False, (1, 2)]
    #
    #     for i in candidates:
    #         try:
    #             a = 10 / i
    #             print(a)
    #         except (TypeError, ZeroDivisionError) as e:
    #             print(e)
    #
    #
    # if __name__ == "__main__":
    #     main()





