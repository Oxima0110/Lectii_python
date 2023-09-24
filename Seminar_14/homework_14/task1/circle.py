# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

import math


class MyException(Exception):
    pass


class RadiusError(MyException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Значение радиуса должно быть положительное.'\
               f'Вы вводите: {self.value}'


class Circle:
    '''Класс круг, с методами расчета длины окружности
      и ее площади.'''
    _pi = math.pi

    def __init__(self, radius) -> None:
        '''Метод инициализации круга с радиусом radius
        >>> print(Circle(5))
        Круг с радиусом 5

        >>> print(Circle(10))
        Круг с радиусом 10

        >>> print(Circle(0))
        Traceback (most recent call last):
        ...
        RadiusError: Значение радиуса должно быть положительное.Вы вводите: 0
        '''
        if radius > 0:
            self.radius = radius
        else:
            raise RadiusError(radius)

    def calc_len(self):
        '''
        Метод расчета длины окружности
        >>> print(Circle(5).calc_len())
        31.41592653589793

        >>> print(Circle(10).calc_len())
        62.83185307179586
        '''
        return self._pi * self.radius * 2

    def calc_area(self):
        '''
        Метод расчета площади круга
        >>> print(Circle(5).calc_area())
        78.53981633974483

        >>> print(Circle(10).calc_area())
        314.1592653589793
        '''
        return self._pi * self. radius ** 2

    def __eq__(self, other: "Circle"):
        '''Переопределенный дандер метод сравнения двух
        кругов.
        >>> print(Circle(5) == Circle(10))
        False

        >>> print(Circle(5) == Circle(5))
        True
          '''
        return self.calc_area() == other.calc_area()

    def __str__(self):
        '''Переопределенный дандер метод строчного выведения
          экземпляра класса'''
        return f'Круг с радиусом {self.radius}'


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
