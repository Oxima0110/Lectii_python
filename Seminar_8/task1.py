# ✔ Напишите функцию, которая генерирует 
# псевдоимена. 
# ✔ Имя должно начинаться с заглавной буквы, 
# состоять из 4-7 букв, среди которых 
# обязательно должны быть гласные. 
# ✔ Полученные имена сохраните в файл.

# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

from pathlib import Path
import json

__all__ = ['name_json']


def name_json(file_name: Path, file_name_json: Path) -> None:
    with open(file_name, 'r', encoding='utf-8') as f_read:
        file_data = {}
        for line in f_read:
            name, number = line.split()
            file_data[name.capitalize()] = float(number)
    with open(file_name_json, 'w', encoding='utf-8') as f_write:
        json.dump(file_data, f_write, ensure_ascii=False, indent=2)

# def txt_to_json(input_filename: str,
# output_filename: str):

#     with open(input_filename, 'r') as f:
#         data = f.read().split('\n')[:-1]
#         data = [{i.split()[0].capitalize():
#         float(i.split()[1])} for i in data]

#     with open(output_filename, 'w') as res:
#         json.dump(data, res, indent=4)  


if __name__ == '__main__':
    name_json('name_num.txt', 'name_num.json')