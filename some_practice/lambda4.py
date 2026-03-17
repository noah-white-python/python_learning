celsius = [0, 20, 37, 100]
result = map(lambda x: float(x*9/5+32),celsius)
print(list(result))