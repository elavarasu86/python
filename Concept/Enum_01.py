from enum import Enum, auto

'''
An enum (short for enumeration) in Python is a way to define a set of symbolic names bound to unique values.

Enums provide several benefits over using plain constants:
Readability: Enums replace "magic numbers" or strings with meaningful names, making the code easier to understand.
Type safety: Enums prevent accidental use of incorrect values, as they are distinct types.
Grouping: Enums group related constants together, improving code organization.
Iteration: Enums can be iterated over, allowing easy access to all members.
Comparison: Enum members can be compared by identity (is) or equality (==).
'''
class Color(Enum):
    RED = 'r'
    GREEN = 'g'
    BLUE = 'b'

class Status(Enum):
    PENDING = 1
    RUNNING = 2
    COMPLETED = 3
    FAILED = auto() # auto() assigns the next available integer value

print(Color.RED)
print(Color.RED.value)
print(Status.FAILED.value)
