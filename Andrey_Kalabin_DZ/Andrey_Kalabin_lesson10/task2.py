from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def calculate(self) -> float:
        pass


class Coat(Clothes):

    def __init__(self, size: float or int):
        self._size = size

    @property
    def calculate(self):
        return f'Для пошива пальто необходимо {self._size / 6.5 + 0.5 : .2f} ткани'


class Costume(Clothes):

    def __init__(self, height: float or int):
        self._height = height

    @property
    def calculate(self):
        return f'Для пошива костюма необходимо {2 * self._height + 0.3 : .2f} ткани'


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)

    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3