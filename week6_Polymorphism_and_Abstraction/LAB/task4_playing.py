def start_playing(object):
    return object.play()


class Guitar:
    def play(self):
        return "PLaying the guitar"


class Children:
    def play(self):
        return "Children are playin"

guitar = Guitar()
print(start_playing(guitar))
