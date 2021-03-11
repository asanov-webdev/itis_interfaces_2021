import os
import oschmod
import re
from constants import *


def handle_cs_a_key(path, c):
    full_path = f'{path}/{c}'
    print(full_path)

    owner = os.stat(full_path).st_uid
    path_type = '<DIR>' if os.path.isdir(full_path) else '<FILE>'
    access_rights = oct(os.stat(path).st_mode)[-3:]

    result = f'{owner}\t{access_rights}\t{path_type}\t{c}'
    print(result)


def handle_cs():
    if '--SOS' in input_parts:
        print(CS_DOCUMENTATION)
        return

    count = len(input_parts)
    path = input_parts[count - 1]

    if not os.path.isdir(path):
        print('Указанный путь не является директорией.')
        return

    contents = os.listdir(path=path)

    if '-a' in input_parts:
        for c in contents:
            handle_cs_a_key(path, c)
    else:
        for c in contents:
            print(c)


def handle_teleport():
    destination = input_parts[1]
    os.chdir(destination)


def handle_chattr_path(input_parts, path):
    for p in input_parts:
        if p[0] == '-':
            if p == '-R':
                for root, dirs, files in os.walk(path):
                    for dir in dirs:
                        handle_chattr_path(input_parts, os.path.join(root, dir))
                    for file in files:
                        handle_chattr_path(input_parts, os.path.join(root, file))
            elif p.startswith('--regex'):
                expr = p.split('=')[1]

                for n in os.listdir(path=path):
                    if re.match(expr, n):
                        handle_chattr_path(input_parts, path)
            elif p.startswith('--owner'):
                # TODO: add --owner key handling
                pass
            elif p.startswith('--ext') and os.path.isfile(path):
                ext = p.split('=')[1]
                os.rename(path, path.split('.')[0] + f'.{ext}')
            else:
                sign = '+' if p.split('=')[1] == '1' else '-'

                if p.startswith('-psr'):
                    oschmod.set_mode(path, f'go{sign}r')
                elif p.startswith('-psw'):
                    oschmod.set_mode(path, f'go{sign}w')
                elif p.startswith('-psex'):
                    oschmod.set_mode(path, f'go{sign}x')
                elif p.startswith('-psor'):
                    oschmod.set_mode(path, f'u{sign}r')
                elif p.startswith('-psow'):
                    oschmod.set_mode(path, f'u{sign}w')
                elif p.startswith('-psoex'):
                    oschmod.set_mode(path, f'u{sign}x')


def handle_chattr():
    if '--SOS' in input_parts:
        print(CHATTR_DOCUMENTATION)
        return

    count = len(input_parts)
    path = input_parts[count - 1]

    handle_chattr_path(input_parts, path)


while True:
    print(os.getcwd() + '>', end='')

    user_input = input()
    input_parts = user_input.split(' ')
    command = input_parts[0]

    if command == 'cs':
        handle_cs()
    elif command == 'teleport':
        handle_teleport()
    elif command == 'chattr':
        handle_chattr()
    else:
        print(f'"{command}" не является поддерживаемой коммандой.')
