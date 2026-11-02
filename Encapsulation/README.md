# Encapsulation in Python

## Overview

Encapsulation is one of the four fundamental principles of Object-Oriented Programming (OOP). It refers to the bundling of data (attributes) and the methods that operate on that data into a single unit (class), while restricting direct access to some of the object's components. This is achieved by making attributes private (using a double underscore prefix `__`) so they cannot be accessed or modified directly from outside the class. Instead, access is provided through well-defined public methods such as getters, setters, and other business logic methods.

## What's in this file

`Encapsulation.py` demonstrates encapsulation using a `BankAccount` class:

- A **private attribute** `__balance` stores the account balance, initialized in the constructor.
- `deposit(amount)` increases the balance only when the amount is positive.
- `withdraw(amount)` decreases the balance only when the amount is positive and does not exceed the current balance.
- `get_balance()` is a **getter** that returns the current balance without exposing the internal attribute directly.

### Code

```python
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

if __name__ == "__main__":
    acc = BankAccount(5000)
    acc.deposit(1000)
    print(acc.get_balance())  # 6000
    # print(acc.__balance)    # Raises AttributeError
```

### Running the example

```bash
python Encapsulation.py
```

Expected output:

```
6000
```

## Key Concepts

- **Private attributes** are declared with a double underscore prefix (`__balance`), triggering Python's name mangling to prevent direct external access.
- **Public methods** (`deposit`, `withdraw`, `get_balance`) act as the controlled interface to the internal state.
- Attempting to access `acc.__balance` directly raises an `AttributeError`, enforcing encapsulation.

## Interview Questions

1. **What is encapsulation in Python, and how is it implemented?**
   Encapsulation is the practice of hiding the internal state of an object and exposing it only through a controlled interface. In Python, it is implemented using private attributes (prefixed with `__`) and public methods that provide controlled access to those attributes.

2. **What is the difference between a single underscore (`_`) and a double underscore (`__`) prefix on an attribute?**
   A single underscore is a convention indicating that an attribute is "protected" or internal, but it is not enforced by Python. A double underscore triggers name mangling, making the attribute much harder to access from outside the class, effectively making it private.

3. **What is name mangling in Python?**
   Name mangling is a mechanism where Python internally renames attributes defined with a double underscore prefix (e.g., `__balance`) to `_ClassName__balance` to prevent accidental access or overriding in subclasses. For example, `BankAccount.__balance` becomes `_BankAccount__balance`.

4. **Why use getter and setter methods instead of accessing attributes directly?**
   Getters and setters allow validation, computation, or side effects to be applied when reading or modifying state. They provide a stable interface, so internal implementation can change without breaking external code, and they help enforce invariants (e.g., preventing negative balances).

5. **Can a private attribute in Python truly be made inaccessible?**
   No. Because Python relies on name mangling rather than strict access modifiers, a private attribute can still be accessed via its mangled name (e.g., `acc._BankAccount__balance`). Encapsulation in Python is largely a convention and a mechanism to avoid accidental misuse rather than absolute security.
