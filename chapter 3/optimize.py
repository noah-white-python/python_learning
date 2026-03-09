import random
num = random.randint(1,10)
num1 = int(input("enter a number in 1 to 10"))
if num1 == num:
    print("you are right")
else:
    if num1>num:
        print("the number is high")
    else:
        print("the number is low")
num2 = int(input("enter a number in 1 to 10 again"))
if num2 == num:
    print("you are right")
else:
    if num2>num:
        print("the number is high")
    else:
        print("the number is low")
num3 = int(input("try again"))
if num3 == num:
    print("you are right")
else:
    if num3>num:
        print("the number is high")
    else:
        print("the number is low")