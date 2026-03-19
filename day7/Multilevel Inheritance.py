class Animal:
    def speak(self):
        return ". . ."

class Dog(Animal):
    def speak(self):
        return "汪汪"
class GoldenRetriever(Dog):
    def speak(self):
        return super().speak() + "(友善的摇尾巴)"
g = GoldenRetriever()
print(g.speak())