"""
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""
from my_errors import RectangleError


class Rectangle:
    def __init__(self, length: float, width: float = None) -> None:
        if not isinstance(length, (int, float)) or length < 0:
            raise RectangleError(length)
        else:
            self.length = length
        if width:
            if not isinstance(width, (int, float)) or width < 0:
                raise RectangleError(width)
            else:
                self.width = width
        else:
            self.width = length

    def calc_len(self):
        return (self.width + self.length) * 2

    def calc_area(self):
        return self.width * self.length


if __name__ == '__main__':
    r1 = Rectangle(length=2, width=2)
    print(f'{r1.calc_len() = }')
    print(f'{r1.calc_area() = }')

    print('---')

    r2 = Rectangle(length=3)
    print(f'{r2.calc_len() = }')
    print(f'{r2.calc_area() = }')