class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Student(Person):
    def __init__(self, name, age, specialty):
        super().__init__(name, age)
        self.specialty=specialty

    def displayStudent(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Specialty:",self.specialty)

student1=Student("Name",15,"CS")

student1.displayStudent()