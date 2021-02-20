import random
from constants.digits import *


def digits_to_roman(digits):
    roman = []

    for d in digits:
        roman.append(ROMAN_BY_ARABIC[d])

    return roman


def digits_to_pictograms(digits):
    pictograms = []

    for d in digits:
        pictogram = ''

        for i in range(d):
            pictogram += chr(PICTOGRAM_SYMBOL_ASCII_CODE) + '-'

        pictograms.append(pictogram[:-1])

    return pictograms


def generate_random_set():
    set = []
    digits = DIGITS.copy()

    for i in range(DIGITS_AMOUNT):
        index = random.randint(0, len(digits) - 1)
        set.append(digits[index])
        digits.pop(index)

    return set


def count_mistakes(random_set, answer):
    count = 0

    set_of_strings = ''.join(str(e) for e in random_set)

    for digit in set_of_strings:
        if not (digit in answer):
            count += 1

    return str(count)
