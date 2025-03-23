''' Parent class has Move method, similarly all the child classes
will have move method with its own implementation.
'''
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

''' Child class'''
class Car(Vehicle):
  pass

''' Child class'''
class Boat(Vehicle):
  def move(self):
    print("Sail!")

''' Child class'''
class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand, end=' ')
  print(x.model)
  x.move()