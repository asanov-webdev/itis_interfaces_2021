import random
from constants.pygame import *


def init_pygame(pygame):
    pygame.init()

    pygame.display.set_caption('lab1')

    icon = pygame.image.load('icon.png')
    pygame.display.set_icon(icon)


def get_text_objects(digits, positions, center, pygame, font_size):
    text_objects = []

    for i in range(len(digits)):
        font = pygame.font.Font(FONT, font_size)
        text = font.render(digits[i], True, COLORS['black'])

        if center:
            text_rect = text.get_rect(center=positions[i])
        else:
            text_rect = text.get_rect(topleft=positions[i])

        text_objects.append({'text': text, 'text_rect': text_rect})

    return text_objects
