"""Pomyśl co sprawia, że ssak jest ssakiem? Utwórz klasę
 ssaki.
Stwórz kilka obiektów klasy ssaki np. wilk, koń, ssaki."""


#ssaki sa zyworodne wiec rodza sobie dzieci, po wywolaniu
# ssaka wyswietli sei nazwa jego dziecka


class Mammal:
    def __init__(self, species, children):
        self.species = species
        self.children = children
        self.zyworodne = True


    def if_zyworodny(self):
        if self.zyworodne:
            print(f'{self.species} jest ssakiem żyworodnym, a jego dziecko to: {self.children}.')
        else:
            print(f'{self.species} nie jest ssakiem żyworodnym.')

mammal1 = Mammal('Kot', 'koteczek')
mammal1.if_zyworodny()


mammal2 = Mammal('Pies', 'szczeniak')
mammal2.if_zyworodny()

