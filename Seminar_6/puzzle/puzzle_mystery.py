# Создайте модуль с функцией внутри. 
# Функция получает на вход загадку, список с возможными 
# вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была 
# отгадана загадка или ноль, если попытки исчерпаны.

__all__ = ['get_mystery']

COUNT = 3

def get_mystery(data:str, data_list:list[str], count:int = COUNT)->int:
    res = 0
    for i in range(1, count + 1):
        answ = input(f'Отгадай загадку:{data}\n - ')
        if answ.lower() in data_list:
            print(f'Вы угадали с {i} попытки')
            return i
        else:
            print('Неверно. Еще раз')
    print('Попытки закончились')
    return res


if __name__ == '__main__':
    str_input = 'Висит груша - нельзя скушать'
    list_input = ['лампочка', 'лампа']
    print(get_mystery(str_input, list_input))