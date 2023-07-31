# ✔ Создайте функцию-генератор. 
# ✔ Функция генерирует N простых чисел, 
# начиная с числа 2. 
# ✔ Для проверки числа на простоту используйте 
# правило: «число является простым, если делится 
# нацело только на единицу и на себя».

NUM = 2


def simple_numbers(number: int):
    yield NUM
    for i in range(NUM + 1, number + 1):
        simple = True
        for j in range(NUM, i):
            if i % j == 0:
                simple = False
        if simple:
            yield i



print(*simple_numbers(20))