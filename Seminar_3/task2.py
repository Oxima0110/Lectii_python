# Пользователь вводит данные. Сделайте проверку данных 
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть 
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях

data_list = ['mju', '-12', '25', '3.14', '-25.01', 'bhKlo', 'mkjh253KIU']
for element in data_list:
    if element.lstrip('-').isdigit():
        element = int(element)
        print(f'{element} - {type(element)}')
    elif element.count('.') == 1 or element.count('.') == 1 and element.count('-') == 1:
        if element.replace('.', '').lstrip('-').isdigit():
            element = float(element)
            print(f'{element} - {type(element)}')
    elif not element.islower():
        element = element.lower()
        print(f'{element} - {type(element)}')
    else:
        element = element.upper()
        print(f'{element} - {type(element)}')

