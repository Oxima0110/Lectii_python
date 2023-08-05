# ✔ Напишите функцию, которая генерирует 
# псевдоимена. 
# ✔ Имя должно начинаться с заглавной буквы, 
# состоять из 4-7 букв, среди которых 
# обязательно должны быть гласные. 
# ✔ Полученные имена сохраните в файл.

from pathlib import Path
from random import randint, choice

__all__ = ['get_name']

VOWES = 'aeiouy'
CONSTONATS = 'bcdfghjklmnqrstvwxz'


def get_name(count: int, name_len_min: int, name_len_max: int, file_2: Path) -> None:
    with open(file_2, 'a', encoding='utf-8') as f_2:
        for _ in range(count):
            rad_string = ''.join(choice(VOWES) if i % 3 == 0 else choice(CONSTONATS)
                                 for i in range(1, randint(name_len_min + 1, name_len_max + 1)))
            f_2.write(f'{rad_string.capitalize()}\n')


# from random import randint


# def give_name() -> str:
#     name: str = ''
#     for _ in range(randint(4, 7)):
#         name += chr(randint(98, 122))
#     return name.capitalize()


# def fill_in_file_names(name_file: str, count_line: int) -> None:
#     name_file += '.txt'

#     with open(name_file, 'a', encoding='utf-8') as file:
#         for _ in range(count_line):
#             file.write(f"{give_name()}\n")


if __name__ == '__main__':
    get_name(5, 3, 7, 'task2.txt')