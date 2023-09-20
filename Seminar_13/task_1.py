# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

import math
from my_errors import RadiusError


class Circle:
    _pi = math.pi

    def __init__(self, radius) -> None:
        if radius > 0:
            self.radius = radius
        else:
            raise RadiusError(radius)

    def calc_len(self):
        return self._pi * self.radius * 2

    def calc_area(self):
        return self._pi * self. radius ** 2


if __name__ == '__main__':
    c1 = Circle(0)
