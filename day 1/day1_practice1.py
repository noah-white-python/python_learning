name = "小明"
age = 18
height1 = 1.75
student = True
city = "北京"
print(f"my name is {name},age is {age},height is {height1},is a student;favorite city is {city}")

sentence = "  Hello, My Name Is Python!  "
print(f"{sentence.strip()}")
print(f"{sentence.lower()}")
print(f"{sentence.upper()}")
print(sentence.count("o"))
print(sentence.replace("Python","Noah_White"))
print(sentence.strip()[0:5]=="Hello")
print(sentence.strip()[0])

height = float(input("enter ur height in meter"))
weight = float(input("enter ur weight in kg"))
BMI = weight / height / height
print(f"BMI is {BMI}")
if BMI < 18.5:
    print("you are underweight")
elif BMI < 25:
    print("you are normal")
elif BMI < 28:
    print("you are obese")
else:
    print("u r overheight")
