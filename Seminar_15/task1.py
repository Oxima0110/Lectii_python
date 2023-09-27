"""
Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
Например отлавливаем ошибку деления на ноль.
"""
import logging


logging.basicConfig(filename="log.log",
                    encoding='utf-8',
                    level=logging.ERROR)

logger = logging.getLogger(__name__)


def div(a, b):
    try:
        res = a/b
        return res
    except ZeroDivisionError:
        logger.error(f'b = {b}')


if __name__ == '__main__':
    div(1, 0)
