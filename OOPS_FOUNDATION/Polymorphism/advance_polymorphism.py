class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5
    
class Square(Shape):
    def area(self):
        return 4 * 4

shapes = [Circle(), Square()]

for s in shapes:
    print(s.area())