# ✔ Пользователь вводит строку текста. 
# ✔ Подсчитайте сколько раз встречается 
# каждая буква в строке без использования 
# метода count и с ним. 
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи 
# символа в строке. 
# ✔ Обратите внимание на порядок ключей. 
# Объясните почему они совпадают 
# или не совпадают в ваших решениях.

# Использование count
data_input = 'Пользователь вводит строку текста. Вывести каждое слово с новой строки.'
res_dict1 = {}
for element in data_input:
    if element not in res_dict1.keys():
        res_dict1[element] = data_input.count(element)
print(res_dict1)

# Без count
data_input = 'Пользователь вводит строку текста. Вывести каждое слово с новой строки.'
res_dict2 = {}
for element in data_input:
    if element not in res_dict2.keys():
        res_dict2[element] = 1
    else:
        res_dict2[element] = res_dict2[element] + 1
print(res_dict2)

