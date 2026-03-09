number = 10
if int(input("enter a number"))==number:
    print("you are right")
elif int (input("you are wrong,try again")) == number:
    print("you are right")
elif int(input("try it one more time")) == number:
    print("you are right")
else:
    print("the number in my mind is 10")