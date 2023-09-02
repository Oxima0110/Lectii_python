# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию 
# угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.

from random import randint

def gaming(func):
    def wrapper(num2gess: int, tries: int):
        if not 100 >= num2gess >= 1:
            num2gess = randint(1, 100)
        if not 10 >= tries >= 1:
            tries = randint(1, 10)
        return func(num2gess, tries)
    return wrapper

@gaming
def guees_num(num2guess: int, tries: int):
    print(num2guess, tries)
    for _ in range(tries):
        if num2guess == int(input("Введите число: ")):
            return True
    return False


if __name__ == "__main__":
    print(guees_num(101, 11))