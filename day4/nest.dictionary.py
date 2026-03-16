school = {
    "Alice": {"math": 92, "english": 85, "science": 78},
    "Bob":   {"math": 67, "english": 73, "science": 88},
    "Carol": {"math": 95, "english": 91, "science": 97},
}

print(school.get("Bob", {}).get("science"))  # 88

school["Alice"]["math"] = 96

school["Bob"]["history"] = 80

average = {}
for key, values in school.items():
    average[key] = sum(values.values()) / len(values)
    print(f"{key} 的平均分：{average[key]:.2f}")

best = None
best_average = -1
for name, avg in average.items():
    if avg > best_average:
        best_average = avg
        best = name
print(best)