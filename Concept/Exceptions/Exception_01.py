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
