#tuple()  不能增删改
tuple = (1,2,3)
print(tuple)

#可以混合类型,可以不带() (但不推荐)
t = (1,3.14,"hello",True)
print(t)

#即使只有一个元素也需要带,
t1 = (1,)
print(t1)

t = ()  #空元组
print(t)

#索引和修改同列表

#一些可以做的操作

t2 = (3,1,2,1)
print(len(t2))
print(t2.count(1))
print(t2.index(2))
print(1 in t2)

#元组拆包
t3 = (10,20,30)
a,b,c = t3
print(a)
print(b)
print(c)

def get_into():
    return "Tom",19,"beijing"
name,age,city = get_into()
print(name)
