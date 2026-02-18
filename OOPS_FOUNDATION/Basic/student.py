class Student:
    school_name = "Alliance Unviersity"
    student_count = 0

    __slots__ = ["name", "age", "grade"]
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.student_count += 1

    def get_details(self):
        return f"{self.name}, {self.age} years old, Grade {self.grade}"

    def update_grade(self, new_grade):
        self.grade = new_grade

    # How this obejct should look wne object is printed
    def __repr__(self):
        return f"Student(name'{self.name}', age'{self.age}')"
    
    # This is equality operator used to comapre the content of the two oebjects
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.name == other.name and self.age == other.age and self.grade == other.grade


student1 = Student("Shiv Nandan Verma", 21, "12th")
student2 = Student("Shiv Nandan Verma", 21, "12th")
print(Student.student_count)
print(student1)
print(student1 == student2) #True
print(student1 is student2) #False


    
