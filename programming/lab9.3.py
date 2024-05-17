class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def transpose(self):
        return [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]

class Vector(Matrix):
    def __init__(self, vector):
        super().__init__(vector)

    def dot_product(self, other):
        if len(self.matrix) != len(other.matrix):
            raise ValueError("Vectors must have the same length for dot product.")
        return sum(x * y for x, y in zip(self.matrix, other.matrix))

    def cross_product(self, other):
        if len(self.matrix) != 3 or len(other.matrix) != 3:
            raise ValueError("Cross product is defined only for 3-dimensional vectors.")
        x = self.matrix[1] * other.matrix[2] - self.matrix[2] * other.matrix[1]
        y = self.matrix[2] * other.matrix[0] - self.matrix[0] * other.matrix[2]
        z = self.matrix[0] * other.matrix[1] - self.matrix[1] * other.matrix[0]
        return Vector([x, y, z])

# Пример использования:
vector1 = Vector([1, 2, 3])
vector2 = Vector([4, 5, 6])

print("Dot product:", vector1.dot_product(vector2))
print("Cross product:", vector1.cross_product(vector2).matrix)