# Aggregation = A relationship where one object contains references to other INDEPENDENT objects
#                           "has-a" relationship

# Composition = The composed object directly owns its components, which cannot exist independently
#                            "owns-a" relationship
class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power


class Wheel:
    def __init__(self, size):
        self.size = size
#Car own Engine and Wheel classes
# If we remove Car object(CRV) we will not have Engine and Wheel
class Car:
    def __init__(self, make, model, horse_power, size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power) # depends on Car
        self.wheel = Wheel(size) # depends on Car

    def print_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheel.size}in"

CRV = Car("Honda","CRV","300",20)
print(CRV.print_car())