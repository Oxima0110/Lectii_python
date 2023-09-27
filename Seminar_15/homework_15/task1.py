# Треугольник существует только тогда, когда сумма 
# любых двух его сторон больше третьей. Дано a, b, c - 
# стороны предполагаемого треугольника. Требуется 
# сравнить длину каждого отрезка-стороны с суммой двух 
# других. Если хотя бы в одном случае отрезок окажется 
# больше суммы двух других, то треугольника с такими 
# сторонами не существует. Отдельно сообщить является ли 
# треугольник разносторонним, равнобедренным или 
# равносторонним.

from functools import wraps
import logging
import argparse

FORMAT = \
    '{levelname:<8} - {asctime}. В модуле "{name}" ' \
    'в строке {lineno:03d} функция "{funcName}()" ' \
    'в {created} секунд записала сообщение: {msg}'

logging.basicConfig(format=FORMAT,
                    style='{',
                    filename="log_for_task1.log",
                    encoding='utf-8',
                    level=logging.NOTSET,
                    filemode='a')

logger = logging.getLogger(__name__)


def deco(func: callable):

    @wraps(func)
    def wrapper(*args, **kwargs):
        for i in args:
            if not isinstance(i, int):
                logger.error('TypeError: Ошибка ввода')
                raise TypeError('Ошибка ввода')
            if i <= 0:
                logger.error('Число должно быть положительным')
                raise ValueError('ValueError: Число должно быть положительным')
        return func(*args, **kwargs)

    return wrapper


@deco
def triangle(a, b, c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        if a == b and b == c and c == a:
            logger.info(f'Треугольник {a}/{b}/{b} существует')
            result = 'Это треугольник \nИ это равносторонний треугольник'
        elif a == b or b == c or c == a:
            logger.info(f'Треугольник {a}/{b}/{b} существует')
            result = 'Это треугольник \nИ это равнобедренный треугольник'
        else:
            logger.info(f'Треугольник {a}/{b}/{b} существует')
            result = 'Это треугольник \nИ это разносторонний треугольник'
    else:
        logger.info(f'Треугольник {a}/{b}/{b} не существует')
        result = 'Такой треугольник не существует'
    print(result)

def pars():
    parser = argparse.ArgumentParser(description='My first argument parser')
    parser.add_argument('-a', '--a', type=int)
    parser.add_argument('-b', '--b', type=int)
    parser.add_argument('-c', '--c', type=int)
    args = parser.parse_args()
    return triangle(args.a, args.b, args.c)


if __name__ == '__main__':
    #triangle(4, 2, 3)
    pars()
