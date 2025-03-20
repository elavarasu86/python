###  __init__() ###
# init method is similar to constructor in java, its purpose is to initialize variable. 
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

class Car:
    year:int
    def __init__(self,brand="BMW",model="X7",year=2025):
        print("init function will be called automatically when an object is created")
        self.brand =brand
        self.model=model
        self.year =year

    def display_info(self):
        print("Brand: ",self.brand)
        print("Model: ",self.model)
        print("Year: ",self.year)

#Object creation for Car
car =Car()
car.display_info()
#Object creation for Car
car2 =Car("Honda","CRV",2026)
car2.display_info()

'''
Output:
init function will be called automatically when an object is created
Brand:  BMW
Model:  X7
Year:  2025
init function will be called automatically when an object is created
Brand:  Honda
Model:  CRV
Year:  2026
'''

###################################
