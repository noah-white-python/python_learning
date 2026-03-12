score = float(input("enter your score: "))
attendance = float(input("enter your attendance: "))
if attendance > 0.8:
    if score >= 90:
        print("excellent")
    elif score >= 75:
        print("good")
    elif score >=60:
        print("pass")
    else:
        print("fail")
else:
    if score >=60:
        print("cancel the rating because ur attendance is low")
    else:
        print("you failed the exam and attendance is low,take a make-up exam please")