def roman_to_decimal_convertor(roman_number: str):
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


roman_to_decimal = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


print(roman_to_decimal_convertor("I"))


# def roman_to_decimal_convertor(roman_number: str):   modified with help from the Internet
#
#     arabic_number = 0
#     for i in range(len(roman_number) - 1):
#         curr_letter = roman_to_decimal[roman_number[i]]
#         next_letter = roman_to_decimal[roman_number[i + 1]]
#         if curr_letter >= next_letter:
#             arabic_number += curr_letter
#         else:
#             arabic_number -= curr_letter
#
#     return arabic_number + roman_to_decimal[roman_number[-1]]
#
