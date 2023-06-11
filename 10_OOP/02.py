"""Utwórz klasę dla storczyków. Storczyki z zasady mają
 różne kolory, pory kwitnienia, gatunki. Utwórz dowolne atrybuty
 i metody.
Dodaj atrybut wspólny dla wszystkich storczyków - królestwo roślin."""



class Orchid:
    królestwo_roślin = "Plants"

    def __init__(self, color, flowering, species):
        self.color = color
        self.flowering = flowering
        self.species = species

    def discription(self):
        return f"Storczyk o kolorze {self.color}, kwitnie w {self.flowering}, należy do gatunku {self.species}."

    def change_color(self, new_color):
        self.color = new_color

    def change_flowering(self, new_flowering):
        self.flowering = new_flowering

    def change_species(self, new_species):
        self.species = new_species


orchid_1 = Orchid("zielony", "lato", "Phecostam")
print(orchid_1.discription())


orchid_1.change_color("czarny")
print(orchid_1.discription())