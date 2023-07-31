# ✔ Создайте генератор чётных чисел от нуля до 100. 
# ✔ Из последовательности исключите 
# числа, сумма цифр которых равна 8. 
# ✔ Решение в одну строку.

NUM = 100
CHECK = 8
def my_gen1():
    return (i for i in range(0, NUM + 1, 2) if 
          sum(map(int, str(i).strip())) != CHECK)

def my_gen2():
    return (i for i in range(0, NUM + 1, 2) if 
          i // 10 + i % 10 != CHECK)



print(*my_gen1())
print(*my_gen2())
