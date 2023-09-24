class Rectangle:
    '''Класс прямоугольник, с методами расчета периметра и площади фигуры.'''
    def __init__(self, length: float, width: float = None) -> None:
        '''Метод инициализации прямоугольника со сторонами length и width.'''
        self.length = length
        if width:
            self.width = width
        else:
            self.width = length

    def calc_len(self):
        '''Метод расчета периметра прямоугольника.'''
        return (self.width + self.length) * 2

    def calc_area(self):
        '''Метод расчета площади прямоугольника.'''
        return self.width * self.length

    def __str__(self):
        '''Переопределенный дандер метод строчного выведения
          экземпляра класса'''
        return f'Прямоугольник {self.width} x {self.length}'

    def __repr__(self):
        '''Переопределенный дандер метод строчного выведения
          создания экземпляра класса'''
        return f'Rectangle({self.width}, {self.length})'

    def __add__(self, other):
        '''Переопределенный дандер метод сложения двух прямоугольников.'''
        return Rectangle(length=(self.length + other.length),
                         width=self.width)

    def __sub__(self, other):
        '''Переопределенный дандер метод вычетания двух прямоугольников.'''
        return Rectangle(length=abs(self.length - other.length),
                         width=self.width)

    def __eq__(self, other: "Rectangle"):
        '''Переопределенный дандер метод сравнения двух прямоугольников.'''
        return self.calc_area() == other.calc_area()

    def __lt__(self, other: "Rectangle"):
        '''Переопределенный дандер метод сравнения двух прямоугольников.'''
        return self.calc_area() < other.calc_area()

    def __gt__(self, other: "Rectangle"):
        '''Переопределенный дандер метод сравнения двух прямоугольников.'''
        return self.calc_area() > other.calc_area()

    def __ge__(self, other: "Rectangle"):
        '''Переопределенный дандер метод сравнения двух прямоугольников.'''
        return self.calc_area() >= other.calc_area()

    def __le__(self, other: "Rectangle"):
        '''Переопределенный дандер метод сравнения двух прямоугольников.'''
        return self.calc_area() <= other.calc_area()


if __name__ == '__main__':
    r1 = Rectangle(length=2, width=2)
    print(f'{r1.calc_len() = }')
    print(f'{r1.calc_area() = }')
    print('---')

    r2 = Rectangle(length=3)
    print(f'{r2.calc_len() = }')
    print(f'{r2.calc_area() = }')

    r3 = r2 + r1

    print('---')
    print(r3)
    print(f'{r3.calc_len() = }')
    print(f'{r3.calc_area() = }')

    print(r1 == r2)
    print(r1 <= r2)
    print(r1 >= r2)
