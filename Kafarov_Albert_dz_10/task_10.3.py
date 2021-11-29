

class Cell:

    def __new__(cls, integer):
        try:
            if integer <= 0:
                print('Клетка не жизнеспособна')
                return None
            else:
                return super().__new__(cls)
        except AttributeError:
            AttributeError()

    def __init__(self, integer):
        self.integer = int(integer)
        print('Создана клетка', self.integer)

    def __add__(self, other):
        return self.integer + other.integer

    def __sub__(self, other):
        if self.integer > other.integer:
            return self.integer - other.integer
        else:
            return 0

    def __mul__(self, other):
        return self.integer * other.integer

    def __truediv__(self, other):
        return self.integer // other.integer

    def make_order(self, row):
        if self.integer % row == 0:
            return ('*' * row + '\n') * int(self.integer / row)
        else:
            return ('*' * row + '\n') * int(self.integer // row) + '*' * int(self.integer % row) + '\n'


cell_1 = Cell(10)
cell_2 = Cell(8)
cell_3 = Cell(13)

print(cell_1.make_order(5))
print(cell_2.make_order(3))
print(cell_3.make_order(5))

cell_4 = Cell(cell_1 + cell_3)
cell_5 = Cell(cell_3 / cell_1)
cell_6 = Cell(cell_2 - cell_2)
cell_7 = Cell(cell_1 * cell_3)
print(cell_4.make_order(5))
print(cell_5.make_order(5))
# print(cell_6.make_order(5))
print(cell_7.make_order(5))
