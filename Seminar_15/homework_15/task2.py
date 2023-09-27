# Напишите код, который запрашивает число и сообщает 
# является ли оно простым или составным. Используйте 
# правило для проверки: “Число является простым, если 
# делится нацело только на единицу и на себя”. Сделайте 
# ограничение на ввод отрицательных чисел и чисел 
# больше 100 тысяч.

from functools import wraps
import logging
import argparse

FORMAT = \
    '{levelname:<8} - {asctime}. В модуле "{name}" ' \
    'в строке {lineno:03d} функция "{funcName}()" ' \
    'в {created} секунд записала сообщение: {msg}'

logging.basicConfig(format=FORMAT,
                    style='{',
                    filename="log_for_task2.log",
                    encoding='utf-8',
                    level=logging.NOTSET,
                    filemode='a')

logger = logging.getLogger(__name__)

def deco(func: callable):

    @wraps(func)
    def wrapper(num):
        try:
            if 0 < num < 100000:
                return func(num)
            else:
                logger.error('ValueError: Число должно быть положительным и меньше 100000')
                print('Число должно быть положительным и меньше 100000')
        except TypeError:
            logger.error('TypeError: Ошибка ввода')
            print('Это не то ...')
            
    return wrapper


@deco
def get_num(number):
    flag = True
    for i in range(2, number):
        if number % i == 0:
            flag = False
            break
    if flag:
        logger.info(f'Число {number}  является простым')
        result = f'Число {number}  является простым'
    else:
        logger.info(f'Число {number}  является составным')
        result = f'Число {number}  является составным'
    print(result)

def pars():
    parser = argparse.ArgumentParser(description='My first argument parser')
    parser.add_argument('-num', '--num', type=int)
    args = parser.parse_args()
    return get_num(args.num)


if __name__ == '__main__':
    # get_num(7)
    pars()
