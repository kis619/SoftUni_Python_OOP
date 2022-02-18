from itertools import permutations


def possible_permutations(numbers):
    for each in permutations(numbers):
        yield list(each)


[print(n) for n in possible_permutations([1, 2, 3])]
