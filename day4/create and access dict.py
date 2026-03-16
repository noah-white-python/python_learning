#创建 {}直接创建  dict()创建

person = {"name":"alice","age":"18","city":"tokyo"}
print(person)

person1 = dict(name="alice",age="18",city="tokyo")
print(person1)

#空字典

empty = {}
print(empty)
empty1 = dict()
print(empty1)

pairs = [("a","1"),("b",2)]
d = dict(pairs)
print(d)

#访问

print(person["name"])


print(person.get("email"))
print(person.get("email","N/A"))


#增删改
d["c"] = "3"
print(d)
d["b"] = "4"
print(d)
del d["c"]
print(d)
d.pop("b")
print(d)


#遍历
for key in person:
    print(key)

for val in person.values():
    print(val)

for key,value in person.items():
    print(f"{key} : {value}")

#字典推导式
squares = {x:x**2 for x in range(11)}
print(squares)