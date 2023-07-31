# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.


def str_word(str_input:str)->list[str]:
    txt_list = sorted(str_input.split(' '))
    #max_length = len(max(txt_list,key=lambda x: len(x) ))
    max_length = len(max(txt_list,key = len ))
    for i, element in enumerate(txt_list, start=1):
        print(f'{i} {element:>{max_length}}')


data_input = 'Пользователь вводит строку текста. Вывести каждое слово с новой строки.'
str_word(data_input)

