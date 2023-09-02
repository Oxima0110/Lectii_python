# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.

from functools import wraps
import json


def our_cash(func: callable):
    try:
        with open(f'{func.__name__}.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        arg = str(args) + str(kwargs)
        data_res = data.get(arg)
        if data_res:
            return data_res
        result = func(*args, **kwargs)
        data.update({arg: result})
        with open(f'{func.__name__}.json', 'w') as f:
            json.dump(data, f, indent=4)
        return result

    return wrapper


def param(count: int):
    def deco(func):
        my_list = []
        @wraps(func)
        def wrapper(*args, **kargs):
            for i in range(count):
                result = func(*args, **kargs)
                my_list.append(result)
            return my_list
        return wrapper
    return deco


@param(3)
@our_cash
def sum_(a, b):
    return a + b

if __name__ == '__main__':
    print(sum_(6, 4))