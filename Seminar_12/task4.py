"""
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств.
"""


class Rectangle:
    def __init__(self, length_cm: float, width_cm: float = None) -> None:
        self.__length = length_cm
        if width_cm:
            self.__width = width_cm
        else:
            self.__width = length_cm

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value < 0:
            raise ValueError("не может быть меньше нуля")
        self.__length = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("не может быть меньше нуля")
        self.__width = value


if __name__ == '__main__':
    r1 = Rectangle(length_cm=2, width_cm=3)
    print(r1.length)
    print(r1.width)
    r1.length = 4
    print(r1.length)
    print(r1.width)
    r1.length = -1
    print(r1.length)
    print(r1.width)
