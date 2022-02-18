def type_check(type_to_check_against):

    def decorator(function):

        def wrapper(element):
            if type(element) == type_to_check_against:
                return function(element)

            return "Bad Type"

        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(4))
print(times2('Not a number'))

@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter("Hello World"))
print(first_letter(['Not', 'A', 'String']))