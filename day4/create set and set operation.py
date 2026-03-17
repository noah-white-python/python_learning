s1 = {1,2,3,4,5,6,7,8,9}
s2  = set([11,12,12,14])
empty = set()

#加减长度随机取出数字检测是否在集合中
print( 9 in s1 )
s1.add(10)
s1.remove(10)
s1.discard(9)
len(s1)
print(9 in s1)
print(s1.pop())

#并集 交集 差集 对称差集
print(s1 | s2)
print(s1.union(s2))

print(s1 & s2)
print(s1.intersection(s2))

print(s1 - s2)
print(s1.difference(s2))

print(s1 ^ s2)
print(s1.symmetric_difference(s2))


s3 = {1,2,3,4,5}
s4 = {1,2,3}
print(s3 >= s4)
print(s3 <= s4)
print()