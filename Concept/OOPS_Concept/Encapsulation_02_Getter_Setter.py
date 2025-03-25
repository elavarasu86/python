class Person():
    '''
    Program to show use of normal get() and set() methods.
    '''

    def __init__(self, age=0):
        self.age = age

    def get_age(self):
        return self.age

    def set_age(self, ageSetter):
        self.age = ageSetter


person1 = Person()
person1.set_age(38)
print(person1.get_age())
##########################################################################################
class Person():
    '''
    In Python property()is a built-in function that creates and returns a property object.
    A property object has three methods, getter(), setter(), and delete().
    property() function in Python has four arguments property(fget, fset, fdel, doc),
    fget is a function for retrieving an attribute value.
    fset is a function for setting an attribute value.
    fdel is a function for deleting an attribute value.
    doc creates a docstring for attribute.
    A property object has three methods, getter(), setter(), and delete()
    to specify fget, fset and fdel individually.
    '''

    def __init__(self):
        print("Initialization method called")
        self._age = 0

    def get_age(self):
        print("Inside get method")
        return self._age

    def set_age(self, ageSetter):
        print("Inside set method")
        self._age = ageSetter

    def del_age(self):
        print("Inside Delete method")
        del self._age

    # property function helps setting age and getting age.
    age = property(get_age,set_age,del_age)


person1 = Person()
person1.age=38
print(person1.age)
##########################################################################################
class Person():
    '''
    Python @property is one of the built-in decorators.
    The main purpose of any decorator is to change your class methods or attributes
    in such a way so that the user of your class no need to make any change in their code
    '''

    def __init__(self):
        print("Initialization method called")
        self._age = 0

    @property
    def age(self):
        print("Inside get method")
        return self._age

    @age.setter
    def age(self, ageSetter):
        print("Inside set method")
        if (ageSetter < 18):
            raise  ValueError("Sorry your age is below eligibility criteria!")
        self._age = ageSetter

person1 = Person()
person1.age = 38
print("Age is set")
print(person1.age)
##########################################################################################
