def multiply(time):
    def decorator(function):
        def wrapper(num):
            return function(num) * time

        return wrapper
    return decorator

@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))