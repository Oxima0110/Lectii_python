# ✔ Создайте вручную кортеж содержащий элементы разных типов. 
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

my_tuple = (1, 3.14, 'Hi!', 25, 'Hello!', 25.12, 16.18, 258, 'str')
my_dict = {}
for element in my_tuple:
    if type(element) not in my_dict.keys():
        my_dict[type(element)] = []
    my_dict[type(element)].append(element)
print(my_dict)
