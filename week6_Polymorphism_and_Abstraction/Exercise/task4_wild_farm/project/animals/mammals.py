from project.animals.animal import Mammal
from project.food import *


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, wing_size):
        super().__init__(name, weight, wing_size)
        self.foods_to_eat = [Vegetable, Fruit]
        self.weight_per_food = 0.1

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    def __init__(self, name: str, weight: float, wing_size):
        super().__init__(name, weight, wing_size)
        self.foods_to_eat = [Meat]
        self.weight_per_food = 0.4

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    def __init__(self, name: str, weight: float, wing_size):
        super().__init__(name, weight, wing_size)
        self.foods_to_eat = [Vegetable, Meat]
        self.weight_per_food = 0.3

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, wing_size):
        super().__init__(name, weight, wing_size)
        self.foods_to_eat = [Meat]
        self.weight_per_food = 1

    def make_sound(self):
        return "ROAR!!!"
