def vowel_filter(function):

    def wrapper(*args, **kwargs):
        return [letter for letter in function() if letter.lower() in "aeouiy"]
    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "o"]

print(get_letters())