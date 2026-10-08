class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"Hey {self.name}, here is your ${self.balance}")

    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
            print(
                f"Here is your total amount after deposit: ${self.balance}, User: {self.name}"
            )
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print(
                f"Withdraw amount is {amount} and remaining is ${self.balance}, User: {self.name}"
            )

        else:
            print("Invalid withdrawal amount.")

    def check_balance(self):
        print(f"Here is your balance amount: ${self.balance}, User: {self.name}")


class SavingsAccount(BankAccount):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print(f"Annual interest: ${interest:.2f}")
        
    


# account1 = BankAccount("Aditya", 5000)
account2 = BankAccount("Rahul", 2000)
savings = SavingsAccount("Aditya",5000,5)

savings.deposit(1000)
savings.check_balance()
savings.calculate_interest()
savings.check_balance()
# account1.deposit(1000)

# account1.check_balance()
account2.check_balance()
