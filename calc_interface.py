'''
Модуль ввода и обработки данных от пользователя.

Выполнил Андрей.
'''

from fractions import Fraction


def get_expression(phrase: str) -> str:
    result = input(phrase)
    result = result.strip()
    result = result.replace(',', '.')
    result = result.replace('\\', '/')
    return result

def is_complex(value: str) -> bool:
    return 'j' in value


def is_real(value: str):
    pass


def parse_text(line: str) -> int:
    line_sp = line.split()
    if len(line_sp) != 3:
        return 0
    elif not line_sp[1] in '-+/*':
        return 0
    elif is_complex(line_sp[0]) or is_complex(line_sp[2]):
        return 1
    else:
        return 2


def convert_operation(value: str) -> int:
    if value == '+':
        return 0
    elif value == '-':
        return 1
    elif value == '*':
        return 2
    elif value == '/':
        return 3
    # elif value == '%': return 4
    # else:


def convert_to_complex(expresion: str) -> dict:
    values = expresion.split()
    result = {'op': convert_operation(values[1]), 'x': complex(values[0]), 'y': complex(values[2])}
    return result


def convert_to_fraction(expresion: str) -> dict:
    values = expresion.split()
    result = {'op': convert_operation(values[1]), 'x': Fraction(values[0]), 'y': Fraction(values[2])}
    return result
