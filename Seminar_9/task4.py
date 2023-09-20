# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

def param(count: int):
    def deco(func):
        my_list = []
        def wrapper(*args, **kargs):
            for i in range(count):
                result = func(*args, **kargs)
                my_list.append(result)
            return my_list
        return wrapper
    return deco


@param(3)
def sum_(a, b):
    return a + b

if __name__ == '__main__':
    print(sum_(2, 4))
