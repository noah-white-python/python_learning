records = (
    ("Alice", "math",    95),
    ("Bob",   "math",    80),
    ("Alice", "english", 88),
    ("Bob",   "english", 76),
    ("Carol", "math",    92),
    ("Carol", "english", 85),
)

result = {}
for name, subject, score in records:
    if name not in result:
        result[name] = {}
    result[name][subject] = score
print(result)

for name,subjects in result.items():
    s = sum(subjects.values())
    print(f"{name}:{s/len(subjects)}")