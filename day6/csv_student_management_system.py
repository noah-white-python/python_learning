students = []
with open(r"scores1.csv","r",encoding = "utf-8")as f:
    lines = f.readlines()

for line in lines[1:]:
    line = line.strip()
    name,score = line.split(",")

    students.append({"name":name, "score":int(score)})
print(students)

total = 0
for student in students:
    total += student["score"]

average = total / len(students)
print(f"{average:.2f}")

max_score = students[0]["score"]
min_score = students[0]["score"]
for student in students:
    if student["score"] > max_score:
        max_score = student["score"]
    elif student["score"] < min_score:
        min_score = student["score"]
print(f"最高分是{max_score}")
print(f"最低分是{min_score}")