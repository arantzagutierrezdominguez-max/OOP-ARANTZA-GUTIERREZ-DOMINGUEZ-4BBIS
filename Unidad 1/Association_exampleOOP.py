class Student:
    def __init__(self,name):
        self.name = name

    def enroll(self, course):
        self.course = course
    def show_course(self):
        print(f"{self.name} is enrolled in {self.course.name}")

class Course:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Course: {self.name}")

#Instance
student = Student("Carlos")
course = Course ("Phyton Programming")

#Creating a relationship
student.enroll(course)

#Use the Relationship
student.enroll(course)

student.show_course()

#Output expected: "Carlos is enrolled in python Programming"
