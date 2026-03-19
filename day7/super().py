class Animal:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def info(self):
        return f"名字:{self.name}  年龄:{self.age}"

class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed = breed
    def info(self):
        base = super().info()
        return f"{base}  品种:{self.breed}"
dog = Dog("旺财",3,"拉布拉多")
print(dog.info())