class EncryptionGenerator:
    def __init__(self, text: str):
        self.text = text

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("You must add a number.")
        new_txt = ''
        for char in self.text:
            numeric_char = ord(char) + other
            while numeric_char > 126:
                numeric_char -= 95
            while numeric_char < 32:
                numeric_char += 95
            new_txt += chr(numeric_char)

        return new_txt


some_txt = EncryptionGenerator("Super-Secret Message")
some_other_txt = EncryptionGenerator("I Love Python!")
print(some_txt + (-52))
print(some_other_txt + 'l')
