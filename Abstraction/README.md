# Abstraction in Python

## Overview

Abstraction is one of the four fundamental principles of Object-Oriented Programming (OOP). It focuses on hiding complex implementation details and exposing only the essential features of an object through a simplified interface. In Python, abstraction is commonly achieved using the `abc` (Abstract Base Classes) module, where abstract classes define a contract (abstract methods) that subclasses must implement.

## What's in this file

`Abstraction.py` demonstrates abstraction using a `PaymentGateway` abstract base class and two concrete implementations:

- `PaymentGateway(ABC)` declares an abstract method `process_payment(amount)` that has no implementation.
- `CreditCardPayment` and `PPPayment` (PayPal-like) inherit from `PaymentGateway` and provide their own implementations of `process_payment`.
- You cannot instantiate `PaymentGateway` directly; only concrete subclasses can be created.

### Code

```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processed credit card payment of {amount} INR")

class PPPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processed PP Payment of {amount} INR")

credit_card = CreditCardPayment()
pp = PPPayment()

print("Payment started ...")
credit_card.process_payment(100)

print("\nPayment started ...")
pp.process_payment(50)
```

### Running the example

```bash
python Abstraction.py
```

Expected output:

```
Payment started ...
Processed credit card payment of 100 INR

Payment started ...
Processed PP Payment of 50 INR
```

## Key Concepts

- **Abstract class**: A class that cannot be instantiated and may contain abstract methods.
- **Abstract method**: A method declared but not implemented in the base class; subclasses must override it.
- **`ABC` and `@abstractmethod`**: Provided by Python's `abc` module to enforce the abstraction contract.
- **Interface enforcement**: Any subclass that fails to implement all abstract methods cannot be instantiated.

## Interview Questions

1. **What is abstraction in Python?**
   Abstraction is the process of hiding complex implementation details and exposing only the necessary functionality through a simplified interface, allowing users to interact with objects without knowing their internal workings.

2. **How is abstraction implemented in Python?**
   Python implements abstraction using the `abc` module. An abstract base class (inheriting from `ABC`) can define abstract methods (decorated with `@abstractmethod`) that subclasses must implement before they can be instantiated.

3. **What is the difference between an abstract class and an interface?**
   Python has no formal `interface` keyword. An abstract class can contain both abstract and concrete methods plus state, while an interface (often simulated with a pure abstract class) defines only method signatures. Abstract classes support partial implementation; interfaces define a pure contract.

4. **Can you instantiate an abstract class in Python?**
   No. Attempting to instantiate an abstract class that has unimplemented abstract methods raises a `TypeError`. Only fully implemented concrete subclasses can be instantiated.

5. **What happens if a subclass does not implement all abstract methods?**
   The subclass itself becomes abstract and cannot be instantiated. Python raises a `TypeError` listing the unimplemented abstract methods if you try to create an instance.
