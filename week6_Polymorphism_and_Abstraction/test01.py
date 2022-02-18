from birds import *
from mammals import *
from food import *


owl = Owl("Olly", 1.2, 0, .3)
hen = Hen("Henry", 1.5, 0, .3)
mouse = Mouse("Maud", .3, 0, "BG")
dog = Dog("Doggo", 4.1, 0, "DE")
cat = Cat("Katy", 3.5, 0, "EN")
tiger = Tiger("Siberia", 44, 0, "RU")
veggie = Vegetable(2)
meat = Meat(4)
print(owl.feed(veggie))
print(owl)
print(owl.feed(meat))
print(owl)

print(dog.feed(Vegetable(2)))