#def 函数名
#函数体
#返回值

def greet(name,age):
    print(f"i am {name}, i am {age}")
greet("John",23)

#可变位置参数

def total(*numbers):
    return sum(numbers)
print(total(1,2,3,4,5))

#关键字参数

def show_info(**info):
    for key,value in info.items():
        print(f"you are {key} : {value}")
show_info(name = "Alice" , city = "Tokyo")

#仅关键字参数

def connect(host , * , port = 80 , timeout = 30):
    pass

#参数规则     (/左边仅参数,*右边仅关键词)
def func(pos , / , normal , * , kw_only):
    pass
