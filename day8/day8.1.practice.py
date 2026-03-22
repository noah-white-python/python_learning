import numpy as np
even_number = np.arange(0, 10, 2)
print(even_number)
multiples_3 = np.arange(0, 20, 3)
print([number ** 2 for number in multiples_3])

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
for row in matrix:
    print(sum(row))

scores = [88, 72, 95, 60, 45, 83, 76]
average = sum(scores) / len(scores)
print(f"average is :{average:.2f}")

for score in scores:
    if score > average:
        print(f"{score:}")


print(max(scores))
print(min(scores))