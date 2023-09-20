"""
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""
from my_errors import NameError, AgeError


class Person:

    def __init__(self, surname, name, patronymic, age):
        if not isinstance(surname, str):
            raise NameError(surname)
        else:
            self.surname = surname
        if not isinstance(name, str):
            raise NameError(name)
        else:
            self.name = name
        if not isinstance(patronymic, str):
            raise NameError(patronymic)
        else:
            self.patronymic = patronymic
        if not isinstance(age, (int, float)) or age < 0:
            raise AgeError(age)
        else:
            self.__age = age

    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age += 1

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'


if __name__ == '__main__':
    p1 = Person("Ivanov", 'Ivan', 'Ivanovich', 25)
    print(p1.get_age())
    p1.birthday()
    print(p1)
    print(p1.get_age())
