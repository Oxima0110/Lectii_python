# ✔ Напишите программу, которая вычисляет площадь 
# круга и длину окружности по введённому диаметру. 
# ✔ Диаметр не превышает 1000 у.е. 
# ✔ Точность вычислений должна составлять 
# не менее 42 знаков после запятой.

import math
import decimal

def get_number(input_string:str)->int:
    '''
    Получение окружности
    '''
    while True:
        try:
            num = int(input(input_string))
            if 0 < num <= 1000: 
                return num
            else:
                print('Число должно быть положительным и не больше 1000')
        except ValueError:
            print('Это не то ...')


decimal.getcontext().prec = 44
d = get_number('Введите диаметр окружности до 1000 у.е.\n')
d = decimal.Decimal(d)
pi_ = decimal.Decimal(math.pi)
s = (pi_ * d**2)/4 
l = pi_ * d
print(f'площадь круга = {s}, длина окружности = {l}')