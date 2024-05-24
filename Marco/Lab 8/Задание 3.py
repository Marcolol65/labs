class Vector:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.start = (x1, y1, z1)
        self.end = (x2, y2, z2)

    def sum_and_sub_vectors(self, other):
        x11 = self.end[0] - self.start[0]
        x12 = other.end[0] - other.start[0]
        y11 = self.end[1] - self.start[1]
        y12 = other.end[1] - other.start[1]
        z11 = self.end[2] - self.start[2]
        z12 = other.end[2] - other.start[2]
        x = x11 + x12
        y = y11 + y12
        z = z11 + z12
        x_ = x12 - x11
        y_ = y12 - y11
        z_ = z12 - z11
        return Vector(self.start[0], self.start[1], self.start[2], x, y, z), Vector(self.start[0], self.start[1],
                                                                                    self.start[2], x_, y_, z_), (
                           x ** 2 + y ** 2 + z ** 2) ** 0.5

    def umno(self, other):
        x = (self.end[0] - self.start[0]) * (other.end[0] - other.start[0])
        y = (self.end[1] - self.start[1]) * (other.end[1] - other.start[1])
        z = (self.end[2] - self.start[2]) * (other.end[2] - other.start[2])
        return x + y + z

    def calculate_length(self):
        return ((self.end[0] - self.start[0]) ** 2 + (self.end[1] - self.start[1]) ** 2 + (
                    self.end[2] - self.start[2]) ** 2) ** 0.5

    def calculate_cosine(self, other):
        multiply = self.umno(other)
        length_product = self.calculate_length() * other.calculate_length()
        return multiply / length_product


v1 = Vector(1, 1, 1, 3, 3, 3)
v2 = Vector(2, 2, 2, 5, 5, 5)

sum_result, sub, lena = v1.sum_and_sub_vectors(v2)
umn = v1.umno(v2)
cosine_result = v1.calculate_cosine(v2)

print("Сумма векторов: ", sum_result.end)
print("Вычитание векторов: ", sub.end)
print("Скалярное произведение: ", umn)
print("Длина вектора: ", lena)
print("Косинус угла между векторами: ", cosine_result)
