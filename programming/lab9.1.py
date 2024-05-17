import matplotlib.pyplot as plt

class GeometricFigure:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def calculate_perimeter(self):
        pass

    def calculate_area(self):
        pass

    def paint(self):
        pass

class Triangle(GeometricFigure):
    def __init__(self, coordinates):
        super().__init__(coordinates)

    def calculate_perimeter(self):
        # Предполагаем, что координаты представлены в формате (x, y)
        side1 = ((self.coordinates[0][0] - self.coordinates[1][0])**2 + (self.coordinates[0][1] - self.coordinates[1][1])**2)**0.5
        side2 = ((self.coordinates[1][0] - self.coordinates[2][0])**2 + (self.coordinates[1][1] - self.coordinates[2][1])**2)**0.5
        side3 = ((self.coordinates[2][0] - self.coordinates[0][0])**2 + (self.coordinates[2][1] - self.coordinates[0][1])**2)**0.5
        return side1 + side2 + side3

    def calculate_area(self):
        # Предполагаем, что координаты представлены в формате (x, y)
        return 0.5 * abs((self.coordinates[0][0] - self.coordinates[2][0]) * (self.coordinates[1][1] - self.coordinates[2][1]) - (self.coordinates[1][0] - self.coordinates[2][0]) * (self.coordinates[0][1] - self.coordinates[2][1]))

    def paint(self):
        x = [point[0] for point in self.coordinates + [self.coordinates[0]]]
        y = [point[1] for point in self.coordinates + [self.coordinates[0]]]
        plt.plot(x, y, 'b-')
        plt.fill(x, y, color='lightblue', alpha=0.5)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Triangle')
        plt.grid(True)
        plt.show()

class Rectangle(GeometricFigure):
    def __init__(self, coordinates):
        super().__init__(coordinates)

    def calculate_perimeter(self):
        width = abs(self.coordinates[0][0] - self.coordinates[1][0])
        height = abs(self.coordinates[0][1] - self.coordinates[1][1])
        return 2 * (width + height)

    def calculate_area(self):
        width = abs(self.coordinates[0][0] - self.coordinates[1][0])
        height = abs(self.coordinates[0][1] - self.coordinates[1][1])
        return width * height

    def paint(self):
        width = abs(self.coordinates[0][0] - self.coordinates[1][0])
        height = abs(self.coordinates[0][1] - self.coordinates[1][1])
        x = [self.coordinates[0][0], self.coordinates[0][0] + width, self.coordinates[0][0] + width, self.coordinates[0][0], self.coordinates[0][0]]
        y = [self.coordinates[0][1], self.coordinates[0][1], self.coordinates[0][1] + height, self.coordinates[0][1] + height, self.coordinates[0][1]]
        plt.plot(x, y, 'b-')
        plt.fill(x, y, color='lightblue', alpha=0.5)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Rectangle')
        plt.grid(True)
        plt.show()

class Circle(GeometricFigure):
    def __init__(self, coordinates, radius):
        super().__init__(coordinates)
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * 3.14159 * self.radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2

    def paint(self):
        circle = plt.Circle((self.coordinates[0], self.coordinates[1]), self.radius, color='lightblue')
        fig, ax = plt.subplots()
        ax.add_artist(circle)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Circle')
        plt.grid(True)
        plt.axis('equal')
        plt.show()

# Пример использования:
triangle = Triangle([(1, 1), (4, 1), (2.5, 4)])
rectangle = Rectangle([(1, 1), (5, 4)])
circle = Circle((2, 2), 3)

print("Triangle Perimeter:", triangle.calculate_perimeter())
print("Triangle Area:", triangle.calculate_area())
triangle.paint()

print("Rectangle Perimeter:", rectangle.calculate_perimeter())
print("Rectangle Area:", rectangle.calculate_area())
rectangle.paint()

print("Circle Perimeter:", circle.calculate_perimeter())
print("Circle Area:", circle.calculate_area())
circle.paint()