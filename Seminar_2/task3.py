# ✔ Напишите программу, которая получает целое число и 
# возвращает  его двоичное, восьмеричное строковое 
# представление.
# ✔ Функции bin и oct используйте для проверки своего 
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода 
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

def get_res(num: int, base:int) -> str:
    res = ''
    while num != 0:
        num, digit = divmod(num, base)
        res = str(digit) + res
        # res += str(digit)
        # res = res[::-1]
    return res
    
while True:
    num = int(input('Введите число для преобразования:\n'))
    base = int(input('Введите основание 2 или 8\n'))
    match base:
        case 8 | 2:
            result = get_res(num, base)
            print(result)
            print(f'Проверка: {bin(num)}' if base == 2 else f'Проверка: {oct(num)}')
            break
        case _:
            print('Это не то...')
