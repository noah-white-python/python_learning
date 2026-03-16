students = [("Alice", 85), ("Bob", 92), ("Carol", 78), ("David", 92)]

# 1. 打印分数最高的学生（分数相同时打印所有人）
max_score = max(students, key=lambda s: s[1])[1]
for name, score in students:
    if score == max_score:
        print(name)