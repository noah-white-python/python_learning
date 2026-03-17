class_a = {"Alice", "Bob", "Charlie", "David"}
class_b = {"Charlie", "David", "Eve", "Frank"}


s1 = class_a & class_b
print(class_a & class_b)
print(class_a - s1)
print(len(class_a)+len(class_b)-len(s1))