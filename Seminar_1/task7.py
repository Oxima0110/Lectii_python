# Пользователь вводит число от 1 до 999. Используя операции 
# с числами сообщите что введено: цифра, двузначное число 
# или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

def get_number(input_string:str)->int:
    '''
    Получение числа
    '''
    while True:
        try:
            num = int(input(input_string))
            if 0 < num < 1000: 
                return num
            else:
                print('Число должно быть от 1 до 999')
        except ValueError:
            print('Это не то ...')

number = get_number('Введите число от 1 до 999\n')
if 0 < number < 10:
    result = number ** 2
    result = 'Это цифра, квадрат числа = ' + str(result)
elif 9 < number < 100:
    num1 = number % 10
    num2 = (number % 100) // 10
    result = num1 * num2
    result = 'Это двузначное число, произведение его цифр = ' + str(result)
else:
    num1 = number % 10
    num2 = (number % 100) // 10
    num3 = (number % 1000) // 100
    result = num1*100 + num2*10 + num3
    result = 'Это двузначное число, его зеркальное отображение = ' + str(result)
print(result)