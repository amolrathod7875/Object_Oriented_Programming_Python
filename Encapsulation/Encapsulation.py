class BankAccount : 
    def __init__(self, initial_balance):
        self.__balance = initial_balance ## <- This is the Private Attribute with double underscore

    def deposit(self, amount):
        if amount > 0 :
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

if __name__ == "__main__":
    acc = BankAccount(5000)
    acc.deposit(1000)
    t1 = acc.get_balance()
    print(t1)

    #print(acc.__balance) # if we uncommit this it will Raise Attribute Error 
