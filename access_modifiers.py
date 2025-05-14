class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name           # Public
        self._salary = salary      # Protected (convention)
        self.__ssn = ssn           # Private (name mangled)

    def show_info(self):
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN:", self.__ssn)

# Create object
emp = Employee("John Doe", 50000, "123-45-6789")

# Access public variable
print("Accessing public variable:", emp.name)        # Works

# Access protected variable
print("Accessing protected variable:", emp._salary)  # Works, but discouraged (convention)

# Try accessing private variable
try:
    print("Accessing private variable:", emp.__ssn)   # Fails
except AttributeError as e:
    print("Error accessing private variable:", e)

# Access private variable using name mangling
print("Accessing private variable using name mangling:", emp._Employee__ssn)  # Works
