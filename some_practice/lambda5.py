
students = [
    {"name": "Alice", "score": 90},
    {"name": "Bob",   "score": 85},
    {"name": "Carol", "score": 90},
    {"name": "Dave",  "score": 85},
]

sorted_students = sorted(students, key=lambda x: (-x["score"], x["name"]))

for student in sorted_students:
    print(student)