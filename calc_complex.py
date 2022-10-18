#  Модуль вычислений с комплексными числами - выполнила Гугина Екатерина


def complex_sum(x: complex, y: complex) -> complex:
    return complex(x) + complex(y)


def complex_diff(x: complex, y: complex) -> complex:
    return complex(x) - complex(y)


def complex_mult(x: complex, y: complex) -> complex:
    return complex(x) * complex(y)


def complex_div(x: complex, y: complex) -> complex:
    return complex(x) / complex(y)


def complex_calc(d: dict) -> complex:
    """
    Калькулятор принимает словарь вида {'op':0, 'x':complex('x'), 'y':complex('y')}
    + 0
    - 1
    * 2
    / 3
    """
    if d['op'] == 0:
        arifmetic = complex_sum
    elif d['op'] == 1:
        arifmetic = complex_diff
    elif d['op'] == 2:
        arifmetic = complex_mult
    elif d['op'] == 3:
        arifmetic = complex_div
    else:
        raise ValueError
    return arifmetic(d['x'], d['y'])
