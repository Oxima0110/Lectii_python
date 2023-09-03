"""
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
"""


class Animal:
    def __init__(self,
                 name: str,
                 age: int) -> None:
        self.name = name.capitalize()
        self.age = age

    def __str__(self) -> str:
        return f'{self.name} {self.age}'

    def birthday(self):
        self.age += 1


class Dog(Animal):
    def __init__(self,
                 name: str,
                 age: int,
                 color: str,
                 breed: str,
                 is_domestic: bool = True) -> None:
        super().__init__(name, age)

        self.color = color
        self.breed = breed
        self.is_domestic = is_domestic

    def __str__(self) -> str:
        if self.is_domestic:
            return f'Dog {self.color} {self.breed} домашняя'
        return f'Dog {self.color} {self.breed} дворняга'


class Kotopes(Animal):
    def __init__(self,
                 name: str,
                 age: int,
                 number_heads: int = 2) -> None:
        super().__init__(name, age)

        self.__number_heads = number_heads

    def __str__(self) -> str:
        return f'Kotopes -> number_heads: {self.__number_heads}'


class Fish(Animal):
    def __init__(self,
                 name: str,
                 age: int,
                 size: int,
                 aqua: bool = True) -> None:
        super().__init__(name, age)

        self.size = size
        self.aqua = aqua

    def __str__(self) -> str:
        if self.aqua:
            return f'Fish {self.name} морская Возраст: {self.age}'
        return f'Fish {self.name} пресноводная Возраст: {self.age}'


if __name__ == '__main__':
    kotopes = Kotopes(name='Miracle', age=11, number_heads=2)
    print(kotopes)
    dog = Dog('Бобик', 3, 'рыжий', 'спаниель', True)
    dog2 = Dog('Тузик', 3, 'серый', 'спаниель', False)
    print(dog)
    print(dog2)
    fish = Fish('окунь', 1, 15, True)
    print(fish)
    fish.birthday()
    print(fish)
