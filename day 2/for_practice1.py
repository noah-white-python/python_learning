# for 变量 in 序列：
# range（）
#range (stop) 从0开始

for i in range(5):
    print(i,end=" ")

print(" ")

#range(start,stop)
for i in range(1,6):
    print(i,end=" ")

print(" ")

#range(start,stop,step)

for i in range(10,20,2):
    print(i,end=" ")

print(" ")

#遍历字符
for char in "hello":
    print(char,end=" ")

print("")

#遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit,end=" ")

print("")


#break 提前退出
#continue 跳过档次
for i in range(1,10):
    if i == 5:
        break
    print(i,end=" ")

print("")

for i in range(1,10):
    if i == 3:
        continue
    print(i,end=" ")

print(" ")
#嵌套


#打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}")



