

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print(f'Запуск отрисовки, выбран инструмент: {self.title}')


class Pencil(Stationery):

    def draw(self):
        print(f'Запуск отрисовки, выбран инструмент: {self.title}')


class Handle(Stationery):

    def draw(self):
        print(f'Запуск отрисовки, выбран инструмент: {self.title}')


stationary = Stationery('None')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
stationary.draw()
pen.draw()
pencil.draw()
handle.draw()
