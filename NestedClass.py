# Nested class = A class defined within another class.
#               class Outer:
#               class Inner:
#
# Benefits: Allows you to logically group classes that are closely related
#           Encapsulates private details that aren't relevant outsideof the outer class
#           Keeps the namespace clean; reduces the possibility of naming conflicts

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)


    def list_employees(self):
        return [employees.get_details() for employees in self.employees]

company = Company("Krusty Krab")

company.add_employee("Eugene", "Manager")
company.add_employee("Spongebob", "Cook")
company.add_employee("Squidward", "Cashier")

print(company.list_employees())

for employee in company.list_employees():
    print(employee)
