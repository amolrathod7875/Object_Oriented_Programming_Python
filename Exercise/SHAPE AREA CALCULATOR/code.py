from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()

        if length <= 0 or width <= 0:
            raise ValueError("Dimensions must be greater than zero")

        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()

        if radius <= 0:
            raise ValueError("Radius must be greater than zero")

        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()

        if base <= 0 or height <= 0:
            raise ValueError("Dimensions must be greater than zero")

        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


# Create objects
r = Rectangle(4, 5)
c = Circle(5)
t = Triangle(4, 6)


# Polymorphism: Mixed list of shapes
shapes = [r, c, t]

for shape in shapes:
    print(f"{type(shape).__name__} Area: {shape.calculate_area():.2f}")


# Validate invalid dimensions
try:
    r1 = Rectangle(-4, 5)
except ValueError as e:
    print("Rectangle Error:", e)

try:
    c1 = Circle(0)
except ValueError as e:
    print("Circle Error:", e)

try:
    t1 = Triangle(4, -6)
except ValueError as e:
    print("Triangle Error:", e)


# Verify abstract class cannot be instantiated
try:
    s = Shape()
except TypeError as e:
    print("Abstract Class Error:", e)