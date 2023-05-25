import random




def find_longest_sequence(word):
    longest_sequence = ''
    current_sequence = ''
    previous_char = None
    for char in word:
        if char == previous_char:
            current_sequence += char
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            current_sequence = char
            previous_char = char
    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence
    return longest_sequence, len(longest_sequence)

var = input('podaj ciąg znaków do sprawdzenia: ')
result = find_longest_sequence(var)
print('teraz obliczę najdłuższy ciąg powtarzających się znaków w podanym ciągu:')
print(result)



def generate_test_instance(length, characters):
    sequence = [random.choice(characters)]
    while len(sequence) < length:
        if random.random() < 0.5:
            sequence.append(sequence[-1])
        else:
            sequence.append(random.choice(characters))
    return ''.join(sequence)

characters = input("Podaj znaki, oddzielając je przecinkami: ").split(',')
test_instance = generate_test_instance(4, characters)
print('teraz z podanych znaków stworzę ciąg:')
print(test_instance)
