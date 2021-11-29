

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = '\n\n'.join(['\t'.join([f'{el}' for el in row])
                              for row in self.matrix])
        return f'{result}\n\n'

    def __add__(self, other):
        a = [map(sum, zip(*i)) for i in zip(self.matrix, other.matrix)]
        return self.__class__(a)


matrix_1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_2 = [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]

mx_1 = Matrix(matrix_1)
mx_2 = Matrix(matrix_2)

print(mx_1)
print(mx_2)

print(mx_1 + mx_2)
