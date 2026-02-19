class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes some sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Bhau Bhau!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow Meow!")


dog = Dog("Buddy")
cat = Cat("Kitty")

dog.speak()
cat.speak()