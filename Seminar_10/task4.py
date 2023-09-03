"""
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь

"""

from random import randint
from task3 import Person


def sum_didgit(a: int):
    a = str(a)
    sum_a = 0
    for i in a:
        sum_a += int(i)
    return sum_a % 7


class Employ(Person):
    def __init__(self, surname, name, patronymic, age):
        super().__init__(surname, name, patronymic, age)
        self.id = randint(100000, 999999)
        self.level = sum_didgit(self.id)


if __name__ == '__main__':
    p1 = Employ("Ivanov", 'Ivan', 'Ivanovich', 25)
    print(p1)
    print(p1.get_age())
    print(p1.id, p1.level)
