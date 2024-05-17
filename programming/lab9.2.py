class Matrix:
    def __init__(self, matrix):
        self.matrix = [row[:] for row in matrix]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other):
        if self.size() != other.size():
            raise ValueError("Matrix dimensions must be the same for addition.")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.size()[1])] for i in
                  range(self.size()[0])]
        return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.size()[1] != other.size()[0]:
                raise ValueError(
                    "Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication.")
            result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.size()[1])) for j in
                       range(other.size()[1])] for i in range(self.size()[0])]
        else:
            result = [[element * other for element in row] for row in self.matrix]
        return Matrix(result)

    __rmul__ = __mul__

    @staticmethod
    def transposed(matrix):
        transposed_matrix = [[matrix.matrix[j][i] for j in range(matrix.size()[0])] for i in range(matrix.size()[1])]
        return Matrix(transposed_matrix)


# Пример использования:
matrix1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix2 = Matrix([[7, 8], [9, 10], [11, 12]])

print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)

print("Size of matrix 1:", matrix1.size())
print("Size of matrix 2:", matrix2.size())

try:
    print("Sum of matrices:")
    print(matrix1 + matrix2)
except ValueError as e:
    print(e)

try:
    print("Product of matrices:")
    print(matrix1 * matrix2)
except ValueError as e:
    print(e)

scalar = 2
print("Scalar multiplication:")
print(matrix1 * scalar)

print("Transposed matrix 1:")
print(Matrix.transposed(matrix1))