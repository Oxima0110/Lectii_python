# Пользователь вводит строку текста. Вывести каждое слово с 
# новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки 
# Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого 
# длинного слова был один пробел между ним и номером строки.

data_input = 'Пользователь вводит строку текста. Вывести каждое слово с новой строки.'
txt_list = sorted(data_input.split(' '))
max_length = 0
for world in txt_list:
    if len(world) > max_length:
        max_length = len(world)
for i, element in enumerate(txt_list, start=1):
    print(f'{i} {element:>{max_length}}')
