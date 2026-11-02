# Object_Oriented_Programming_Python

A collection of Python examples demonstrating the four fundamental principles of Object-Oriented Programming (OOP): Encapsulation, Inheritance, Polymorphism, and Abstraction.

## What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around **objects** rather than functions and logic. An object is an instance of a **class**, which acts as a blueprint defining attributes (data) and methods (behavior). OOP promotes modularity, reusability, scalability, and maintainability of code.

## The Four Pillars of OOP

### 1. Encapsulation
Bundling data and the methods that operate on it into a single unit (class), while restricting direct access to internal state. Achieved in Python using private attributes (`__name`) and public getter/setter methods. See `Encapsulation/`.

### 2. Inheritance
A mechanism where a new class (subclass) derives attributes and methods from an existing class (superclass), promoting code reuse and establishing "is-a" relationships. See `Inheritance/`.

### 3. Polymorphism
The ability of different objects to respond to the same method call in their own way, enabling a common interface across different types. Achieved through method overriding and duck typing. See `Polymorphism/`.

### 4. Abstraction
Hiding complex implementation details and exposing only essential features through a simplified interface. Implemented in Python using abstract base classes (`abc` module) and `@abstractmethod`. See `Abstraction/`.

## Project Structure

```
Object_Oriented_Programming_Python/
├── README.md
├── Encapsulation/
│   ├── Encapsulation.py
│   └── README.md
├── Inheritance/
│   ├── Interitance.py
│   └── README.md
├── Polymorphism/
│   ├── Polymorphism.py
│   └── README.md
└── Abstraction/
    ├── Abstraction.py
    └── README.md
```

## Running the examples

Each example is standalone. Run any file directly:

```bash
python Encapsulation/Encapsulation.py
python Inheritance/Interitance.py
python Polymorphism/Polymorphism.py
python Abstraction/Abstraction.py
```

## Core OOP Concepts in Python

- **Class**: A blueprint for creating objects (`class ClassName:`).
- **Object/Instance**: A concrete occurrence of a class created via the constructor.
- **`__init__`**: The initializer (constructor) called when an object is created.
- **`self`**: Reference to the current instance, used to access attributes and methods.
- **Attribute**: A variable bound to an object or class.
- **Method**: A function defined inside a class that operates on instances.
- **Inheritance**: `class Child(Parent):` to derive from a parent.
- **`super()`**: Proxy to access parent class methods.
- **Encapsulation**: Private attributes via `__name` (name mangling).
- **Abstraction**: Abstract base classes via `abc.ABC` and `@abstractmethod`.
- **Polymorphism**: Method overriding and duck typing.

## Why OOP?

- **Reusability**: Inheritance and composition reduce duplicated code.
- **Modularity**: Objects encapsulate related state and behavior.
- **Maintainability**: Changes are localized; interfaces remain stable.
- **Extensibility**: New types can be added without modifying existing code (open/closed principle).
- **Modeling real world**: Objects map naturally to real-world entities.

## Interview Questions (OOP in Python)

1. **What are the four pillars of OOP?**
   Encapsulation, Inheritance, Polymorphism, and Abstraction.

2. **What is the difference between a class and an object?**
   A class is a blueprint/template; an object is an instance created from that blueprint.

3. **What is `self` in Python?**
   `self` is the first parameter of instance methods, referring to the current object instance. It is passed automatically when calling a method on an instance.

4. **What is the difference between instance, class, and static methods?**
   Instance methods take `self` and operate on instance state. Class methods take `cls` (decorated with `@classmethod`) and operate on class state. Static methods (decorated with `@staticmethod`) take neither and behave like regular functions grouped within a class.

5. **What is the MRO (Method Resolution Order) in Python?**
   MRO is the order Python searches classes when resolving a method/attribute, computed via C3 linearization. Inspect with `ClassName.__mro__` or `ClassName.mro()`.
