#变量
name1 = "小明"
age1 = 18
height1 = 175.0

#命名规则：数字 下划线_ 和字母
#不能以数字开头，不能用关键字

#动态类型

x1 = 1
x1 = "一个变量"
x1 = 3.14


#常见数据类型

age = 18
print(age)
height = 1.95
print(height)
name = "小李"
print(name)
is_student = True
print(is_student)
res = None
print(res)

#多重赋值

x,y,z = 1,2,3
a = 10
b = 20
a,b = b,a
print(a,b)

x=y=z=0

#数组
m = [1,2,3]
n=m
n.append(4)
print(m)



#全大写表示不修改
PI = 3.1415926
MAX_SCORE = 100


#def 创建函数 方便调用
x2 = 10
def my_function():
    x = 20
    print(x2)
print(x2)

x3 = 100
def my_function2():
    global x3
    x3 = 200
print(x3)