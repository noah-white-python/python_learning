class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        print(f"deposited {amount}, balance is now {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("not enough money!")
        else:
            self.balance -= amount
            print(f"withdrew {amount}, balance is now {self.balance}")
    def check_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")

if __name__ == "__main__":
    name = input("enter your name: ")
    account = BankAccount(name)

    while True:
        print("\n1. deposit")
        print("2. withdraw")
        print("3. check balance")
        print("4. exit")

        choice = input("choose an option: ")

        if choice == "1":
            deposit_amount = float(input("how much to deposit: "))
            account.deposit(deposit_amount)
        elif choice == "2":
            withdraw_amount = float(input("how much to withdraw: "))
            account.withdraw(withdraw_amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("goodbye!")
            break
        else:
            print("invalid option!")