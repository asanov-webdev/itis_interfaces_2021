import random
from constants.pygame import *


def init_pygame(pygame):
    pygame.init()

    pygame.display.set_caption('lab1')

    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)


def get_text_objects(digits, positions, center, fonts=[]):
    text_objects = []

    for i in range(len(digits)):
        if len(fonts) > 1:
            font = fonts[i]
        else:
            font = fonts[0]

        text = font.render(digits[i], True, COLORS['black'])

        if center:
            text_rect = text.get_rect(center=positions[i])
        else:
            text_rect = text.get_rect(topleft=positions[i])

        text_objects.append({'text': text, 'text_rect': text_rect})

    return text_objects


def generate_random_fonts(count, pygame):
    fonts = []

    for i in range(count):
        font_size = random.randint(FONT_SIZE_MIN, FONT_SIZE_MAX)
        font = pygame.font.Font(FONT, font_size)
        fonts.append(font)

    return fonts
