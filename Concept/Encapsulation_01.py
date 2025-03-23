class BankAccount():
    '''
    Encapsulation restricts direct access to data and protect it

    Python uses access modifiers to implement encapsulation:

    Public: Accessible from anywhere.

    Protected: Accessible within the class and its subclasses (denoted by a single underscore prefix,
    e.g., _attribute).

    Private: Accessible only within the class (denoted by a double underscore prefix, e.g., __attribute).
    Python uses name mangling to make it harder, but not impossible, to access these attributes directly
    from outside the class.

    Encapsulation can be achieved using getter and setter methods, also known as property decorators,
    which allow controlled access to attributes.
    '''

    def __init__(self, account_number, balance=0):
        self.__account_number = account_number  # private attribute
        self._balance = balance  # protected attribute

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount > 0:
            self._balance = amount
        else:
            print("Invalid amount")

    def get_account_number(self):
        return self.__account_number


account = BankAccount("1234567890")
print(account.get_balance())  # Access using getter method
account.set_balance(1000)  # Modify using setter method
print(account.get_balance())
print(account.get_account_number())
