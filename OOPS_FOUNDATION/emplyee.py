class Employee:
    company_name = "Googlu Baba"
    employees_count = 0

    __slots__ = ["name", "salary"]
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employees_count += 1

    def give_raise(self, percent):
        self.salary = self.salary * (percent / 100) + self.salary

    def __del__(self):
        print("Object Destroyed")


emp1 = Employee("Shiv", 15000)
emp2 = Employee("Sarvesh", 20000)

print(Employee.employees_count) #2
