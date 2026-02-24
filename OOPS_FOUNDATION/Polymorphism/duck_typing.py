class Dog:
    def speak(self):
        print("Dog Barks")

class Robot:
    def speak(self):
        print("Robotic Voice")

def make_sound(entity):
    entity.speak()

make_sound(Dog())
make_sound(Robot())