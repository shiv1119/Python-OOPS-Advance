class User:
    def __init__(self, username, email, age = None, address = None, roles = None):
        if roles is None:
            roles = []
        self.email = email
        self.username = username
        self.age = age
        self.address = address
        self.roles = roles

    def add_roles(self, role):
        self.roles.append(role)

u1 = User("shiv", "shiv@gmail.com", 21)
u1.add_roles("student")
u1.add_roles("class leader")
u2 = User("sarvesh", "sarvesh@gmail.com")
print(u2.age)