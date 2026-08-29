class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    ...

d = Dog()
d.speak()