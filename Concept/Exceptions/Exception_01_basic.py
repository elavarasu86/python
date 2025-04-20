class Person():
    def __init__(self, name):
        self.name: str = name
        self.age: int

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        if age < 0:
            #we are raising python provided exception
            raise ValueError("Age cannot be in Negative")
        else:
            self._age = age


def main():
    try:
        person = Person("Ela")
        person.age = 10
        print(f"Name is : {person.name} and Age is: {person.age}")
    except ValueError as error:
        print(f"Error: {error}")

if __name__ =='__main__':
    main()