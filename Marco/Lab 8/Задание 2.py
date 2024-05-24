class Pol:
    def __init__(self, degree, coefficients):
        self.degree = degree
        self.coefficients = coefficients

    def filip(self, x):
        result = 0
        for i in range(self.degree + 1):
            result += self.coefficients[i] * (x ** i)
        return result

    def add(self, other):
        new_degree = max(self.degree, other.degree)
        new_coefficients = [0] * (new_degree + 1)
        for i in range(self.degree + 1):
            new_coefficients[i] += self.coefficients[i]
        for i in range(other.degree + 1):
            new_coefficients[i] += other.coefficients[i]
        return Pol(new_degree, new_coefficients)

    def subtract(self, other):
        new_degree = max(self.degree, other.degree)
        new_coefficients = [0] * (new_degree + 1)
        for i in range(self.degree + 1):
            new_coefficients[i] += self.coefficients[i]
        for i in range(other.degree + 1):
            new_coefficients[i] -= other.coefficients[i]
        return Pol(new_degree, new_coefficients)

    def multiply(self, other):
        new_degree = self.degree + other.degree
        new_coefficients = [0] * (new_degree + 1)
        for i in range(self.degree + 1):
            for j in range(other.degree + 1):
                new_coefficients[i + j] += self.coefficients[i] * other.coefficients[j]
        return Pol(new_degree, new_coefficients)

    def show(self):
        print("Степень многочлена:", self.degree)
        print("Коэффициенты:", self.coefficients)


p1 = Pol(3, [1, 2, 7, 8])
p2 = Pol(2, [3, 4, 6])

print("Многочлен 1:")
p1.show()
print("Многочлен 2:")
p2.show()

result_add = p1.add(p2)
result_subtract = p1.subtract(p2)
result_multiply = p1.multiply(p2)
print("Результат сложения многочленов:")
result_add.show()

print("Результат вычитания многочленов:")
result_subtract.show()

print("Результат умножения многочленов:")
result_multiply.show()

x = 8
print(f"Значение многочлена 1 при x = {x}:", p1.filip(x))
print(f"Значение многочлена 2 при x = {x}:", p2.filip(x))
