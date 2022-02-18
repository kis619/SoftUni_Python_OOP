from project.animals.animal import Bird
from ..food import *


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size):
        super().__init__(name, weight, wing_size)
        self.foods_to_eat = [Meat]
        self.weight_per_food = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size):
        super().__init__(name, weight, wing_size)
        self.foods_to_eat = [Meat, Vegetable, Fruit, Seed]
        self.weight_per_food = 0.35

    def make_sound(self):
        return "Cluck"
