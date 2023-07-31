# ✔ Напишите программу, которая решает 
# квадратные уравнения даже если 
# дискриминант отрицательный. 
# ✔ Используйте комплексные числа 
# для извлечения квадратного корня.


import decimal

a = 1
b = -6
c = 34
d = b**2 - 4*a*c
decimal.getcontext().prec = 4
if d != 0:
    x1 = (-b + d**0.5) / (2*a)
    x2 = (-b - d**0.5) / (2*a)
    result = 'уpaвнeниe имeeт 2 кopня: x1=' + str(x1) + ' x2=' + str(x2)
else:
    x = (-b) / (2*a)
    x = decimal.Decimal(x)
    result = 'уpaвнeниe имeeт 1 кopeнь: x=' + str(x)
print(result)

