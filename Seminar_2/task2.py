# Создайте в переменной data список значений разных типов 
# перечислив их через запятую внутри квадратных скобок. 
# Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на 
# результаты.

data = [1, 'Hello', 3.14, 1, 'Hi!', 2.5, 'Hello', 'a']

for num, element in enumerate(data, start=1):
    if isinstance(element, int):
        element_type = 'INT'
    elif isinstance(element, str):
        element_type = 'STR'
    print(num, element)
    print(f'адрес в памяти:{id(element)}\nразмер в памяти: {element.__sizeof__()}\nхэш объекта{hash(element)}\n{element_type}')