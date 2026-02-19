# Static methods can be used to group the utility function 

class Validators:
    @staticmethod
    def is_valid_name(name):
        return name.isalpha()
    
    @staticmethod
    def is_valid_age(age):
        return 0 < age < 120
    
    @staticmethod
    def is_allowed_to_vote(age):
        return age > 18
    

class Voter:
    def __init__(self, name, age):
        if Validators.is_valid_name(name):
            self.name = name
        else:
            raise ValueError("Invalid Name")
        if Validators.is_valid_age(age):
            self.age = age
        else:
            raise ValueError("Invalid Age")
        
    
    def is_candidate_allowed_voting(self):
        if Validators.is_allowed_to_vote(self.age):
            print(f"{self.name} is of {self.age} years and allowed to vote.")
        else:
            print(f"{self.name} is of {self.age} years and not allowed to vote.")


candiate = Voter("Shiv", 21)
candiate.is_candidate_allowed_voting()
candiate2 = Voter("Jiya", 17)
candiate2.is_candidate_allowed_voting()

try:
    candiate3 = Voter("Shreya", -5)
    candiate2.is_candidate_allowed_voting()
except ValueError as e:
    print("Error:", e)