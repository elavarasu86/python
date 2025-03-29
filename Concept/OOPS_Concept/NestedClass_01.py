# Nested class = A class defined within another class
#                            class Outer:
#                                class Inner:

# Benefits: Allows you to logically group classes that are closely related
#                 Encapsulates private details that aren't relevant outside of the outer class
#                 Keeps the namespace clean; reduces the possibility of naming conflicts

class Company:
    # Nested Class this is kind of attribute to company class
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employee = []

    def add_employee(self, name, position):
        # created an attribute and called Employee constructor
        new_employee = self.Employee(name, position)
        self.employee.append(new_employee)

    def list_employee(self):
        return [employees.get_details() for employees in self.employee]

company = Company("ABC")

company.add_employee("Selvan","CEO")
company.add_employee("Maran","Manager")

for employee in company.list_employee():
    print(employee)