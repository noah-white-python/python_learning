print("something",end=" ")
print("else")

name1 = "小明"
age = 18
print(name1,age,sep=",")
print(name1,age,sep="")

score = 98.57
print(f"score:{score:.2f}")
print(f"score:{score:.0f}")

print(f"{age:05d}")
print(f"{'居中':^10}")
print(f"{'左对齐':<10}丨")
print(f"{'右对齐':>10}丨")

name = input("enter ur name")
print(f"ur name is {name}")

while True:
    try:
        age = int(input("enter ur age"))
        break
    except ValueError:
        print("enter again")
    print("ur age is ",age)

x,y = input("enter two number").split()
print(x,y)

