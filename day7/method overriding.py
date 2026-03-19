class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} make noise"
class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof"
class Cat(Animal):
    def speak(self):
        return f"{self.name} says miaow"

dog = Dog("旺财")
cat = Cat("咪咪")
print(dog.speak())
print(cat.speak())