# Создайте модуль с функцией внутри. 
# Функция принимает на вход три целых числа: нижнюю и 
# верхнюю границу и количество попыток. 
# Внутри генерируется случайное число в указанных границах 
# и пользователь должен угадать его за заданное число попыток. 
# Функция выводит подсказки “больше” и “меньше”. 
# Если число угадано, возвращается истина, а если попытки 
# исчерпаны - ложь.

from random import randint as rnd

__all__ = ['guess_num']

MAX = 10
COUNT = 3

def guess_num(min_num:int, max_num:int = MAX, count:int = COUNT)-> bool:
    if min_num > max_num:
        min_num, max_num = max_num, min_num
    num = rnd(min_num, max_num + 1)
    for i in range(count):
        number = int(input(f'Угадай число которое я задумал от {min_num} до {max_num}: '))
        if number == num:
            print('Вы угадали')
            return True
        elif number < num:
            print('Мое число больше')
        else:
            print('Мое число меньше')
    print('Попытки закончились')
    return False


if __name__ == '__main__':
    print(guess_num(5, 15, 5))
    print(guess_num(5, 15))
    print(guess_num(5))
    print(guess_num(10, 5))