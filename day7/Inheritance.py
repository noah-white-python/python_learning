class Animal:
    def __init__(self,name):
        self.name = name
    def bark(self):
        return f"{self.name} bark"
class Dog(Animal):
    pass
dog = Dog("rex")
print(dog.bark())