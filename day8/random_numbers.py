import numpy as np
a = np.random.rand(3,3)
print(a)
b = np.random.randint(0,3)
print(b)

c = np.random.uniform(3,10,(3,3))
print(c)

x = [1,2,3,4,5]
print(np.random.choice(x))
print(np.random.choice(x,3))
print(np.random.choice(x,3,replace = False))

np.random.shuffle(x)
print(x)

y = np.random.permutation(x)
print(y)