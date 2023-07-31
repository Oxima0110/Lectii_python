# Посчитайте сумму чётных элементов от 1 до n исключая 
# кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n.

n = 8
e = 6
i = 1
result = 0
while i < n:
    if i % 2 == 0:
        if i % e != 0:
            result= result + i   
    i+=1
print(result)