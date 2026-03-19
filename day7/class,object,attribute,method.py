

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

my_dog = Dog("rex",3)
print(my_dog.name)
print(my_dog.age)


class Dog:
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name
my_dog = Dog("rex")
print(Dog.species)
print(my_dog.species)

class Dog:
    def __init__(self,name):
        self.name = name
    def bark(self):
        return f"{self.name} bark"
my_dog = Dog("rex")
print(my_dog.bark())