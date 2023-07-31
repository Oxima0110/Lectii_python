# ✔ Продолжаем развивать задачу 2. 
# ✔ Возьмите словарь, который вы получили. 
# Сохраните его итераторатор. 
# ✔ Далее выведите первые 5 пар ключ-значение, 
# обращаясь к итератору, а не к словарю.

NUM = 5


def get_dict(data:str)->dict[str:int]:
    return {i:ord(i) for i in data.replace(' ', '')}


def get_iter(input_dict:dict):
     iter_dict = iter(input_dict.items())
     for i in range(NUM):
        print(*next(iter_dict))


data_str = 'Самостоятельно сохраните в переменной строку текста.'
res_dict = get_dict(data_str)
get_iter(res_dict)