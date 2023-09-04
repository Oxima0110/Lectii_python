"""
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
Добавьте к задачам 1 и 2 строки документации для классов.
"""
import time


class MyStr(str):
    '''Расширяемый класс str.'''
    def __new__(cls, value: str, name: str):
        '''Расширяеи метод new параметрами value и name.'''
        instance = super().__new__(cls, value)
        instance.name = name
        instance.value = value
        instance.time_create = time.time()
        return instance

    def __str__(self):
        '''Переопределенный дандер метод строчного выведения
           экземпляра класса'''
        return f'MyStr: {self.value = } {self.name = } {self.time_create = }'

    def __repr__(self):
        '''Переопределенный дандер метод строчного выведения
          создания экземпляра класса'''
        return f'MyStr({self.value}, {self.name})'


if __name__ == "__main__":
    res = MyStr('Получилось', 'Оксана')
    print(res)
