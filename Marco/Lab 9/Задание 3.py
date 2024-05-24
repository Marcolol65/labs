from Задание_2 import Matrix


class Vector(Matrix):
    def __init__(self, vector):
        super().__init__([[elem] for elem in vector])

    def umno(self, other):
        if self.size() == other.size() == (3, 1):
            x1, x2, x3 = self.matrix[0][0], self.matrix[1][0], self.matrix[2][0]
            y1, y2, y3 = other.matrix[0][0], other.matrix[1][0], other.matrix[2][0]
            x_1 = x2 * y3 - x3 * y2
            y_1 = x3 * y1 - x1 * y3
            z_1 = x1 * y2 - x2 * y1
            return Vector([x_1, y_1, z_1])
        else:
            print("Мы работаем только до трёх!!!")
            return None


v1 = Vector([17, 9, 13])
v2 = Vector([5, 7, 1])
print("Вектор 1:")
print(v1)
print("Вектор 2:")
print(v2)
print("Сумма векторов:")
print(v1 + v2)
print("Умножение векторов:")
print(v1 * v2)
print("Произведение на число:")
print(v2 * 7)
print("Произведение на число:")
print(17 * v1)
print("Векторное произведение:")
print(v1.umno(v2))
