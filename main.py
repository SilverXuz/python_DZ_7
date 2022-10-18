"""
Создать калькулятор для работы с рациональными и комплексными числами,
организовать меню, добавив в неё систему логирования.

Точка входа. Главный файл. Плюс логирование..

Работа Дарьи.
"""
from calc_fraction import real_calc
from calc_complex import complex_calc
from calc_interface import get_expression, parse_text, convert_to_complex, convert_to_fraction


def write_to_log(filename='logfile.txt', data: list = []):
    with open(filename, 'a') as output:
        output.write(" = ".join(data))
        output.write('\n')


def main():
    start = True
    question = 'Введите выражение, которое нужно вычислить. Числа и знаки отделяйте пробелом. Например 2 + 2 или 7-2j + 3+4j для комплексных чисел. И нажмите enter: \n'
    question2 = 'Если хотите продолжить нажмите ENTER. Чтобы выйти введите: выход '

    while start:
        expression = get_expression(question)
        select_calc = parse_text(expression)
        if select_calc == 1:
            d = convert_to_complex(expression)
            try:
                result = complex_calc(d)
            except ZeroDivisionError:
                print('Деление на ноль не допускается!')
        elif select_calc == 2:
            d = convert_to_fraction(expression)
            try:
                result = real_calc(d)
            except ZeroDivisionError:
                result = 'Деление на ноль не допускается!'
        else:
            result = 'Ошибка ввода!'

        write_to_log(data=[expression, str(result)])

        if result != None:
            print(result)
        answer = get_expression(question2)
        if answer.lower() == 'выход':
            start = False


if __name__ == '__main__':
    main()
