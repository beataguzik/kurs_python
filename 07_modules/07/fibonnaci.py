def fibonacci(x):
    sequence = []
    a, b = 0, 1

    while len(sequence) < x:
        sequence.append(a)
        a, b = b, a + b

    return sequence

def main():
    x = int(input('podaj cyfrę do stworzenia ciągu fibonnaciego: '))
    fib_sequence = fibonacci(x)
    print(fib_sequence)


main()