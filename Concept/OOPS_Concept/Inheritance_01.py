class Person:
  def __init__(self, fname, lname):
    '''
        Initializer will be called from child.
    '''
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

# __init__() method will be automatically created and arguments will be passed and
# then Parent initializer will be called.
x = Student("Mike", "Olsen")
x.printname()

#######################
#Parent class
class Instrument():
    def play(self):
        print("Instrument is playing")

#Child Class inherits Parent class by receiving parent class as argument.
class Guitar(Instrument):
    def play(self):
        #super function used to access Parent initializer
        super().play()
        print("Guitar strums")


guitar = Guitar()
guitar.play()