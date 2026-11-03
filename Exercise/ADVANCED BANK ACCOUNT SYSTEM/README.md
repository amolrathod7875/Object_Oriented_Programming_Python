# Advanced Bank Account System

## Overview

This exercise demonstrates **encapsulation** in Python through a `BankAccount` class. The balance and transaction history are kept private, and all interactions happen through well-defined public methods that validate input and raise `ValueError` on invalid operations.

## Tasks

- [x] Create `BankAccount` with an initial balance.
- [x] Keep the balance non-public using `__balance`.
- [x] Implement `deposit(amount)`, `withdraw(amount)`, and `get_balance()`.
- [x] Reject zero/negative deposits and withdrawals.
- [x] Reject withdrawals greater than the available balance.
- [x] Maintain a private transaction history.
- [x] Expose `get_transactions()` without allowing callers to change the internal history list (returns a copy).
- [x] Raise `ValueError` for invalid amounts / insufficient balance.

## Sample Behavior

```python
acc = BankAccount(5000)
acc.deposit(2000)
acc.withdraw(1500)
print(acc.get_balance())
# 5500
```

## Code

```python
class BankAccount:

    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.__balance = balance
        self.__transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")
        self.__balance += amount
        self.__transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero")
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount
        self.__transactions.append(f"Withdrawn: {amount}")

    def get_balance(self):
        return self.__balance

    def get_transactions(self):
        return list(self.__transactions)
```

## How the Code Satisfies the Tasks

- **Initial balance**: `__init__` accepts `balance` and validates it is non-negative; raises `ValueError` otherwise.
- **Private balance**: Stored as `self.__balance` (name-mangled), inaccessible directly from outside.
- **Deposit/Withdraw/Get balance**: Public methods `deposit`, `withdraw`, `get_balance` provide the controlled interface.
- **Reject zero/negative**: Both `deposit` and `withdraw` check `amount <= 0` and raise `ValueError`.
- **Reject over-withdrawal**: `withdraw` compares `amount > self.__balance` and raises `ValueError("Insufficient balance")`.
- **Private history**: Transactions stored in `self.__transactions` (private list).
- **Safe exposure**: `get_transactions()` returns `list(self.__transactions)` — a new list, so callers cannot mutate internal history.
- **ValueError on invalid**: All invalid inputs and insufficient-balance cases raise `ValueError`.

## Pass Checks

- [x] Starting 5000; deposit 2000; withdraw 1500 => balance 5500.
- [x] `deposit(-100)`, `withdraw(0)`, `withdraw(99999)` are rejected with `ValueError`.
- [x] A failed transaction does not change the balance or history (validation happens before any state mutation).
- [x] Editing `get_transactions()` output does not change internal history (a copy is returned).

## Running the example

```bash
cd "Exercise/ADVANCED BANK ACCOUNT SYSTEM"
python code.py
```

Expected output:

```
5500
```
