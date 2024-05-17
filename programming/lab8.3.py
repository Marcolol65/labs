import math

class Vector3D:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.start_point = (x1, y1, z1)
        self.end_point = (x2, y2, z2)

    def __add__(self, other):
        x = self.end_point[0] + other.end_point[0] - self.start_point[0] - other.start_point[0]
        y = self.end_point[1] + other.end_point[1] - self.start_point[1] - other.start_point[1]
        z = self.end_point[2] + other.end_point[2] - self.start_point[2] - other.start_point[2]
        return Vector3D(0, 0, 0, x, y, z)

    def __sub__(self, other):
        x = self.end_point[0] - other.end_point[0] - self.start_point[0] + other.start_point[0]
        y = self.end_point[1] - other.end_point[1] - self.start_point[1] + other.start_point[1]
        z = self.end_point[2] - other.end_point[2] - self.start_point[2] + other.start_point[2]
        return Vector3D(0, 0, 0, x, y, z)

    def dot_product(self, other):
        x1, y1, z1 = self.vector_components()
        x2, y2, z2 = other.vector_components()
        return x1 * x2 + y1 * y2 + z1 * z2

    def length(self):
        x, y, z = self.vector_components()
        return math.sqrt(x**2 + y**2 + z**2)

    def cosine_similarity(self, other):
        dot_product = self.dot_product(other)
        length_self = self.length()
        length_other = other.length()
        return dot_product / (length_self * length_other)

    def vector_components(self):
        x = self.end_point[0] - self.start_point[0]
        y = self.end_point[1] - self.start_point[1]
        z = self.end_point[2] - self.start_point[2]
        return x, y, z

# Пример использования:
vec1 = Vector3D(1, 2, 3, 4, 5, 6)
vec2 = Vector3D(7, 8, 9, 10, 11, 12)

print("Сумма векторов:", (vec1 + vec2).vector_components())
print("Разность векторов:", (vec1 - vec2).vector_components())
print("Скалярное произведение векторов:", vec1.dot_product(vec2))
print("Длина вектора 1:", vec1.length())
print("Длина вектора 2:", vec2.length())
print("Косинус угла между векторами:", vec1.cosine_similarity(vec2))