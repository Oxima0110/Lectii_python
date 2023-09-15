"""
Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.
"""
"""
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.

"""

import json


class MyFac:
    def __init__(self, size: int):
        self._size = size
        self.__archiv: list = []

    def show_archiv(self):
        return self.__archiv

    def __call__(self, namber: int):
        res: int = 1
        for i in range(1, namber+1):
            res *= i

        if len(self.__archiv) >= self._size:
            self.__archiv.pop(0)
        self.__archiv.append({namber: res})
        return res

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(r'factorial.json', 'w', encoding='utf-8') as f:
            json.dump(self.__archiv, f)


if __name__ == '__main__':
    f1 = MyFac(size=4)
    # print(f1(1))
    # print(f1(2))
    # print(f1(3))
    # print(f1(4))
    # print(f1(5))
    # print(f1(6))
    # print(f1(7))
    # print(f1.show_archiv())
    with f1 as copy_:
        print(copy_(3))
        print(copy_(4))
        print(copy_(5))
        print(copy_(6))
        print(copy_(7))
        print(copy_(8))
