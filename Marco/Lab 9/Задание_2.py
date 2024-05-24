class Matrix:
    def __init__(self, matrix):
        self.matrix = [row[:] for row in matrix]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, i)) for i in self.matrix])

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    def __add__(self, other):
        if self.size() != other.size():
            print("Разного размера( всппомни правило сложения!!!")
            return None
        answer = []
        for i in range(len(self.matrix)):
            stolb = []
            for j in range(len(self.matrix[0])):
                stolb.append(self.matrix[i][j] + other.matrix[i][j])
            answer.append(stolb)
        return Matrix(answer)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.size()[1] != other.size()[0]:
                print("Нельзя умножать, почитай правило!!!")
                return None
            answer = []
            for i in range(len(self.matrix)):
                stolb = []
                for j in range(len(other.matrix[0])):
                    k = 0
                    for f in range(len(other.matrix)):
                        k += self.matrix[i][f] * other.matrix[f][j]
                    stolb.append(k)
                answer.append(stolb)
            return Matrix(answer)
        elif type(other) == int or type(other) == float:
            answer = []
            for i in range(len(self.matrix)):
                stolb = []
                for j in range(len(self.matrix[0])):
                    stolb.append(self.matrix[i][j] * other)
                answer.append(stolb)
            return Matrix(answer)

    __rmul__ = __mul__

    @staticmethod
    def transposed(matrix):
        trans = [[matrix.matrix[j][i] for j in range(len(matrix.matrix))] for i in range(len(matrix.matrix[0]))]
        return Matrix(trans)


m1 = Matrix([[1, 1, 9], [0, 5, 1]])
m2 = Matrix([[3, 17, 9], [10, 5, 3], [4, 2, 6]])
print("Матрица 1:")
print(m1)
print("Матрица 2:")
print(m2)
print("Сумма наших матриц:")
print(m1 + m2)
print("Умножение матриц:")
print(m1 * m2)
print("Умножение матрицы на число:")
print(m2 * 7)
print("Умножение матрицы на число:")
print(17 * m1)
print("транспортированная матрица:")
print(Matrix.transposed(m2))
