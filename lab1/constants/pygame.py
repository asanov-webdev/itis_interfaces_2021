SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700

FONT_SIZE_MIN = 8
FONT_SIZE_MAX = 40
FONT_SIZE_STANDARD = 24
FONT = 'freesansbold.ttf'

COLORS = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
}

GUESS_DIGITS_TIME_IN_MILLISECONDS = 10000

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

NOTATION_POSITIONS = [(SCREEN_WIDTH / 3, MIDDLE_Y - MARGIN),
                      (SCREEN_WIDTH / 3, MIDDLE_Y + MARGIN)]
