class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                return room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room.free_room()

    def status(self):
        free_rooms_numbers = []
        taken_rooms_numbers = []
        guests = 0
        for room in self.rooms:
            if room.is_taken:
                taken_rooms_numbers.append(room.number)
                guests += room.guests
            else:
                free_rooms_numbers.append(room.number)
        free_rooms_numbers = ', '.join([str(room) for room in free_rooms_numbers])
        taken_rooms_numbers = ', '.join([str(room) for room in taken_rooms_numbers])
        return f"Hotel {self.name} has {guests} total guests\n" \
               f"Free rooms: {free_rooms_numbers}\n" \
               f"Taken rooms: {taken_rooms_numbers}"


