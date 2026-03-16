students = [("Alice", 85), ("Bob", 92), ("Carol", 78), ("David", 92)]
max_score = max(student[1] for student in students)
for score in students:
    if score[1] == max_score:
        print(score[0])


sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
for student in sorted_students:
    print(f"{student[0]}: {student[1]}")
