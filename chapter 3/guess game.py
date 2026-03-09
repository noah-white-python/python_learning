number = 10
number_1 = int(input("enter a number"))
if number_1 != number:
    print("you are wrong,try again")
    number_2 = int(input("enter a number"))
    if number_2 != number:
        print("you are wrong,try again")
        number_3 = int(input("enter a number"))
        if number_3 != number:
            print("you are wrong,the number in my mind is 10")
        else:
            print("you are right")
    else:
        print("you are right")
else:
    print("you are right")