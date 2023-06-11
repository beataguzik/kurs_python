"""1▹ Skorzystaj z wprowadzenia do OOP. Stwórz klasę Pies, która posiada wspomniane atrybuty oraz metodę.

        atrybuty: imię, kolor sierści, rasę

        metody: szczekaj, machaj ogonem

Utwórz kilka obiektów klasy Pies z różnymi parametrami."""


class Dog:
    def __init__(self, name, color, race):
        self.name = name
        self.color = color
        self.race = race

    def wof(self, specjal_sound):
        return f'{specjal_sound}! - {self.name} nie szczekaj {self.color} piesku!'


    def tail_move(self):
        return f'machaj {self.name}!' * 3



bingo = Dog('bingo', 'red', 'york')
dyzio = Dog('dyzio', 'biszkoptowy', 'kundelek')


print(bingo.name)
print(bingo.tail_move())
print(dyzio.wof('HAU'))


