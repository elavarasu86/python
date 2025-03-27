# "Duck typing" = Another way to achieve polymorphism besides Inheritance
#                            Object must have the minimum necessary attributes/methods
#                            "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

# Even though car is not animal type like Dog and cat still Car considered as Animal like because of its attributes.
class Car:
    alive = True

    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)