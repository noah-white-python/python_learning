#is the number prime?

def func(n):
    for x in range(2,int(n**0.5+1)):
        if n % x == 0:
            return False
    return True
number = float(input("Enter a number: "))
print(func(number))