def logged(function):

    def wrapper(*args):
        return f"you called {function.__name__}{args}\n" \
               f"it returned {function(*args)}"

    return wrapper


@logged
def func(a, b):
    return a + b


print(func(1, 4))