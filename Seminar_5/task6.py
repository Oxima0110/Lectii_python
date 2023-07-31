# ✔ Выведите в консоль таблицу умножения 
# от 2х2 до 9х10 как на школьной тетрадке. 
# ✔ Таблицу создайте в виде однострочного 
# генератора, где каждый элемент генератора — 
# отдельный пример таблицы умножения. 
# ✔ Для вывода результата используйте «принт» 
# без перехода на новую строку

# for i in range(2, 11):
#     for j in range(2, 6):
#         print(j, 'x', i, '=', i*j, end = '\t')
#     print()
# print()
# for i in range(2, 11):
#     for j in range(6, 10):
#         print(j, 'x', i, '=', i*j, end = '\t')
#     print()

# colums = 5
# rows = 2

# for i in range(rows):
#     for j in range(2, 11):
#         line = ''
#         for k in range(colums):
#             table_num = k*rows + i + 2
#             if table_num > 9:
#                 break
#             line += f'{table_num} x {j} = {table_num*j}\t'
#         print(line)
#     print()


LOWER_LIMIT = 2
UPPER_lIMIT = 10
COLUMN = 4

# def mult_table():
#     print(' ', end='')
#     print(*(f'{k:>} x {j:>2} = {k * j:>2}' if j == UPPER_lIMIT and k == i + COLUMN - 1 else \
#                 f'{k:>} x {j:>2} = {k * j:>2}\n' if k == i + COLUMN - 1 else \
#                     f'{k:>} x {j:>2} = {k * j:>2}\t' \
#             for i in range(LOWER_LIMIT, UPPER_lIMIT, COLUMN)
#             for j in range(LOWER_LIMIT, UPPER_lIMIT + 1)
#             for k in range(i, i + COLUMN)))

def mult_table():
    print(*(f'{k} x {j} = {k * j}\n' if j == UPPER_lIMIT and k == i + COLUMN - 1 else \
                f'{k} x {j} = {k * j}\n' if k == i + COLUMN - 1 else \
                    f'{k} x {j} = {k * j}\t' \
            for i in range(LOWER_LIMIT, UPPER_lIMIT, COLUMN)
            for j in range(LOWER_LIMIT, UPPER_lIMIT + 1)
            for k in range(i, i + COLUMN)))
mult_table()



