#斐波那契数列
#0 1 1 2 3 5 8



def func(n):
    a = 0
    b = 1
    print(a)
    for i in range(1,n):
        print(b)
        a,b = b,a+b

func(10)