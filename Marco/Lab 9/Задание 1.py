import matplotlib.pyplot as plt
import numpy as np


class Geo_Fig:
    def __init__(self, points):
        self.points = points
        self.P = None
        self.S = None


class Tri(Geo_Fig):
    def __init__(self, points):
        super().__init__(points)
        a = np.linalg.norm(self.points[1] - self.points[0])
        b = np.linalg.norm(self.points[2] - self.points[1])
        c = np.linalg.norm(self.points[0] - self.points[2])

        p = (a + b + c) / 2
        self.S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        self.P = a + b + c

    def paint(self):
        plt.plot([self.points[0][0], self.points[1][0], self.points[2][0], self.points[0][0]],
                 [self.points[0][1], self.points[1][1], self.points[2][1], self.points[0][1]])
        plt.title('Треугольник')
        plt.show()


triangle = Tri(np.array([[5, 7], [10, 3], [3, 3]]))
print("Периметр треугольника:", round(triangle.P, 5))
print("Площадь треугольника:", round(triangle.S, 5))
triangle.paint()


class Rect(Geo_Fig):
    def __init__(self, points):
        super().__init__(points)
        a = np.linalg.norm(self.points[1] - self.points[0])
        b = np.linalg.norm(self.points[2] - self.points[1])
        self.P = 2 * a + 2 * b
        self.S = a * b

    def paint(self):
        x = [self.points[0][0], self.points[1][0], self.points[2][0], self.points[3][0], self.points[0][0]]
        y = [self.points[0][1], self.points[1][1], self.points[2][1], self.points[3][1], self.points[0][1]]
        plt.plot(x, y)
        plt.title('Прямоугольник')
        plt.show()


rectangle = Rect(np.array([[0, 0], [3, 0], [3, 3], [0, 3]]))
print("Периметр прямоугольника:", rectangle.P)
print("Площадь прямоугольника:", rectangle.S)
rectangle.paint()


class Circle(Geo_Fig):
    def __init__(self, points, radius):
        super().__init__(points)
        self.radius = radius
        self.P = 2 * np.pi * self.radius
        self.S = np.pi * self.radius ** 2

    def paint(self):
        fig, ax = plt.subplots()
        circle = plt.Circle((self.points[0], self.points[1]), self.radius, fill=False)
        ax.set_aspect(1)
        ax.add_artist(circle)
        ax.set_xlim(self.points[0] - self.radius, self.points[0] + self.radius)
        ax.set_ylim(self.points[1] - self.radius, self.points[1] + self.radius)
        plt.title('Круг')
        plt.show()


circle = Circle(np.array([1, 5]), 3)
print("Периметр круга:", round(circle.P, 3))
print("Площадь круга:", round(circle.S, 3))
circle.paint()
