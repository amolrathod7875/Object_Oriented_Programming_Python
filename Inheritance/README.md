# Inheritance in Python

## Overview

Inheritance is one of the four fundamental principles of Object-Oriented Programming (OOP). It allows a new class (child/subclass) to acquire the attributes and methods of an existing class (parent/superclass), promoting code reuse and establishing an "is-a" relationship between classes. The child class can extend or override the inherited behavior to add new functionality.

## What's in this file

`Interitance.py` demonstrates inheritance using a `Vehicle` base class and a `Car` subclass:

- `Vehicle` defines a common attribute `color` and a method `start()`.
- `Car(Vehicle)` inherits from `Vehicle`, adding its own attribute `num_doors` and method `drive()`.
- `super().__init__(color)` calls the parent constructor to initialize the inherited `color` attribute.
- An instance `my_car = Car("Blue", 4)` can call both inherited (`start`) and its own (`drive`) methods.

### Code

```python
class Vehicle:
    def __init__(self, color):
        self.color = color

    def start(self):
        print("Vehicle is Starting ....")

class Car(Vehicle):
    def __init__(self, color, num_doors):
        super().__init__(color)
        self.num_doors = num_doors

    def drive(self):
        print(f"Car with{self.num_doors} doors is driving ...")

my_car = Car("Blue", 4)
my_car.start()
my_car.drive()
```

### Running the example

```bash
python Interitance.py
```

Expected output:

```
Vehicle is Starting ....
Car with4 doors is driving ...
```

## Key Concepts

- **Single inheritance**: `Car` inherits from a single parent class `Vehicle`.
- **`super()`**: Used to invoke the parent class's `__init__` (or other methods) without hardcoding the parent name.
- **Method overriding**: A subclass can redefine a parent method to provide specialized behavior.
- **Code reuse**: Common functionality lives in the base class and is shared by all subclasses.

## Interview Questions

1. **What is inheritance in Python, and what problem does it solve?**
   Inheritance lets a subclass reuse the attributes and methods of a parent class, reducing code duplication and modeling "is-a" relationships (e.g., a Car is a Vehicle).

2. **What is the difference between single and multiple inheritance?**
   Single inheritance means a class derives from one parent. Multiple inheritance means a class derives from more than one parent. Python supports both; multiple inheritance uses the Method Resolution Order (MRO) to resolve which method is called.

3. **What does `super()` do in Python?**
   `super()` returns a proxy object that delegates method calls to the parent class. It is commonly used in `__init__` to call the parent constructor, and it supports cooperative multiple inheritance by following the MRO.

4. **What is Method Resolution Order (MRO)?**
   MRO is the order in which Python looks up methods and attributes across a class hierarchy. It is computed using the C3 linearization algorithm. You can inspect it with `ClassName.__mro__` or `ClassName.mro()`.

5. **How can a subclass override a parent method, and how can it still call the parent's version?**
   A subclass simply redefines the method with the same name. To invoke the parent's version, it calls `super().method_name()` (or `ParentClass.method_name(self)`), allowing extension rather than full replacement of behavior.
