balance = 1000.0
while True:
    money = float(input("enter a number you want to withdraw"))
    if money == 0:
        print(f"thanks for using,final money is {balance}")
        break
    if money > balance:
        print(f"not sufficient funds,the current balance is {balance}")
    else:
        balance = balance - money
        print(f"withdrawal successful,the remaining balance is {balance}")
        if balance == 0:
            print("you have no money yet")
            break
