"""
Задача 2. Доработаем задания 5-6. Создайте класс-фабрику.
- Класс принимает тип животного
(название одного из созданных классов) и параметры для
этого типа.
- Внутри класса создайте экземпляр на основе переданного
типа и верните его из класса-фабрики.
"""

from animals import (Dog, Fish, Kotopes)


class Fabrica:
    def get_animal(self, name_animal: str, *args):
        match name_animal:
            case 'Dog':
                return Dog(*args)
            case 'Fish':
                return Fish(*args)
            case 'Kotopes':
                return Kotopes(args)
        return f'Нет такого животного: {name_animal}'


"""
Возьмите 1-3 любые задания из прошлых семинаров
(например сериализация данных), которые вы уже решали.
Превратите функции в методы класса, а параметры в
свойства. Задания должны решаться через вызов
методов экземпляра.
Задача: работа с портфелем акций
"""

RENTA = 100
_initial_value = dict()


class Briefcase:
    def __init__(self,
                 stocks: dict,
                 price_initial: dict,
                 price_current: dict) -> None:
        self.stocks = stocks
        self.price_initial = price_initial
        self.price_current = price_current

    def calculate_portfolio_value_initial(self) -> float:
        """
        Расчет общей начальной стоимости портфеля акций
        """
        if len(_initial_value) == 0:
            for i, j in self.price_initial.items():
                _initial_value[i] = j
        sum = 0
        for key_stok, value_stock in self.stocks.items():
            sum += value_stock * self.price_initial[key_stok]
        return sum

    def calculate_portfolio_value_current(self) -> float:
        """
        Расчет общей текущей стоимости портфеля акций
        """
        if len(_initial_value) == 0:
            for i, j in self.price_current.items():
                _initial_value[i] = j
        sum = 0
        for key_stok, value_stock in self.stocks.items():
            sum += value_stock * self.price_current[key_stok]
        return sum

    def calculate_portfolio_return(self) -> float:
        """
        Расчет доходности портфеля
        """
        value_initial = self.calculate_portfolio_value_initial()
        value_current = self.calculate_portfolio_value_current()
        res = round((value_current - value_initial)/value_initial*100, 2)
        return res

    def get_most_profitable_stock(self) -> str:
        """
        Определение наиболее прибыльной акции
        """
        res = list(self.stocks.keys())[0]
        max = self.price_current[list(self.stocks.keys())[0]] - _initial_value[list(self.stocks.keys())[0]]
        for key, value in self.price_current.items():
            if value - _initial_value[key] > max:
                res, max = key, value - _initial_value[key]
        return res


if __name__ == '__main__':
    animal = Fabrica()
    dog = animal.get_animal('Dog', 'Полкан', 2, 'черный', 'такса', True)
    print(dog)
    animal2 = Fabrica()
    dog2 = animal.get_animal('Hors', 'Буран', 8, 'черный', 'конь')
    print(dog2)

    res = Briefcase({"AAPL": 10, "GOOGL": 5, "MSFT": 8},
                    {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50},
                    {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50})
    print(res.calculate_portfolio_value_initial())
    print(res.calculate_portfolio_value_current())
    print(res.calculate_portfolio_return())
    print(res.get_most_profitable_stock())
