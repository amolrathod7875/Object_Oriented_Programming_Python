class BankAccount:

    def __init__(self, balance):

        if balance < 0 :
            raise ValueError("Initial balance cannot be negative")

        self.__balance = balance
        self.__transactions = []

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise ValueError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")
        self.__balance += amount
        self.__transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise ValueError("Amount must be a number")
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


if __name__ == "__main__":
    acc = BankAccount(5000)
    acc.deposit(2000)
    acc.withdraw(1500)
    print(acc.get_balance())
    # 5500
