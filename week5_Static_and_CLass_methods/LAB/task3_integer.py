import math


class Integer:

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"

        return cls(math.floor(float_value))

    @classmethod
    def from_roman(cls, value):
        return cls(Integer.roman_to_decimal_convertor(value))

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return 'wrong type'
        try:
            value = eval(value)
            if isinstance(value, int):
                return cls(value)
        except ValueError:
            return 'wrong type'

    @staticmethod
    def roman_to_decimal_convertor(roman_number: str):
        roman_to_decimal = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        arabic_number = roman_to_decimal[roman_number[0]]
        for i in range(len(roman_number) - 1):
            curr_letter = roman_to_decimal[roman_number[i]]
            next_letter = roman_to_decimal[roman_number[i + 1]]
            if curr_letter >= next_letter:
                arabic_number += next_letter
            else:
                arabic_number -= curr_letter
                arabic_number += abs(curr_letter - next_letter)
        return arabic_number



import unittest


class IntegerTests(unittest.TestCase):
    def test_basic_init(self):
        integer = Integer(1)
        self.assertEqual(integer.value, 1)

    def test_from_float_success(self):
        integer = Integer.from_float(2.5)
        self.assertEqual(integer.value, 2)

    def test_from_float_wrong_type(self):
        result = Integer.from_float("2.5")
        self.assertEqual(result, "value is not a float")

    def test_from_roman(self):
        integer = Integer.from_roman("XIX")
        self.assertEqual(integer.value, 19)

    def test_from_string_success(self):
        integer = Integer.from_string("10")
        self.assertEqual(integer.value, 10)

    def test_from_string_wrong_type(self):
        result = Integer.from_string(1.5)
        self.assertEqual(result, "wrong type")


if __name__ == "__main__":
    unittest.main()

