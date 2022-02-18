class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()




a1 = ImageArea(6, 4)
a2 = ImageArea(2, 12)
a3 = ImageArea(3, 18)

print(a1 >= a3)