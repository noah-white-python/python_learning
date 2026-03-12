#create lists

fruits = ["apple","banana","cherry","mango"]
numbers = [1,2,3,4,5,6,7,8,9,10]
mixed = [108,"hello",3.14,True]
empty = []
#construct function

chars = list("hello")
from_range = list(range(5))
#list comprehension

squares = [x for x in range(1,11)]
even_number = [x for x in range(1,11) if x % 2 == 0]
#nest

martix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

#index

print(fruits[0])
print(fruits[-1])

#section

print(numbers[2:6])     #2-5
print(numbers[:2])      #从头到1
print(numbers[2:])      #从2到结尾
print(numbers[:])       #完整复制列表
#带步长

print(numbers[::2])      #每隔一个取一个
print(numbers[2:2])      #从2开始,每隔一个取一个
print(numbers[::-1])     #反转列表
print(numbers[7:2:-1])   #从7到2,每隔一个取一个

#嵌套列表索引
print(martix[0])
print(martix[1][2])
print(martix[-1][-1])

#索引修改
clothes = ["pants","sweater","jeans","coat"]
clothes[1] = "skirts"
print(clothes)
clothes[0:2] = ["a","b"]
print(clothes)
clothes[1:1] = ["x","y"]
print(clothes)
del clothes[0]
print(clothes)
