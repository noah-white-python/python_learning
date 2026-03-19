
#无返回值
def say_hi():
    print("Hi")

#单个返回值
def square(x):
    return x ** 2
x = float(input("enter a number"))
print(f"{square(x):.2f}")

#多个返回值(本质是列表)
def min_max(lst):
    return min(lst), max(lst)

lo, hi = min_max([3, 1, 4, 1, 5])
print(lo, hi)