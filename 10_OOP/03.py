""" Stwórz własną implementację kolejki FIFO. Klasa kolejka
(Queue) powinna na starcie przyjmować listę elementów.
Wśród metod powinny się znaleźć takie jak: wyswietlenie kolejki,
sprawdzenie czy jest pusta, dodanie elementu do kolejki
(put), wyjęcie elementu z kolejki (get).

Utwórz kilka obiektów klasy Queue z różnymi parametrami."""



class Queue:
    def __init__(self, elements=None):
        if elements is None:
            self.elements = []
        else:
            self.elements = list(elements)

    def is_empty(self):
        return len(self.elements) == 0

    def put(self, element):
        self.elements.append(element)
        print(f'dodano {element} do kolejki')

    def get(self):
        return self.elements.pop(0)

    def display(self):
        print(self.elements)


queue1 = Queue()
queue1.display()

elements = [1, 2, 3]
queue2 = Queue(elements)
queue2.display()


queue2.put(4)
queue2.display()

element = queue2.get()
print(element)
queue2.display()