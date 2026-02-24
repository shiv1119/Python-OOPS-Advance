class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User: {self.name}"

u = User("Shiv")
print(u)