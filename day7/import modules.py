import math
import random
import datetime
num = random.randint(1,100)
result = math.sqrt(num)
print(f"{result:.2f}")
now = datetime.datetime.now()
print("当前时间是:", now.strftime("%Y-%m-%d %H:%M:%S"))