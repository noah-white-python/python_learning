import random
num = random.randint(1,10)
number1 = int(input("guess the number"))
if number1 == num:
    print("the number is right")
elif number1 > num:
    print("the number is high")
else:
    print("the number is low")
if number1 != num:
    number2 = int(input("guess another number"))
    if number2 == num:
        print("the number is right")
    elif number2 > num:
        print("the number is high")
    else:
            print("the number is low")
if number2 != num:
    number3 = int(input("try again"))
    if number3 == num:
        print("you are right")
    elif number3 > num:
        print("the number is high")
    else:
        print("the number is low")