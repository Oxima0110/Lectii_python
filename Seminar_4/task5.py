# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.


def dict_awards(name:list[str], money:list[int|float], bonus:list[str])->dict[str:float]:
    awards = [round(float(i.replace('%', ''))/100, 4) for i in bonus]
    dict_bonus = {i:j*k for i, j, k in zip(name, money, awards)}
    return dict_bonus


list_name = ['Иван', 'Олег', 'Василий', 'Петр']
list_money = [125000, 110000, 118000, 130000]
list_bonus = ['10.22%', '12.3%', '8.5%', '9.85%']
print(dict_awards(list_name, list_money, list_bonus))
