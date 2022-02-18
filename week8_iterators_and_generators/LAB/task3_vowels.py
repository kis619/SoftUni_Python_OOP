class vowels:
    def __init__(self, string: str):
        self.vowels = 'AaEeOoIiYyUu'
        self.string = [letter for letter in string if letter in self.vowels]

    def __iter__(self):
        return self

    def __next__(self):
        if self.string:
            return self.string.pop(0)
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for ch in my_string:
    print(ch)