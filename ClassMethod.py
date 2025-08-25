# Class methods = Allow operations related to the class itself
# Take (cls) as the first parameter, which represents the class itself.
#
# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself

class Student:

    count = 0
    total_gpa = 0
    name_list = []

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
        Student.name_list.append(name)

    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total students: {cls.count}" # Returns how many students have been created.

    @classmethod
    def get_average_gpa(cls): # cls refers to Student class itself.
        if cls.count == 0:
           return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count}"

    @classmethod
    def get_name_list(cls):
        return f"Name list: {cls.name_list}"

student1 = Student("Eugene", 3.5)
student2 = Student("Spongebob", 4.0)
student3 = Student("Squidward", 3.0)

print(Student.get_count())
print(Student.get_average_gpa())
print(Student.get_name_list())