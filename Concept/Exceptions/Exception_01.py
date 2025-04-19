my_input: str = 'Ten'
try:
    total_days: int = int(my_input) * 365
    print(f"Days on Earth is {total_days}")
except ValueError as e:
    print(f"Bad input: {e}")
except TypeError as e:
    print(f"Bad input: {e}")
###########################################################################


my_input: str = 'Ten'
try:
    total_days: int = int(my_input) * 365
    print(f"Days on Earth is {total_days}")
except (ValueError, TypeError) as e:#Combining exception in one Block.
    print(f"Bad input: {e}")

#####################################ZeroDivisionError######################################
#input a and b value and convert a and b to integer.
a=int(input("Enter value of a"))
b=int(input("Enter value of b"))

try:
    c=a/b
    print(f"Value of c is {c}")
#below exception block will be executed only when divisor is zero.
except ZeroDivisionError:
    print(f"Divisor is Zero")
#below exception block will be executed when specific except block is not available.
except Exception as e:
    print(f"We got a {e} exception")
#finally block will be executed irrespective of exception arise or not.
finally:
    print("Clean-up and closing program")

print("Thank You")