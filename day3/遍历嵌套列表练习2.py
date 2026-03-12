seats = [
    [101, 102, 103],
    [104, 105, 106],
    [107, 108, 109]
]

for i, row in enumerate(seats, 1):
    for j, student in enumerate(row, 1):
        print(f"学号 {student} 在第{i}排第{j}列")