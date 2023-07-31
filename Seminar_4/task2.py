# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.


def list_cod(str_input:str)->list[int]:
    list_res = [ord(i) for i in sorted(list(str_input.replace(' ', '')), reverse=True)]
    print(list_res)


data_input = 'Пользователь вводит строку текста. Вывести каждое слово с новой строки.'
list_cod(data_input)