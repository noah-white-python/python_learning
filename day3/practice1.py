numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
list_1 = []
for i in numbers:
    if i not in list_1:
        list_1.append(i)
print(list_1)

for j in numbers:
    if j > 4:
        print(j)