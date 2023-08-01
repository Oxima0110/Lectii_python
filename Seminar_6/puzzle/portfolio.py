
# Расчет общей стоимости портфеля акций:
# Функция calculate_portfolio_value
# (stocks: dict, prices: dict) -> float 
# принимает два аргумента:
# stocks - словарь, где ключами являются символы акций 
# (например, "AAPL" для Apple Inc.), 
# и значениями - количество акций каждого символа.
# prices - словарь, где ключами являются символы акций, 
# а значениями - текущая цена каждой акции.
# Функция должна вернуть общую стоимость портфеля акций на 
# основе количества акций и их текущих цен.

# Расчет доходности портфеля:
# Функция calculate_portfolio_return
# (initial_value: float, current_value: float) -> float 
# принимает два аргумента:
# initial_value - начальная стоимость портфеля акций.
# current_value - текущая стоимость портфеля акций.
# Функция должна вернуть процентную доходность портфеля.

# Определение наиболее прибыльной акции:
# Функция get_most_profitable_stock
# (stocks: dict, prices: dict) -> str принимает два аргумента:
# stocks - словарь с акциями и их количеством.
# prices - словарь с акциями и их текущими ценами.
# Функция должна вернуть символ акции (ключ), которая 
# имеет наибольшую прибыль по сравнению с ее начальной 
# стоимостью.Начальная стоимость - первый вызов calculate_portfolio_value, 
# данные из этого вызова следует сохранить в защищенную переменную на 
# уровне модуля.

# Тестирование модуля:
# Напишите небольшую программу, которая импортирует модуль 
# "portfolio.py" и демонстрирует использование всех трех 
# функций.
# Создайте словари для акций и цен, 
# запустите функции и выведите результаты.


__all__ = ['calculate_portfolio_value', 'calculate_portfolio_return', 'get_most_profitable_stock']

RENTA = 100
_initial_value = dict()



def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    if len(_initial_value) == 0:
        for i, j in prices.items():
            _initial_value[i] = j
    sum = 0
    for key_stok, value_stock in stocks.items():
        sum += value_stock * prices[key_stok]
    return sum


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    res = round((current_value - initial_value)/initial_value*100, 2)
    return res


def get_most_profitable_stock(stocks: dict, prices: dict)-> str:
    res = list(stocks.keys())[0]
    max = prices[list(stocks.keys())[0]] - _initial_value[list(stocks.keys())[0]]
    for key, value in prices.items():
        if value - _initial_value[key] > max:
            res, max = key, value - _initial_value[key]
    return res


if __name__ == '__main__':
    stock = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
    price_initial = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
    price_current =  {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
    sum_value_initial = calculate_portfolio_value(stock, price_initial)
    sum_value_current = calculate_portfolio_value(stock, price_current)
    print(sum_value_initial)
    print(sum_value_current)
    rentabilitate = calculate_portfolio_return(sum_value_initial, sum_value_current)
    print(rentabilitate)
    max_value = get_most_profitable_stock(stock, price_current)
    print(max_value)



    