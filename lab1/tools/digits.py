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
    length = random.randint(1, 9)

    for i in range(length):
        index = random.randint(0, len(digits) - 1)
        set.append(digits[index])
        digits.pop(index)

    return set
