print("请告诉我你的体重:(千克)")
weight = input()
weight = float(weight)
print("请告诉我你的身高:(米)")
height = input()
height = float(height)
BMI = weight/height/height
print(f"你的体重指数是{BMI}")