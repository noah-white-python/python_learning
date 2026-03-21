from day7_practice import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, owner, interest_rate):
        super().__init__(owner)          # 继承父类
        self.interest_rate = interest_rate

    def apply_interest(self, time):
        interest = self.balance * self.interest_rate * time
        self.balance += interest
        print(f"after {time} years, interest earned: {interest:.2f}")
        print(f"final balance: {self.balance:.2f}")


# 主程序

name = input("enter your name: ")
time = int(input("how long you want to save (years): "))

print("\nchoose interest rate plan:")
print("1. 1 year  - interest rate 1.1%")
print("2. 3 years - interest rate 1.5%")
print("3. 5 years - interest rate 1.6%")
print("4. exit")

choice = int(input("choose an option: "))

if choice == 1:
    account = SavingsAccount(name, 0.011)  # 注意：1.1% = 0.011
elif choice == 2:
    account = SavingsAccount(name, 0.015)
elif choice == 3:
    account = SavingsAccount(name, 0.016)
elif choice == 4:
    print("goodbye!")
else:
    print("error")

# 存钱
deposit_amount = float(input("how much to deposit: "))
account.deposit(deposit_amount)

# 计算利息
account.apply_interest(time)