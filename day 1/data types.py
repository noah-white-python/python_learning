#int float string bool none
a = 10
print(type(a))

#int运算

print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10%3)
print(10**3)

b = 17.5
print(type(b))

#精度问题
print(0.1+0.2==0.3)

print(abs(0.1+0.2-0.3)<1e-9)

import math
print(math.isclose(0.1+0.2,0.3))
print(math.isclose(100.0, 102.0, rel_tol=0.01))
#使用decimal模块
from decimal import Decimal,getcontext
a = Decimal("0.1")
b = Decimal("0.2")
c = Decimal("0.3")
print(a+b==c)

#使用fractions模块
from fractions import Fraction
a = Fraction(1,10)
b = Fraction(2,10)
c = Fraction(3,10)
print(a+b==c)
print(float(a+b))


#转换成整数计算

c = "Hello"
print(type(c))

name = "python"
#大小写和首字母大写
print(name.upper())
print(name.capitalize())
print(name.lower())
#长度
print(len(name))
#拼接
print("hello" + " " + name)
#重复
print("ha" * 3)
#索引(从零开始)
print(name[0])
print(name[-1])
#切片
print(name[1:3])
print(name[2:])
#判断是否包含
print("py" in name)
#替换
print(name.replace("p","P"))
#分割
sentence = "苹果，香蕉，橙子"
print(sentence.split(","))
#格式化字符串
#1
age = 18
name = "小明"
print(f"my name is {name} and my age is {age}")
#2  format
print("my name is {} and my age is {}".format(name,age))
#3
print("my name is %s and my age is %d"%(name,age))


d =  True
print(type(d))

#bool is special int
print(True + True)
print(True * 5)

#which value = False?
print(bool(0))
print(bool(""))          #空字符串
print(bool(None))
print(bool([]))          #空列表

#which value = True?
print(bool(1))
print(bool("hello"))
print(bool([1,2,3]))


e = None
print(type(e))

#判断是否为None
if e is None:
    print("e is None")

#系统没有return默认返回None
def 什么都不做():
    pass
result = 什么都不做()
print(result)
