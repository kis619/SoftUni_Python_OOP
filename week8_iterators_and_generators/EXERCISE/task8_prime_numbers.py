def get_primes(numbers: list):
    for num in numbers:
        if is_prime(num):
            yield num


def is_prime(number):

    for i in range(2, number):
        if number % i == 0:
            return False

    return number > 1


print(list(get_primes([2, 4, -3, 5, 6, 9, 1, 0])))
