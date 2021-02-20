from enum import Enum


class AppStatus(Enum):
    INFO_SCREEN = 0
    REMEMBER_DIGITS = 1
    GUESS_DIGITS = 2


class Notation(Enum):
    ROMAN = 0
    PICTOGRAMS = 1
