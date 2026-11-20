class wallet :
    def __init__(self, owner_id, starting_balance=0):
        if type(starting_balance) is not int :
            raise ValueError("Balance must be integer")
        if starting_balance < 0 :
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
        if type(amount) is not int :
            raise ValueError("Amount Must be integer")
        if amount <= 0 :
            raise ValueError("Amount must be positive")
        else:
            self.__balance += amount
            self.__history.append(("Deposite", amount))
        return self.balance
    
    def withdraw(self, amount):
        if type(amount) is not int :
            raise ValueError("Amount must be interger")
        if amount <= 0 :
            raise ValueError("Amount must be Positive ")
        elif amount > self.__balance :
            raise ValueError("Insufficient balance")
        else:
            self.__balance -= amount
            self.__history.append(("Withdraw", amount))
        return self.balance
    
    def transfer_to(self, other_wallet, amount):
        if not isinstance(other_wallet, wallet):
            raise ValueError("Invalid Wallet")
        if self is other_wallet:
            raise ValueError("Cannot transfer to the same wallet")
        if type(amount) is not  int:
            raise ValueError("Amount must be an integer")
        if amount <= 0 :
            raise ValueError("Amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient Balance")
        self.__balance -= amount
        other_wallet.__balance += amount

        self.__history.append(
            ("transfer out", other_wallet.owner_id, amount)
        )
        other_wallet.__history.append(
            ("transfer in", self.owner_id, amount)
        )
        return self.balance
    




walletA = wallet("A", 1000)
walletB = wallet("B", 200)

# Test 1: Successful transfer
walletA.transfer_to(walletB, 300)

assert walletA.balance == 700
assert walletB.balance == 500

print("Test 1 Passed: Successful transfer")

# Test 2: Insufficient funds
try:
    walletA.transfer_to(walletB, 5000)
except ValueError:
    pass

assert walletA.balance == 700
assert walletB.balance == 500
assert len(walletA.history) == 1
assert len(walletB.history) == 1

print("Test 2 Passed: Invalid transfer rejected")

# Test 3: History protection
history = walletA.history

try:
    history[0] = ("fake", 5000)
except TypeError:
    pass

assert walletA.history[0] == ("transfer out", "B", 300)

print("Test 3 Passed: Immutable history")
