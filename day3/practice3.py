inventory = {
    "apple": 50,
    "banana": 30,
    "orange": 0,
    "grape": 15,
    "mango": 0,
}

for key,value in inventory.items():
    if value == 0:
        print(f"{key}")
    if value > 20:
        inventory[key] = value / 2
