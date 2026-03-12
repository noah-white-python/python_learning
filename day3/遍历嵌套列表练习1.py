scores = [
    [85, 92, 78],
    [90, 88, 95],
    [72, 65, 80],
    [88, 91, 85]
]
i = 0
for row in scores:
    total = sum(row)
    average = total / len(row)
    i = i+1
    print(f"student{i} {total}, {average:.2f}")