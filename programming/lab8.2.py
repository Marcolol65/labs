class Polynomial:
    def __init__(self, degree, coefficients):
        if degree != len(coefficients) - 1:
            raise ValueError("Degree should match the length of coefficients array minus one.")
        self.degree = degree
        self.coefficients = coefficients

    def evaluate(self, x):
        value = 0
        for i in range(self.degree + 1):
            value += self.coefficients[i] * (x ** i)
        return value

    def __add__(self, other):
        if self.degree >= other.degree:
            result_degree = self.degree
            result_coefficients = self.coefficients.copy()
            for i in range(other.degree + 1):
                result_coefficients[i] += other.coefficients[i]
        else:
            result_degree = other.degree
            result_coefficients = other.coefficients.copy()
            for i in range(self.degree + 1):
                result_coefficients[i] += self.coefficients[i]
        return Polynomial(result_degree, result_coefficients)

    def __sub__(self, other):
        if self.degree >= other.degree:
            result_degree = self.degree
            result_coefficients = self.coefficients.copy()
            for i in range(other.degree + 1):
                result_coefficients[i] -= other.coefficients[i]
        else:
            result_degree = other.degree
            result_coefficients = [-coeff for coeff in other.coefficients]
            for i in range(self.degree + 1):
                result_coefficients[i] += self.coefficients[i]
        return Polynomial(result_degree, result_coefficients)

    def __mul__(self, other):
        result_degree = self.degree + other.degree
        result_coefficients = [0] * (result_degree + 1)
        for i in range(self.degree + 1):
            for j in range(other.degree + 1):
                result_coefficients[i + j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(result_degree, result_coefficients)

    def display(self):
        polynomial_str = ""
        for i in range(self.degree + 1):
            if self.coefficients[i] != 0:
                if i == 0:
                    polynomial_str += str(self.coefficients[i])
                else:
                    polynomial_str += f"{self.coefficients[i]}x^{i}"
                if i != self.degree:
                    polynomial_str += " + "
        print("Polynomial:", polynomial_str)