import random
i = random.randint(1,100)
print("enter a number in range 1-100")
while True:
    number = int(input())
    if number < i:
        print("the number is low")
    elif number > i:
        print("the number is high")
    else:
        print("you are right");
        break
    EXCEPT:print("enter a new number")