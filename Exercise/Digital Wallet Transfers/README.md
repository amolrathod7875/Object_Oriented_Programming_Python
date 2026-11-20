# Digital Wallet Transfers

## Overview

Day 03 challenge: a digital wallet demonstrating **encapsulation**, **invariant preservation**, and **atomic transfers**. `Wallet` keeps its balance private and exposes it via a property. Deposits, withdrawals, and transfers are validated, and transaction history is returned as an immutable tuple so external callers cannot mutate internal state.

## Tasks

- [x] Create `Wallet(owner_id, starting_balance)` with nonpublic balance.
- [x] Implement `deposit()`, `withdraw()` and `transfer_to(other_wallet, amount)`.
- [x] Keep immutable-style transaction records; reject invalid and insufficient-funds transfers.

## Pass Checks

- [x] Wallet A ₹1,000 transfers ₹300 to B ₹200: balances become ₹700 and ₹500.
- [x] An attempted transfer of ₹5,000 leaves both wallets unchanged.
- [x] External changes to retrieved history do not mutate internal history.

## Code

```python
class wallet:
    def __init__(self, owner_id, starting_balance=0):
        if type(starting_balance) is not int:
            raise ValueError("Balance must be integer")
        if starting_balance < 0:
            raise ValueError("Balance must be Positive")
        self.owner_id = owner_id
        self.__balance = starting_balance
        self.__history = []

    @property
    def balance(self):
        return self.__balance

    @property
    def history(self):
        return tuple(self.__history)

    def deposite(self, amount):
        if type(amount) is not int:
            raise ValueError("Amount Must be integer")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount
        self.__history.append(("Deposite", amount))
        return self.balance

    def withdraw(self, amount):
        if type(amount) is not int:
            raise ValueError("Amount must be integer")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount
        self.__history.append(("Withdraw", amount))
        return self.balance

    def transfer_to(self, other_wallet, amount):
        if not isinstance(other_wallet, wallet):
            raise ValueError("Invalid Wallet")
        if self is other_wallet:
            raise ValueError("Cannot transfer to the same wallet")
        if type(amount) is not int:
            raise ValueError("Amount must be an integer")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient Balance")
        self.__balance -= amount
        other_wallet.__balance += amount
        self.__history.append(("transfer out", other_wallet.owner_id, amount))
        other_wallet.__history.append(("transfer in", self.owner_id, amount))
        return self.balance
```

## How the Code Satisfies the Tasks

- **Encapsulation**: balance stored as `self.__balance` (private); exposed via `balance` property.
- **History immutability**: `history` returns `tuple(self.__history)`, a new immutable snapshot; reassigning an element raises `TypeError`.
- **Validation**: deposit/withdraw/transfer reject non-int and non-positive amounts; withdraw/transfer reject insufficient funds.
- **Atomic transfer**: all validation happens before any mutation; on failure no balance or history changes.
- **Same-wallet guard**: prevents transferring to itself.

## Sample Behavior

```python
walletA = wallet("A", 1000)
walletB = wallet("B", 200)

walletA.transfer_to(walletB, 300)
assert walletA.balance == 700
assert walletB.balance == 500

# insufficient funds leaves state unchanged
try:
    walletA.transfer_to(walletB, 5000)
except ValueError:
    pass
assert walletA.balance == 700 and walletB.balance == 500
```

## Running the example

```bash
cd "Exercise/Digital Wallet Transfers"
python code.py
```

Expected output:

```
Test 1 Passed: Successful transfer
Test 2 Passed: Invalid transfer rejected
Test 3 Passed: Immutable history
```

## Interview Questions

1. **What does atomicity mean in this in-memory model?**
   Either the entire transfer (debit source, credit destination, record both histories) succeeds, or nothing changes. All validation occurs before any mutation, so a failed transfer leaves both wallets untouched.

2. **How is the balance kept private?**
   It is stored as `self.__balance`, which triggers name mangling to `_wallet__balance`, preventing direct external access. It is exposed read-only through the `balance` property.

3. **Why return a tuple instead of a list for history?**
   Tuples are immutable, so callers cannot append, remove, or reassign elements. Returning `tuple(self.__history)` also creates a new snapshot, so the internal list is never exposed.

4. **Why validate before mutating in `transfer_to`?**
   To preserve invariants and atomicity. If validation fails after partial mutation, balances and histories would be inconsistent. Validating first guarantees all-or-nothing behavior.

5. **What is the risk of mutating `other_wallet` directly via name mangling?**
   It relies on both objects being instances of the same class. If `other_wallet` were a subclass with overridden storage, direct access could bypass its invariants. A cleaner design would use public methods on the other wallet.
