# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

# удаление элемента встречающегося дважды
NUM = 2
my_list = [1, 2, 4, 2, 4, 6 , 8 , 4, 9, 6, 4]
for element in my_list:
    if my_list.count(element) % 2 == 0:
        my_list.remove(element)
        my_list.pop(my_list.index(element))
print(my_list)

# удаление всех повторяющихся элементов

my_list = [1, 2, 4, 2, 4, 6 , 8 , 9, 6, 4]
for element in my_list:
    if my_list.count(element) != 1:
        for i in range(my_list.count(element)):
            my_list.remove(element)
print(my_list)