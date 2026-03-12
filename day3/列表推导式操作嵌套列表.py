orders = [
    [120, 350, 80],
    [500, 200, 150, 90],
    [60, 45, 300]
]
print([num for row in orders for num in row ])
print([num for row in orders for num in row if num > 100])
print(f"{[num*0.9 for row in orders for num in row]}")