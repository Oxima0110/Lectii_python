# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.


def sort_list(input_list:list)->list:
    for i in range(len(input_list)-1):
        for j in range(len(input_list)-i-1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
    print(input_list)


num_list = [7, 5, 25, 1, 38, 54, -5, 18]
sort_list(num_list)