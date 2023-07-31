# ✔ Три друга взяли вещи в поход. Сформируйте 
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного 
#   и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции 
# с множествами. Код должен расширяться 
# на любое большее количество друзей.

def total_list(name_dict:dict)->set:
    '''
    получение общего списка вещей
    '''
    total_set = set()
    for value in item_dict.values():
        total_set = total_set.union(value)
    return total_set

def common_dict(name_dict:dict)->dict:
    '''
    получение словаря с количеством взятых вещей
    '''
    total_dict = {}
    total_set = total_list(name_dict)
    for element in total_set:
        total_dict[element] = 0
    for value in name_dict.values():
        for key in total_dict.keys():
            if key in value:
                total_dict[key] = total_dict[key] + 1
    return total_dict

def common_list(name_dict:dict):
    '''
    получение вещей которые взяли все три друга
    '''
    common_set = total_list(name_dict)
    for value in name_dict.values():
        common_set = common_set & value
    print(f'Вещи которые взяли все три друга: {common_set}')

def unic_list(name_dict:dict):
    '''
    список уникальных вещей
    '''
    unic_list = []
    total_dict = common_dict(name_dict)
    for key, value in total_dict.items():
        if value == 1:
            unic_list.append(key)
    print(f'Список уникальных вещей: {unic_list}')

def one_list(name_dict:dict):
    '''
    Вещи которые есть у всех кроме одного
    '''
    total_dict = common_dict(name_dict)
    one_dict = {}
    for key, volume in total_dict.items():
        if volume == len(name_dict) - 1:
            for name, element in name_dict.items():
                if key not in element:
                    if name not in one_dict.keys():
                        one_dict[name] = [key]
                    else:
                        one_dict[name] = one_dict[name].append(key)
    for key, value in one_dict.items():
        print(f'{key} не взял {value}')    


friend_list = ['Вася', 'Коля', 'Миша']
item_dict = {'Вася':{'рюкзак', 'палатка', 'котелок', 'фонарик'}, 
             'Коля':{'рюкзак', 'палатка', 'фонарик', 'спички'}, 
             'Миша':{'рюкзак', 'палатка', 'спички', 'велосипед'}}

common_list(item_dict)
unic_list(item_dict)
one_list(item_dict)


# for i in dict_friends.keys():
#     dict_friends[i] = frozenset(dict_friends[i])
# list_names = list(dict_friends.keys())

# all_set = set(dict_friends[list_names[0]])
# for i in range(1, len(list_names)):
#     all_set = all_set & dict_friends[list_names[i]]
# print(f"1. Вещи, которые есть у каждого из друзей: {list(all_set)}\n")


# Преобразуем кортежи вещей в множества для удобства работы
# friends_sets = {name: set(items) for name, items in friends_dict.items()}

# # Вещи, которые взяли все три друга
# all_items = set.intersection(*friends_sets.values())

# # Вещи, которые уникальны для каждого друга
# unique_items = {name: items - set.union(*(s for n, s in friends_sets.items() if n != name)) 
#                 for name, items in friends_sets.items()}

# # Вещи, которые есть у всех друзей, кроме одного
# one_missing_items = {name: (set.union(*(s for n, s in friends_sets.items() if n != name)) - items) 
#                      for name, items in friends_sets.items()}

# print(f'Все други: {all_items},\n Уникальные вещи: {unique_items}, \n Взял один: {one_missing_items}')