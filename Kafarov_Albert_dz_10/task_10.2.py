from abc import abstractmethod, ABC


class Clothes(ABC):

    def __str__(self):
        return f'На {self.name} нужно {self.tissue_consumption:.2f} ткани'

    def __add__(self, other):
        return round(self.tissue_consumption + other.tissue_consumption, 2)

    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, name, v):
        self.name = name
        self.v = v

    @property
    def tissue_consumption(self):
        return self.v/6.5 + 0.5


class Costume(Clothes):

    def __init__(self, name, h):
        self.name = name
        self.h = h

    @property
    def tissue_consumption(self):
        return 2*self.h + 0.3


coat = Coat('Пальто', 8)
costume = Costume('Костюм', 178)


print(coat)
print(costume)
print(coat + costume)
