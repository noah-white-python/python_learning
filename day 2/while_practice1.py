#while 执行流程
#判断条件（true就执行）→再判断→再执行→false就退出


import random
answer = random.randint(0,100)
count = 0
while True:
    number = int(input("enter a number range from 0 to 100: "))
    count = count + 1
    if number > answer:
        print("the number is too high")
    elif number < answer:
        print("the number is too low")
    else:
        print("you are right")
        break
print(f"you guess {count} times")