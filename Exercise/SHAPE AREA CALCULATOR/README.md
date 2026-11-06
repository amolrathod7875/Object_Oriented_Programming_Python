# Shape Area Calculator

## Overview

This exercise demonstrates **abstraction** and **polymorphism** in Python using an abstract `Shape` base class with `Circle`, `Rectangle`, and `Triangle` subclasses. Each shape implements its own area formula, and a mixed list of shapes is processed with a single shared `calculate_area()` call. Dimensions are validated to be greater than zero.

## Tasks

- [x] Define `Shape` as an Abstract Base Class (ABC).
- [x] Mark `calculate_area()` with `@abstractmethod`.
- [x] Implement `Circle(radius)`, `Rectangle(length, width)`, and `Triangle(base, height)`.
- [x] Calculate each area using its shape-specific formula.
- [x] Process a mixed list of shapes with one shared method call.
- [x] Validate that dimensions are greater than zero.
- [x] Use `math.pi` for a more accurate circle calculation.

## Pass Checks

- [x] `Shape()` cannot be instantiated directly (raises `TypeError`).
- [x] `Rectangle(4, 5)` => `20`.
- [x] `Triangle(4, 6)` => `12`.
- [x] `Circle(5)` => approximately `78.54`.
- [x] Invalid dimensions are rejected (raise `ValueError`).

## Code

```python
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
```

## How the Code Satisfies the Tasks

- **ABC**: `Shape` inherits from `ABC`, making it an abstract base class.
- **Abstract method**: `calculate_area()` is decorated with `@abstractmethod`, forcing subclasses to implement it.
- **Implementations**: `Rectangle`, `Circle`, and `Triangle` each implement `calculate_area()` with their own formula.
- **Shape-specific formulas**: Rectangle `length * width`; Circle `math.pi * radius ** 2`; Triangle `0.5 * base * height`.
- **Mixed list processing**: `shapes = [r, c, t]` iterated with one `shape.calculate_area()` call (polymorphism).
- **Validation**: Each constructor checks dimensions are `> 0`, raising `ValueError` otherwise.
- **math.pi**: Circle uses `math.pi` for accuracy.

## Sample Behavior

```python
r = Rectangle(4, 5)
c = Circle(5)
t = Triangle(4, 6)

for shape in [r, c, t]:
    print(f"{type(shape).__name__} Area: {shape.calculate_area():.2f}")
# Rectangle Area: 20.00
# Circle Area: 78.54
# Triangle Area: 12.00
```

## Running the example

```bash
cd "Exercise/SHAPE AREA CALCULATOR"
python code.py
```

Expected output:

```
Rectangle Area: 20.00
Circle Area: 78.54
Triangle Area: 12.00
Rectangle Error: Dimensions must be greater than zero
Circle Error: Radius must be greater than zero
Triangle Error: Dimensions must be greater than zero
Abstract Class Error: Can't instantiate abstract class Shape without an implementation for abstract method 'calculate_area'
```
