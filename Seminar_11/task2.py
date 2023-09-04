"""
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков архивов
list-архивы также являются свойствами экземпляра
Добавьте к задачам 1 и 2 строки документации для классов.
"""


class Archiv:
    '''Сохраняем данные каждого экземпляра класса в
       списки old_text и old_int.'''
    instance = None

    def __new__(cls, *args, **kwargs):
        '''Переопределили метод new для сохранения аргументов в списки.'''
        if cls.instance:
            cls.instance.old_text.append(cls.instance.text)
            cls.instance.old_int.append(cls.instance.number)
        else:
            cls.instance = super().__new__(cls)
            cls.instance.old_text = []
            cls.instance.old_int = []
        return cls.instance

    def __init__(self, text: str, number: int) -> None:
        '''Определили метод инициализации экземпляра класса.'''
        self.text = text
        self.number = number

    def __str__(self):
        '''Переопределенный дандер метод строчного выведения
          экземпляра класса'''
        return f'Текст: {self.text}, Значение: {self.number}'

    def __repr__(self):
        '''Переопределенный дандер метод строчного выведения
          создания экземпляра класса'''
        return f'Archiv({self.text}, {self.number})'


if __name__ == "__main__":
    a1 = Archiv(text='T', number=1)
    a2 = Archiv(text='E', number=2)
    a3 = Archiv(text='Z', number=3)

print(a2.instance.old_text)
print(a2.instance.old_int)

print('---')

print(a3)
print(a3.text)
print(a3.number)
