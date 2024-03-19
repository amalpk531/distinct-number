##------------------------------bank account balance-------------------------
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount:.2f}. Current balance: ₹{self.balance:.2f}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount:.2f}. Current balance: ₹{self.balance:.2f}.")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Account Balance: ₹{self.balance:.2f}.")

# Creating an instance of BankAccount
my_account = BankAccount("123456", 1000)

# Taking user input for deposit amount
deposit_amount = float(input("Enter the deposit amount in rupees: "))
my_account.deposit(deposit_amount)

# Taking user input for withdrawal amount
withdrawal_amount = float(input("Enter the withdrawal amount in rupees: "))
my_account.withdraw(withdrawal_amount)

# Checking balance
my_account.check_balance()
