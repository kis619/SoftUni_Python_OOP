class store_results:
    file = "results.txt"

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        with open(self.file, 'a') as file:
            file.writelines(
                f"Function '{self.function.__name__}' was called. Result: {self.function(*args, **kwargs)}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


print(add(2, 2))
print(mult(6, 4))
