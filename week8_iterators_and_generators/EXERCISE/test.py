from itertools import permutations


def possible_permutations(numbers):
    for perm in permutations(numbers):
        print(perm)


possible_permutations([1, 2, 3])

