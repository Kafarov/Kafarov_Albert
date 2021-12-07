class ComplexNumber:

    def __init__(self, a, b):
        self.comp_num = complex(a, b)

    def __add__(self, other):
        return self.comp_num + other.comp_num

    def __mul__(self, other):
        return self.comp_num * other.comp_num


c_num_1 = ComplexNumber(1, 2)
c_num_2 = ComplexNumber(3, 4)

x = c_num_1 + c_num_2
y = c_num_2 * c_num_1
print(x)
print(y)
