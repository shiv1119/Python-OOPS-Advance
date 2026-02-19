#When an object is created via a class method, that class method is called a factory method.

class Validator:
    @staticmethod
    def validate_username(username):
        error_message = []
        is_valid = True
        if len(username) < 8:
            is_valid = False
            error_message.append("The user name should be of 8 or more characters")
        
        if any(char.isupper() for char in username):
            is_valid = False
            error_message.append("The username should be lower case")

        if is_valid:
            return True
        else:
            raise ValueError("\n".join(error_message))
        
    @staticmethod
    def validate_password(password):
        is_valid = True
        error_message = []

        if len(password) < 8:
            is_valid = False
            error_message.append("Password should be of 8 or more characters.")
        
        if not any(char.isupper() for char in password):
            is_valid = False
            error_message.append("The password should contain atleast one uppercase letter")
        
        if not any(char.islower() for char in password):
            is_valid = False
            error_message.append("The password should conatin atleast one lower case letter")
        
        if not any(char.isdigit() for char in password):
            is_valid = False
            error_message.append("The password should contain atleast one digit")
        
        if is_valid:
            return True
        else:
            raise ValueError("\n".join(error_message))

        
class User:
    use_case = "Login"
    def __init__(self, name, password):
        if Validator.validate_username(name):
            self.name = name
        if Validator.validate_password(password):
            self.password = password

    @classmethod #Factory method
    def create_user(cls, data):
        return cls(data['username'], data['password'])
    
    @classmethod
    def update_use_case(cls, user_case):
        cls.use_case = user_case

data = {
    "username": "shivnandan",
    "password": "Demo@1234"
}
user = User.create_user(data)
print(user.name)
print(user.password)
    


    

