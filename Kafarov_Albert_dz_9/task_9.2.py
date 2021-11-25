

class Road:

    def __init__(self, lenght, width, _mass_of_asphalt=25, _depth=5):
        self.lenght = lenght
        self.width = width
        self._mass_of_asphalt = _mass_of_asphalt
        self._depth = _depth

    def calculate_mass(self):
        mass = self.lenght * self.width * self._mass_of_asphalt * self. _depth
        print(
            f'Масса асфальта, необходимого для покрытия всей дороги - {mass/1000} тонн')


x = Road(5000, 20)
x.calculate_mass()
