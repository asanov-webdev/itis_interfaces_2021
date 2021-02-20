import random
from classes import Notation

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700

FONT_SIZE_STANDARD = 24
FONT = 'freesansbold.ttf'

COLORS = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
}

REMEMBER_DIGITS_TIME_IN_MILLISECONDS = 4000

MIDDLE_X = SCREEN_WIDTH / 2
MIDDLE_Y = SCREEN_HEIGHT / 2
MARGIN = 60

DIGIT_POSITIONS_RADIAL = [(MIDDLE_X, MIDDLE_Y),
                          (MIDDLE_X, MIDDLE_Y - MARGIN),
                          (MIDDLE_X, MIDDLE_Y + MARGIN),
                          (MIDDLE_X, MIDDLE_Y - MARGIN * 2),
                          (MIDDLE_X, MIDDLE_Y + MARGIN * 2),
                          (MIDDLE_X, MIDDLE_Y - MARGIN * 3),
                          (MIDDLE_X, MIDDLE_Y + MARGIN * 3),
                          (MIDDLE_X, MIDDLE_Y - MARGIN * 4),
                          (MIDDLE_X, MIDDLE_Y + MARGIN * 4)]

DIGIT_POSITIONS_ASCENDING = [(MIDDLE_X, MIDDLE_Y - MARGIN * 4),
                             (MIDDLE_X, MIDDLE_Y - MARGIN * 3),
                             (MIDDLE_X, MIDDLE_Y - MARGIN * 2),
                             (MIDDLE_X, MIDDLE_Y - MARGIN),
                             (MIDDLE_X, MIDDLE_Y),
                             (MIDDLE_X, MIDDLE_Y + MARGIN),
                             (MIDDLE_X, MIDDLE_Y + MARGIN * 2),
                             (MIDDLE_X, MIDDLE_Y + MARGIN * 3),
                             (MIDDLE_X, MIDDLE_Y + MARGIN * 4)]

# Value consists of font size, notation type and sorted/unsorted flag
STAGES = {
    1: [5, Notation.ROMAN.value],
    2: [10, Notation.ROMAN.value],
    3: [15, Notation.ROMAN.value],
    4: [20, Notation.ROMAN.value],
    5: [25, Notation.ROMAN.value],
    6: [30, Notation.ROMAN.value],
    7: [35, Notation.ROMAN.value],
    8: [40, Notation.ROMAN.value],
    9: [45, Notation.ROMAN.value],
    10: [50, Notation.ROMAN.value],
    11: [5, Notation.PICTOGRAMS.value],
    12: [10, Notation.PICTOGRAMS.value],
    13: [15, Notation.PICTOGRAMS.value],
    14: [20, Notation.PICTOGRAMS.value],
    15: [25, Notation.PICTOGRAMS.value],
    16: [30, Notation.PICTOGRAMS.value],
    17: [35, Notation.PICTOGRAMS.value],
    18: [40, Notation.PICTOGRAMS.value],
    19: [45, Notation.PICTOGRAMS.value],
    20: [50, Notation.PICTOGRAMS.value],
    21: [random.randint(8, 14), Notation.ROMAN.value],
    22: [random.randint(15, 35), Notation.ROMAN.value],
    23: [random.randint(36, 50), Notation.ROMAN.value],
    24: [random.randint(8, 14), Notation.PICTOGRAMS.value],
    25: [random.randint(15, 35), Notation.PICTOGRAMS.value],
    26: [random.randint(36, 50), Notation.PICTOGRAMS.value],
    27: [FONT_SIZE_STANDARD, Notation.ROMAN.value, True],
    28: [FONT_SIZE_STANDARD, Notation.ROMAN.value, False],
    29: [FONT_SIZE_STANDARD, Notation.PICTOGRAMS.value, True],
    30: [FONT_SIZE_STANDARD, Notation.PICTOGRAMS.value, False],
}
