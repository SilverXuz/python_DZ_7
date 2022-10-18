"""
Создать калькулятор для работы с рациональными и комплексными числами,
организовать меню, добавив в неё систему логирования.

Часть решения Романа
"""

from fractions import Fraction


def real_sum(x: Fraction, y: Fraction) -> Fraction:
    return Fraction(x) + Fraction(y)


def real_diff(x: Fraction, y: Fraction) -> Fraction:
    return Fraction(x) - Fraction(y)


def real_mult(x: Fraction, y: Fraction) -> Fraction:
    return Fraction(x) * Fraction(y)


def real_div(x: Fraction, y: Fraction) -> Fraction:
    return Fraction(x) / Fraction(y)



def real_calc(d: dict) -> Fraction:
    """
    Калькулятор принимает словарь вида {'op':0, 'x':Fraction('x'), 'y':Fraction('y')}
    + 0
    - 1
    * 2
    / 3
    """
    if d['op'] == 0:
        arifmetic = real_sum
    elif d['op'] == 1:
        arifmetic = real_diff
    elif d['op'] == 2:
        arifmetic = real_mult
    elif d['op'] == 3:
        arifmetic = real_div
    else:
        raise ValueError
    return arifmetic(d['x'], d['y'])

# d = {'op':0, 'x':Fraction('5.5'), 'y':Fraction('0')}
# result = real_calc(d)
# print(result)
