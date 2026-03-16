orders = [
    {"name": "Alice", "product": "apple",  "quantity": 3},
    {"name": "Bob",   "product": "banana", "quantity": 5},
    {"name": "Alice", "product": "orange", "quantity": 2},
    {"name": "Carol", "product": "apple",  "quantity": 4},
    {"name": "Bob",   "product": "apple",  "quantity": 1},
]

result = {}
for order in orders:
    name = order["name"]
    quantity = order["quantity"]
    result[name] = result.get(name, 0) + quantity
print(result)
max_value = max(result.values())
for key,value in result.items():
    if max_value == value:
        print(f"{key}")