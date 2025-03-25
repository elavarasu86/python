class College1():
    name = "CollegeOne"
    def course(self):
        print(f"{College1.name} course")

class College2():
    name = "CollegeTwo"
    def course(self):
        print(f"{College2.name} course")
    def play(self):
        print("Students can play")

# Here we are inheriting two class
class Student(College1,College2):
    def __init__(self,name):
        self.name=name

student = Student("Ela")
print((student.name))
print(College1.name)
# by default College1 method is executing.
student.course()
student.play()