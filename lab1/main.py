import time
from classes import *
from os import environ
from constants.pygame import SCREEN_WIDTH, SCREEN_HEIGHT
from tools.digits import *
from tools.pygame import *

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

random_set = generate_random_set()
roman = digits_to_roman(random_set)
pictograms = digits_to_pictograms(random_set)
full_roman = digits_to_roman(DIGITS)
full_pictograms = digits_to_pictograms(DIGITS)

status = AppStatus.CHOOSE_NOTATION.value
notation = Notation.ROMAN.value

active_guess_notation = 0

init_pygame(pygame)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
random_fonts = generate_random_fonts(len(roman), pygame)

standard_font = pygame.font.Font(FONT, FONT_SIZE_STANDARD)
fonts = [standard_font]

roman_text_objects = get_text_objects(roman, DIGIT_POSITIONS_RADIAL, True, random_fonts)
pictograms_text_objects = get_text_objects(pictograms, DIGIT_POSITIONS_RADIAL, True, random_fonts)

full_roman_text_objects = get_text_objects(full_roman, DIGIT_POSITIONS_ASCENDING, True, fonts)
full_pictograms_text_objects = get_text_objects(full_pictograms, DIGIT_POSITIONS_ASCENDING, True, fonts)

running = True


def highlight_active_notation():
    position_first = (SCREEN_WIDTH / 3 - 30, MIDDLE_Y - MARGIN + 10)
    position_second = (SCREEN_WIDTH / 3 - 30, MIDDLE_Y + MARGIN + 10)

    if notation == Notation.ROMAN.value:
        pygame.draw.circle(screen, COLORS['black'], position_first, 5)
        pygame.draw.circle(screen, COLORS['white'], position_second, 5)
    else:
        pygame.draw.circle(screen, COLORS['white'], position_first, 5)
        pygame.draw.circle(screen, COLORS['black'], position_second, 5)


def handle_choose_notation_screen():
    global notation, status

    screen.fill(COLORS['white'])

    highlight_active_notation()

    screen.blit(standard_font.render('Римская нотация', True, COLORS['black']), NOTATION_POSITIONS[0])
    screen.blit(standard_font.render('Пиктограммы', True, COLORS['black']), NOTATION_POSITIONS[1])

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pressed_list = pygame.key.get_pressed()

        if status == AppStatus.CHOOSE_NOTATION.value:
            if pressed_list[pygame.K_UP] or pressed_list[pygame.K_DOWN]:
                if flag_up_down:
                    notation = notation % 2 + 1
                    highlight_active_notation()
                    pygame.display.flip()
                flag_up_down = False
            else:
                flag_up_down = True

            if pressed_list[pygame.K_SPACE] or pressed_list[pygame.K_RETURN]:
                if flag_space_return:
                    status = AppStatus.REMEMBER_DIGITS.value
                    return
                flag_space_return = False
            else:
                flag_space_return = True


def handle_remember_digits_screen():
    if status == AppStatus.REMEMBER_DIGITS.value:
        if notation == Notation.ROMAN.value:
            for e in roman_text_objects:
                screen.blit(e['text'], e['text_rect'])
        else:
            for e in pictograms_text_objects:
                screen.blit(e['text'], e['text_rect'])


def handle_guess_digits_screen():
    global active_guess_notation

    if status == AppStatus.GUESS_DIGITS.value:
        if notation == Notation.ROMAN.value:
            for e in full_roman_text_objects:
                screen.blit(e['text'], e['text_rect'])
        else:
            for e in full_pictograms_text_objects:
                screen.blit(e['text'], e['text_rect'])


handle_choose_notation_screen()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if status == AppStatus.REMEMBER_DIGITS.value:
            time_taken = time.asctime(time.localtime(time.time()))
            time_taken = time_taken.replace(' ', '_')
            time_taken = time_taken.replace(':', '.')
            screenshot = 'screenshots/' + time_taken + '.png'
            pygame.image.save(screen, screenshot)

            pygame.time.delay(GUESS_DIGITS_TIME_IN_MILLISECONDS)
            status = AppStatus.GUESS_DIGITS.value

        pygame.display.update()

    screen.fill(COLORS['white'])

    handle_remember_digits_screen()

    handle_guess_digits_screen()

    pygame.display.update()

pygame.quit()
