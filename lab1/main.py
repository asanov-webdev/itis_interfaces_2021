import time
from classes import *
from os import environ
from constants.pygame import *
from tools.digits import *
from tools.pygame import *

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

status = AppStatus.INFO_SCREEN.value

stage = 1

init_pygame(pygame)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

standard_font = pygame.font.Font(FONT, FONT_SIZE_STANDARD)

random_set = []

full_roman = digits_to_roman(DIGITS)
full_pictograms = digits_to_pictograms(DIGITS)

current_time = time.asctime(time.localtime(time.time())).replace(' ', '_').replace(':', '.')

running = True


def handle_info_screen():
    global status

    if status == AppStatus.INFO_SCREEN.value:
        text = standard_font.render('Тест ' + str(stage), True, COLORS['black'])
        text_rect = text.get_rect(center=(MIDDLE_X, MIDDLE_Y))
        screen.blit(text, text_rect)
        pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pressed_list = pygame.key.get_pressed()

        if pressed_list[pygame.K_SPACE]:
            status = AppStatus.REMEMBER_DIGITS.value
            screen.fill(COLORS['white'])
            pygame.display.flip()
            return


def handle_remember_digits_screen():
    global random_set, status

    if status == AppStatus.REMEMBER_DIGITS.value:
        random_set = generate_random_set()
        positions = DIGIT_POSITIONS_RADIAL

        if (len(STAGES[stage]) > 2):
            needs_sorting = STAGES[stage][2]

            if needs_sorting:
                random_set.sort()
                positions = DIGIT_POSITIONS_ASCENDING

        notation = STAGES[stage][1]

        if notation == Notation.ROMAN.value:
            roman = digits_to_roman(random_set)
            roman_text_objects = get_text_objects(roman, positions, True, pygame, STAGES[stage][0])

            for e in roman_text_objects:
                screen.blit(e['text'], e['text_rect'])
        else:
            pictograms = digits_to_pictograms(random_set)
            pictograms_text_objects = get_text_objects(pictograms, positions, True, pygame,
                                                       STAGES[stage][0])

            for e in pictograms_text_objects:
                screen.blit(e['text'], e['text_rect'])

        pygame.display.flip()

        pygame.time.delay(REMEMBER_DIGITS_TIME_IN_MILLISECONDS)
        status = AppStatus.GUESS_DIGITS.value
        screen.fill(COLORS['white'])
        pygame.display.flip()


def update_results(answer):
    global current_time, random_set, stage, status

    mistakes_count = count_mistakes(random_set, answer)

    file = open('results/' + current_time + '.txt', 'a')
    file.write(str(stage) + '.\n')
    file.write('Случайный набор: ' + ''.join(str(e) for e in random_set) + '\n')
    file.write('Ответ: ' + answer + '\n')
    file.write('Количество ошибок: ' + mistakes_count + '\n')
    file.close()

    stage += 1

    status = AppStatus.INFO_SCREEN.value

    screen.fill(COLORS['white'])
    pygame.display.flip()


def handle_user_input():
    answer = ''

    text_template = standard_font.render('Введите ответ: ', 1, COLORS['black'])
    screen.blit(text_template, (SCREEN_WIDTH / 5, SCREEN_HEIGHT - MARGIN))
    pygame.display.flip()

    while True:
        if status == AppStatus.GUESS_DIGITS.value:
            event = pygame.event.poll()

            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)

                if len(key) == 1:
                    answer += key
                elif key == "backspace":
                    answer = answer[:len(answer) - 1]
                elif event.key == pygame.K_RETURN:
                    update_results(answer)
                    break

                text = standard_font.render(answer, 1, COLORS['black'])
                text_rect = pygame.Rect(MIDDLE_X + MARGIN / 2, SCREEN_HEIGHT - MARGIN, SCREEN_WIDTH, 50)

                screen.blit(screen, text_rect)
                screen.blit(text, (MIDDLE_X + MARGIN / 2, SCREEN_HEIGHT - MARGIN))

                pygame.display.update()


def handle_guess_digits_screen():
    global status

    if status == AppStatus.GUESS_DIGITS.value:
        notation = STAGES[stage][1]

        if notation == Notation.ROMAN.value:
            full_roman_text_objects = get_text_objects(full_roman, DIGIT_POSITIONS_ASCENDING, True, pygame,
                                                       FONT_SIZE_STANDARD)

            for e in full_roman_text_objects:
                screen.blit(e['text'], e['text_rect'])
        else:
            full_pictograms_text_objects = get_text_objects(full_pictograms, DIGIT_POSITIONS_ASCENDING, True, pygame,
                                                            FONT_SIZE_STANDARD)

            for e in full_pictograms_text_objects:
                screen.blit(e['text'], e['text_rect'])

        pygame.display.flip()


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        pygame.display.update()

    screen.fill(COLORS['white'])

    while stage < 31:
        handle_info_screen()

        handle_remember_digits_screen()

        handle_guess_digits_screen()

        handle_user_input()

        pygame.display.update()

pygame.quit()
