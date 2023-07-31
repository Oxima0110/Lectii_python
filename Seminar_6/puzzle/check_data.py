# Создайте модуль и напишите в нём функцию, которая получает 
# на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать 
# или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне 
# [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) 
# действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную 
# защищённую функцию.

# В модуль с проверкой даты добавьте возможность запуска в 
# терминале с передачей даты на проверку.

__all__ = ['check']

YEARS = range(1, 10000)
MONTHS = range(1, 13)
DAYS = range(1, 32)
LIST_30 = [4, 6, 9, 11]
DAY_30 = 30
VIS_MONTH = 2
DAY_VIS = 29

def _check_vis(year: int) -> bool:
    CHECK_NORMAL_1 = 4
    CHECK_NORMAL_2 = 100
    CHECK_NORMAL_3 = 400
    if  year % CHECK_NORMAL_1 == 0 and year % CHECK_NORMAL_2 != 0 or year % CHECK_NORMAL_3 == 0:
        return True
    return False


def check(data:str) -> bool:
    list_data = list(int(i) for i in data.split('.'))
    if list_data[0] in DAYS and list_data[1] in MONTHS and list_data[2] in YEARS:
        if list_data[0] > DAY_30 and list_data[1] in LIST_30:
            return False
        if list_data[0] > DAY_VIS  and list_data[1] == VIS_MONTH:
            return False
        if list_data[0] == DAY_VIS  and list_data[1] == VIS_MONTH and not _check_vis(list_data[2]):
            return False
        return True
    else:
        return False
    

if __name__ == '__main__':
    print(check('40.02.2020'))
    print(check('10.25.2020'))
    print(check('31.02.2020'))
    print(check('30.04.2020'))
    print(check('31.04.2020'))
    print(check('29.02.2020'))
    print(check('29.02.2021'))