age = int(input("enter your age"))
height = int(input("enter your height in cm"))
accompanied_by_parents = input("are you accompanied by your parents?") == "yes"
if 12 <= age <= 60 or accompanied_by_parents:
    if height >=150:
        print("you can play all projects")
    elif 120 <= height <= 150:
        print("you can play some projects")
    else:
        print("you can play in kids zone")
else:
    print("you can not enter amusement park")