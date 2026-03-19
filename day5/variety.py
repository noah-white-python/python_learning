x = "我是全局变量"
def func():
    y = "我是局部变量"
    print(x)
    print(y)
func()
print(y)