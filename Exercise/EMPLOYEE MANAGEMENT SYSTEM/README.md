# Employee Management System

## Overview

This exercise demonstrates **inheritance** and **polymorphism** in Python through an `Employee` base class and two subclasses, `Developer` and `Manager`. Each subclass extends the base salary with an additional component (bonus / allowance) and overrides `calculate_salary()` to include it. A mixed list of employees is processed uniformly, showcasing runtime polymorphism.

## Tasks

- [x] Create an `Employee` base class with `name`, `employee_id`, and `base_salary`.
- [x] Validate that `base_salary` is non-negative (raise `ValueError` otherwise).
- [x] Implement `calculate_salary()` in `Employee` returning `base_salary`.
- [x] Create a `Developer` subclass that adds a `bonus` (default `0`).
- [x] Create a `Manager` subclass that adds an `allowance` (default `0`).
- [x] Override `calculate_salary()` in each subclass using `super()`.
- [x] Validate `bonus` and `allowance` are non-negative.
- [x] Demonstrate polymorphism by iterating over a mixed list of employees.

## Sample Behavior

```python
emp = Employee("Amol", 101, 125)
dev = Developer("Ram", 102, 758, 30)
mgr = Manager("Sita", 103, 741, 36)

for e in [emp, dev, mgr]:
    print(e.name, e.calculate_salary())
# Amol 125
# Ram 788
# Sita 777
```

## Code

```python
class Employee:
    def __init__(self, name, employee_id, base_salary):
        if base_salary < 0:
            raise ValueError("Salary cannot be Negative")
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

class Developer(Employee):
    def __init__(self, name, employee_id, base_salary, bonus=0):
        super().__init__(name, employee_id, base_salary)
        if bonus < 0:
            raise ValueError("Bonus Cannot be Negative")
        self.bonus = bonus

    def calculate_salary(self):
        return super().calculate_salary() + self.bonus

class Manager(Employee):
    def __init__(self, name, employee_id, base_salary, allowance=0):
        if allowance < 0:
            raise ValueError("Allowance cannot be Negative")
        super().__init__(name, employee_id, base_salary)
        self.allowance = allowance

    def calculate_salary(self):
        return super().calculate_salary() + self.allowance
```

## How the Code Satisfies the Tasks

- **Base class**: `Employee` stores `name`, `employee_id`, `base_salary` and validates the salary.
- **Base salary calculation**: `calculate_salary()` returns `base_salary`.
- **Developer subclass**: Extends `Employee`, adds `bonus`, validates it, and overrides `calculate_salary()` to add `bonus` via `super()`.
- **Manager subclass**: Extends `Employee`, adds `allowance`, validates it, and overrides `calculate_salary()` to add `allowance` via `super()`.
- **Code reuse**: `super().__init__()` and `super().calculate_salary()` reuse parent logic.
- **Polymorphism**: Iterating over `[emp, dev, mgr]` and calling `calculate_salary()` invokes the correct overridden method per actual type.

## Pass Checks

- [x] `Employee` salary equals `base_salary`.
- [x] `Developer` salary equals `base_salary + bonus`.
- [x] `Manager` salary equals `base_salary + allowance`.
- [x] Negative `base_salary`, `bonus`, or `allowance` raises `ValueError`.
- [x] Mixed list iteration produces type-specific salaries.

## Running the example

```bash
cd "Exercise/EMPLOYEE MANAGEMENT SYSTEM"
python code.py
```

Expected output:

```
Amol
101
125
Ram
102
788
Sita
103
777
```
