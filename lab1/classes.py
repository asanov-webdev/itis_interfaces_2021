from enum import Enum


class AppStatus(Enum):
    CHOOSE_NOTATION = 0
    REMEMBER_DIGITS = 1
    GUESS_DIGITS = 2
    SHOW_RESULT = 3


class Notation(Enum):
    ROMAN = 1
    PICTOGRAMS = 2
