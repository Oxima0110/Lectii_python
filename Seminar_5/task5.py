# ✔ Напишите программу, которая выводит 
# на экран числа от 1 до 100. 
# ✔ При этом вместо чисел, кратных трем, 
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz». 
# ✔ Если число кратно и 3, и 5, то программа 
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

NUM_MIN = 1
NUM_MAX = 100
CHECK_1 = 3
CHECK_2 = 5


def my_gen1(min:int, max:int):
    for i in range(min, max + 1):
        if i % (CHECK_1*CHECK_2) == 0:
            i = 'FizzBuzz'
        elif i % CHECK_1 == 0:
            i = 'Fizz'
        elif i % CHECK_2 == 0:
            i = 'Buzz'
        yield i


def my_gen2(min:int, max:int):
    return ('FizzBuzz' if i % (CHECK_1*CHECK_2) == 0 
            else 'Fizz' if i % CHECK_1 == 0 
            else 'Buzz' if i % CHECK_2 == 0 
            else i for i in range(NUM_MIN, NUM_MAX + 1))


print(*my_gen1(NUM_MIN, NUM_MAX))
print(*my_gen2(NUM_MIN, NUM_MAX))