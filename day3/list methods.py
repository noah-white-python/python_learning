fruits = ["apple","banana","orange","mango"]

#append  添加单个元素
fruits.append("pear")
print(fruits)

#extend  添加多个元素
fruits.extend(['peaches',"watermelon"])
print(fruits)

#remove  删除指定值
fruits.remove("pear")
print(fruits)
#(只删除第一个匹配的)

#pop  删除并返回元素
last = fruits.pop()
print(fruits)

second = fruits.pop(2)
print(fruits)

nums = [3, 1, 4, 1, 5, 9, 2]
#sort  原地排序
nums.sort()
print(nums)   #默认升序

#降序
nums.sort(reverse=True)
print(nums)

words = ["banana", "apple", "fig", "cherry"]
words.sort(key=len)
print(words)

#与sorted区别,sort返回原列表,sorted返回新列表(原列表不变)
nums_1 = [3, 1, 2]
nums_1.sort()
print(nums_1)
nums_2 = [3, 1, 4, 1, 5, 9, 2]
new2 = sorted(nums_2)
print(nums_2)
print(new2)
