class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"person:{self.name}, age:{self.age}"
person = Person("Noah",18)
print(person)
print(str(person))

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"dog:{self.name}, age:{self.age}"
dog = Dog("rex",18)
print(repr(dog))