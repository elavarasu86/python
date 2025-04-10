# Static methods = A method that belong to a class rather than any object from that class (instance)
#                                Usually used for general utility functions

# Instance methods - Best for operations on instances of the class (objects)
# Static methods - Best for utility functions that do not need access to class data

'''
It is not bound to either the class or the instance.
It does not take any implicit first argument.
It cannot access or modify class or instance state.
It is essentially a regular function within the class namespace.
It is defined using the @staticmethod decorator. 
'''

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} is the {self.position}"

    # @staticmethod decorator help set a method as static(class level) method.
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions


print(Employee.is_valid_position("Rocket Scientist"))

steve = Employee("Steve", "Manager")
hussain = Employee("Hussain", "Cashier")
prem = Employee("Prem", "Cook")

print(steve.get_info())
print(hussain.get_info())
print(prem.get_info())
