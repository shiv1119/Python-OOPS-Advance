class Animal:

    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"This is an animal named {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def info(self):
        super().info()
        print(f"It is as {self.breed} dog")

dog = Dog("Tommy", "Bull Dog")
dog.info()