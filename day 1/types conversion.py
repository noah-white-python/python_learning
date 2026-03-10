#类型转换
#非数字的字符串不能转换为整数
#string → int
age = int("18")
print(age)

#int → string
num = str(100)
print(num)

#string → float
price = float("99.9")
print(price)

#int → float
x = float(5)
print(x)

#float → int
y = int(5.1)
print(y)

#四舍五入用round
print(round(3.14))

#view types
print(type(18))
print(type(18.0))
print(type("18"))
print(type(True))
print(type(None))

x = 18
print(isinstance(x,int))
print(isinstance(x,float))
print(isinstance(x,str))
