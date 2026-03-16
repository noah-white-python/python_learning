#items keys values get

person = {"name":"noah","age":25,"address":"tokyo"}
for key in person:
    print(key)
for value in person.values():
    print(value)
for key,value in person.items():
    print(f"{key}: {value}")
print(person.get("name"))
print(person.get("age"))
print(person.get("address"))