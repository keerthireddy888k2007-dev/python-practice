class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def check_balance(self):
        print(f"Current balance: {self.balance:.2f}rs")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f}rs")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount:.2f}rs")


# Main program menu
name = input("Enter owner name: ")
account = BankAccount(name)

while True:
    print("\n1. Check Balance | 2. Deposit | 3. Withdraw | 4. Exit")
    choice = input("Select option (1-4): ")

    if choice == "1":
        account.check_balance()
    elif choice == "2":
        amt = float(input("Enter amount to deposit: "))
        account.deposit(amt)
    elif choice == "3":
        amt = float(input("Enter amount to withdraw: "))
        account.withdraw(amt)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")