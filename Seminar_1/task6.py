# Напишите программу, которая запрашивает год и проверяет 
# его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

year = int(input('Введите год:\n'))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            result = 'Високосный'
        else:
            result = 'Обычный'   
    else:
        result = 'Високосный'
else:
    result = 'Обычный'
print(result)

def check_leap_year(year: str) -> bool:
    CHECK_NORMAL_1 = 4
    CHECK_NORMAL_2 = 100
    CHECK_NORMAL_3 = 400
    # YEARS = range(1, 10000)
    # year = int(date.split(".")[-1])
    if  year % CHECK_NORMAL_1 == 0 and year % CHECK_NORMAL_2 != 0 or year % CHECK_NORMAL_3 == 0:
        return True
    return False

print(check_leap_year(2020))