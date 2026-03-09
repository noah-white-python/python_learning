import random
number = random.randint(1,100)
number1 = int(input("enter a number"))
flag = True
while flag:
    if number == number1:
        print("you are right")
        flag = False
    else:
        if number1 < number:
            print("the number is low")
        else:
            print("the number is high")