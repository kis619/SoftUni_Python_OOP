class Calculator:
    @staticmethod
    def add(*args):
        result = 0
        for number in args:
            result += number

        return result

    @staticmethod
    def multiply(*args):
        result = 1
        if args:
            for number in args:
                result *= number
            return result

    @staticmethod
    def divide(*args):
        result = 0
        for i in range(len(args) - 1):
            if args[i + 1]:
                result += args[i] / args[i + 1]

        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for number in args[1:]:
            result -= number

        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 0))
print(Calculator.subtract(90, 20, -50, 43, 7))
