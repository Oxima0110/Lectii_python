# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.


def dict_char(num_list:list[int])->dict:
    res_dict = {chr(i):i for i in range(num_list[0], num_list[1]+1)}
    print(res_dict)


list_input = [97, 102]
dict_char(list_input)

# def str_to_dict(string: str) -> dict[str, int]:
#     result = {}
#     start, end = sorted(map(int, string.split()))
#     for i in range(start, end + 1):
#         result[chr(i)] = i
#     return result


# print(str_to_dict("2 9"))