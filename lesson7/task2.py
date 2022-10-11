from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calc_fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size > 68:
            self.__size = 68
        elif size < 38:
            self.__size = 38
        else:
            self.__size = size

    def calc_fabric_consumption(self):
        return round(self.__size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height > 210:
            self.__height = 210
        elif height < 140:
            self.__height = 140
        else:
            self.__height = height

    def calc_fabric_consumption(self):
        return round(self.height / 100 * 2 + 0.3, 2)


some_coat = Coat(int(input('Введите размер пальто: ')))
print(f'Расход ткани на пальто {some_coat.size} размера составляет: {some_coat.calc_fabric_consumption()}м.')
some_suit = Suit(int(input('Введите размер пальто в см: ')))
print(f'Расход ткани на костюм для человека ростом {some_suit.height}м составляет: '
      f'{some_suit.calc_fabric_consumption()}м.')
print(f'Общий расход ткани составляет: '
      f'{round(some_coat.calc_fabric_consumption() + some_suit.calc_fabric_consumption(), 2)}м.')
