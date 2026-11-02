# Polymorphism in Python

## Overview

Polymorphism is one of the four fundamental principles of Object-Oriented Programming (OOP). It allows objects of different classes to be treated through a common interface, where the same method name behaves differently depending on the actual object's type. In Python, polymorphism is typically achieved through method overriding and duck typing, enabling flexible and extensible code.

## What's in this file

`Polymorphism.py` demonstrates polymorphism using a `Shape` base class with `Circle` and `Rectangle` subclasses:

- `Shape` defines a common method `calculate_area()` (a base implementation that does nothing).
- `Circle` overrides `calculate_area()` to compute `3.14 * radius * radius`.
- `Rectangle` overrides `calculate_area()` to compute `length * width`.
- A list of mixed `Shape` objects is iterated, calling `calculate_area()` on each; the correct version runs based on the actual object type.

### Code

```python
class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

shapes = [Circle(5), Rectangle(4, 5)]
for shape in shapes:
    print("Area : ", shape.calculate_area())
```

### Running the example

```bash
python Polymorphism.py
```

Expected output:

```
Area :  78.5
Area :  20
```

## Key Concepts

- **Method overriding**: Subclasses redefine a parent method to provide type-specific behavior.
- **Runtime polymorphism**: The method invoked is resolved at runtime based on the object's actual class.
- **Duck typing**: Python relies on the presence of methods/attributes rather than explicit type checks ("if it walks like a duck...").
- **Common interface**: Code can operate on a collection of different types uniformly.

## Interview Questions

1. **What is polymorphism in Python?**
   Polymorphism is the ability of different objects to respond to the same method call in their own way. The same interface (method name) produces different behavior depending on the object's actual type.

2. **How is polymorphism implemented in Python?**
   Primarily through method overriding in subclasses and duck typing. Python does not require interfaces or abstract base classes; it resolves methods at runtime based on the object's class.

3. **What is duck typing?**
   Duck typing means Python determines an object's suitability by the methods and attributes it has, not its explicit type. "If it looks like a duck and quacks like a duck, it's a duck." This enables polymorphism without inheritance.

4. **What is the difference between compile-time and runtime polymorphism?**
   Compile-time (static) polymorphism is resolved during compilation (e.g., method overloading in other languages). Runtime (dynamic) polymorphism is resolved at execution (e.g., method overriding). Python only supports runtime polymorphism since it is dynamically typed and does not support method overloading by signature.

5. **What is method overloading, and does Python support it?**
   Method overloading means defining multiple methods with the same name but different parameters. Python does not support it natively; a later definition overwrites earlier ones. Workarounds include default arguments, `*args`/`**kwargs`, or `functools.singledispatch`.
