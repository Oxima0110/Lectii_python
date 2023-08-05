# ✔ Напишите функцию, которая открывает на чтение созданные 
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните 
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя 
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя 
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, 
# сколько в более длинном файле. 
# ✔ При достижении конца более короткого файла, 
# возвращайтесь в его начало.


__all__ = ['num_name']

def get_line(name:str)->str:
    line = name.readline()
    if not line:
        name.seek(0)
        return get_line(name)
    return line[:-1]

    
def num_name(name_num:str, name_name:str, name_res:str)-> None:
    with (open(name_num, 'r', encoding='utf-8') as f_num,
          open(name_name, 'r', encoding='utf-8') as f_name,
          open(name_res, 'w', encoding='utf-8') as f_res
          ):
        max_len = max(sum(1 for _ in f_num), sum(1 for _ in f_name))
        for _ in range(max_len):
            num = get_line(f_num)
            name = get_line(f_name)
            num_1, num_2 = num.split('|')
            mult = int(num_1) * float(num_2)
            if mult < 0:
                f_res.write(f'{name.lower()} {abs(mult)}\n')
            else:
                f_res.write(f'{name.upper()} {round(mult)}\n')


# def read_and_write_files(name_file_names: str,
#                         name_file_nambers: str,
#                         name_file_output: str) -> None:

#     with (open(name_file_names, 'r', encoding='utf-8') as file_names,
#             open(name_file_nambers, 'r', encoding='utf-8') as file_nambers):
#         names = file_names.read().split('\n')
#         nambers = file_nambers.read().split('\n')

#         if len(nambers) > len(names):
#             names += names[:len(nambers)-len(names)]
#         else:
#             nambers += nambers[:len(names)-len(nambers)]

#     with (open(name_file_output, 'w', encoding='utf-8') as file_output):
#         for name, namber in zip(names, nambers):
#             if not name or not namber:
#                 break
#             namber_output_int, namber_output_float = map(float, namber.split(' | '))
#             multik: float = namber_output_int * namber_output_float
#             if multik < 0:
#                 file_output.write(f"{name.lower()} {abs(multik)} \n")
#             else:
#                 file_output.write(f"{name.upper()} {int(multik)} \n")




if __name__ == '__main__':   
    print(num_name('task1.txt', 'task2.txt', 'task3.txt'))