class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species


def animal_sound(animals: list):
    dicky = {
        'cat': 'meow',
        'dog': 'woof-woof',
        'chicken': 'chick',
        'elephant': 'el_noise',
    }
    for animal in animals:
        print(dicky[animal.species])


animals = [Animal('cat'), Animal('dog'), Animal('chicken'), Animal('elephant')]
animal_sound(animals)

# добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
# при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
