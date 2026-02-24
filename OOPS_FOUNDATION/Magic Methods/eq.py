class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
    
p1 = Person("Shiv")
p2 = Person("Shiv")
print(p1 == p2)