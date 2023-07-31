# Напишите функцию, которая принимает строку текста. 
# Сформируйте список с уникальными кодами Unicode каждого 
# символа введённой строки отсортированный по убыванию.

# def list_sim(str_input):
#     return [ord(i) for i in sorted(list(str_input.replace(" ", '')), reverse=True)]

# def list_sim2(str_input):
#     return  map(ord, 
#                 sorted(list(str_input.replace(" ", '')), 
#                        reverse=True))



# str_data = 'Напишите функцию, которая принимает строку текста'
# # list2 = []
# # for i in sorted(list(str_data.replace(" ", '')), reverse=True):
# #     list2.append(ord(i))
# #print(list_sim(str_data))
# print(*list_sim2(str_data))


# Функция получает на вход строку из двух чисел через пробел. 
# Сформируйте словарь, где ключом будет 
# символ из Unicode, а значением —  целое число. 
# Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.

