"""
Задание. Создайте класс студента.
- Используя дескрипторы проверяйте ФИО на первую заглавную
букву и наличие только букв.
- Названия предметов должны загружаться из файла CSV
при создании экземпляра. Другие предметы в экземпляре
недопустимы.
- Для каждого предмета можно хранить оценки (от 2 до 5)
и результаты тестов (от 0 до 100).
- Также экземпляр должен сообщать средний балл по тестам
для каждого предмета и по оценкам всех предметов вместе взятых.
"""
import csv
from statistics import mean


class Name:
    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._param_name, value)

    def validate(self, value):
        if not isinstance(value, str):
            raise AttributeError('Имя должно быть строкой')
        if not value.isalpha():
            raise AttributeError('Имя должно состоять из букв')
        if not value.istitle():
            raise AttributeError('Имя должно начинаться с заглавной буквы')


class Student:
    _first_name = Name()
    _last_name = Name()

    def __new__(cls, *args, **kwargs):
        cls.instance = super().__new__(cls)
        cls.instance.grades = {}
        cls.instance.tests = {}
        with open('items.csv', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cls.instance.grades[row['items']] = []
                cls.instance.tests[row['items']] = []
        return cls.instance

    def __init__(self, first_name, last_name) -> None:
        self._first_name = first_name
        self._last_name = last_name

    def __str__(self):
        avg_test_res = '\n'.join(f'{k}: {v}' for k, v
                                 in self.avg_tests().items())
        return f'Студент: {self._first_name} {self._last_name}\n' \
               f'Средняя оценка по всем предметам: {self.avg_grades()}\n' \
               f'Средние оценки по тестам: \n{avg_test_res}'

    def validate_items(self, item):
        if item not in self.instance.grades:
            raise ValueError('Нет такого предмета')

    def validate_num(self, value, min_num, max_num):
        if not min_num <= value <= max_num:
            raise ValueError('Нет такой оценки')
        if not isinstance(value, int):
            raise TypeError('Значение должно быть целым числом')

    def grade(self, item, value):
        min_grade = 2
        max_grade = 5
        self.validate_items(item)
        self.validate_num(value, min_grade, max_grade)
        data = self.instance.grades[item]
        data.append(value)
        self.instance.grades[item] = data

    def test(self, item, value):
        min_grade = 0
        max_grade = 100
        self.validate_items(item)
        self.validate_num(value, min_grade, max_grade)
        data = self.instance.tests[item]
        data.append(value)
        self.instance.tests[item] = data

    def avg_grades(self):
        res = 0
        count = 0
        for items in self.instance.grades.values():
            if len(items) > 0:
                res += mean(items)
                count += 1
        return res/count

    def avg_tests(self):
        avg_res = dict()
        for key, value in self.instance.tests.items():
            if len(value) > 0:
                avg_res[key] = round(mean(value), 2)
            else:
                avg_res[key] = 0
        return avg_res


if __name__ == "__main__":
    s = Student('Иванов', 'Петя')
    s.grade('Химия', 5)
    s.grade('Химия', 2)
    s.grade('История', 3)
    s.test('Математика', 10)
    s.test('Математика', 30)
    s.test('История', 50)
    print(s)
