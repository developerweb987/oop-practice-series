# Employee class
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_employee_info(self):
        return f"Employee Name: {self.name}, Position: {self.position}"

# Department class using aggregation
class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: Department holds reference to Employee object

    def display_department_info(self):
        print(f"Department: {self.department_name}")
        print(self.employee.display_employee_info())

# Example usage
emp1 = Employee("Alice Johnson", "Software Engineer")
department1 = Department("IT", emp1)

# Displaying department and employee info
department1.display_department_info()
