class Room:

    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people: int):
        if not self.is_taken and self.capacity >= people:
            self.is_taken = True
            self.guests += people
            return

        return f"Room number {self.number} cannot be taken"

    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            self.guests = 0
            return

        return f"Room number {self.number} is not taken"

    # def __repr__(self):
    #     return f"Room number {self.number}"
# room = Room(13, 4)
# print(room.take_room(2))
# print(room.take_room(2))
# print(room.free_room())
# print(room.free_room())

